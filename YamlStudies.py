import glob
import natsort as ns
import numpy as np
import pandas as pd
import re
import requests
import textwrap
import yaml

def synthesis(binvalues):
  return(np.logical_and.reduce(binvalues, 1)*1)

def split_index(df):
  return(pd.MultiIndex.from_tuples([idx.split('_') for idx in df.index], names=['model','run']))

def parse_ripf(str):
  p = re.compile(r'r(?P<r>[0-9-]+)i(?P<i>[0-9-]+)p(?P<p>[0-9-]+)f(?P<f>[0-9-]+)')
  m = p.match(str)
  return(m.groupdict() if m else [])

def indent_text(str, nspace=2):
  dedent = textwrap.dedent(str).strip()
  return(textwrap.fill(
    dedent,
    width = 80,
    initial_indent = ' '*nspace,
    subsequent_indent = ' '*nspace
  ))

def doi2dic(doi):
  url = "http://dx.doi.org/" + doi
  headers = {"accept": "application/x-bibtex"}
  r = requests.get(url, headers = headers)
  rval = r.text.replace('@article{', '')
  for char in '}{\t':
    rval = rval.replace(char, '')
  rdict = {}
  for item in rval.split('\n'):
    if '=' in item:
      kv = item.split('=')
      rdict[kv[0].strip()] = kv[1].strip().strip(',')
  if 'and' in rdict['author']:
    rdict['author'] = rdict['author'].split(' and ')[0] + ' et al.'
  return(rdict)

def find_metric(mlist, key):
  keys = [x.key for x in mlist]
  return(mlist[keys.index(key)])

class MetricEntry:

  def __init__(self, yamlentry, resolve_doi = False):
    self.__dict__.update(yamlentry)
    # print(f'instantiating {self.key} ...')
    self.metric = SubKeys(**self.metric)
    if self.has_period():
      self.period = SubKeys(**self.period)
    for key in ('plausible_values', 'classes'):
      if hasattr(self, key):
        if type(self[key]) is list:
          self[key] = [SubKeys(**x) for x in self[key]]
        else:
          self[key] = [SubKeys(**self[key])]
    if resolve_doi and type(self.doi) == type('string'):
      self.reference = '%(author)s (%(year)s) %(title)s, %(url)s' % doi2dic(self.doi)
    else:
      self.reference = str(self.doi)
    if type(list(self.data.values())[0]) is dict:
      self.data = pd.DataFrame.from_dict(self.data, orient='columns') 
      self.data.columns = [f'{self.key} {x}' for x in self.data.columns]
    else:
      self.data = pd.DataFrame.from_dict(self.data, orient='index', columns=[self.key])
    self.expand_data()
    self.data = self.data.reindex(ns.natsorted(self.data.index))
    self.data.index = split_index(self.data)

  def __str__(self):
    rval = f'- key: {self.key}\n'
    for item in ('doi', 'type', 'spatial_scope', 'temporal_scope', 'data_source'):
      if hasattr(self, item):
        rval += f'  {item}: {self[item]}\n'
    for item in ('metric', 'period'):
      if hasattr(self, item):
        rval += f'  {item}:\n' + self[item].__str__()
    for item in ('plausible_values', 'classes'):
      if hasattr(self, item):
        rval += f'  {item}:\n'
        for x in self[item]:
          rval += f'  - ' + x.__str__().lstrip()
    return(rval)

  def __getitem__(self, item):
    return(self.__dict__[item])

  def __setitem__(self, item, val):
    self.__dict__[item] = val

  def __call__(self, column='data'):
    if column == 'data':
      return(self.data)
    else:
      return(self.data[column])

  def expand_data(self):
    # Expand ranges of members such as:
    # MODEL_r1-3i1p1f1 into MODEL_r1i1p1f1, MODEL_r2i1p1f1, MODEL_r3i1p1f1
    # preserving the same value for all members.
    modelmeanflag = dict()
    for key in self.data.index:
      try:
        model, member = key.split('_')
      except ValueError as e:
        print(f'Malformed model_run string: {key}\n{e}')
        break
      ripf = parse_ripf(member)
      for item in ripf:
        if '-' in ripf[item]:
          ini,end = tuple([int(x) for x in ripf[item].split('-')])
          for imem in range(ini,end+1):
            thisripf = ripf.copy()
            thisripf[item] = imem
            self.data.loc[model + '_r%(r)si%(i)sp%(p)sf%(f)s' % thisripf] = self.data.loc[key]
            modelmeanflag[model + '_r%(r)si%(i)sp%(p)sf%(f)s' % thisripf] = 1
          self.data.drop(index = key, inplace = True)
    self.is_ens_mean = self.data.iloc[:,0].copy()
    self.is_ens_mean.iloc[:] = False
    self.is_ens_mean = self.is_ens_mean | (pd.DataFrame.from_dict(modelmeanflag, orient='index', columns=['is_ens_mean']) != 1)
  
  def get_class_data(self):
    if self.has_classes():
      rval = self.data.copy()
      rval.iloc[:] = pd.cut(self.data.values.flat,
        self.classes[0]['limits'],
        labels=self.classes[0]['labels'],
        ordered = True # TODO: could be made False if 'colors' are passed (e.g. to have ['unplausible', 'medium','unplausible'])
      )
    elif self.metric.units == 'categorical':
      rval = self.data.copy()
    else:
      rval = self.data.copy()
      try:
        for icol in range(rval.shape[1]):
          rval.iloc[:,icol] = pd.qcut(rval.iloc[:,icol].values.flat,
            q=3, # terciles
            labels=[f'T{x}' for x in range(1,3+1)]
          )
      except ValueError:
        rval = self.data.copy()
    return(rval)

  def get_formatted_data(self):
    if 'ensmean' in self.data.columns:
      return(self.data.applymap(lambda x: '%.2f*' % x).where(
        self.is_ens_mean,
        other = self.data.applymap(lambda x: '%.2f' % x)
      ))
    else:
      return(self.data)

  def get_plausible_mask(self):
    if self.has_plausible_values():
      rval = (self.data <= self.plausible_values[0].max) & (self.data >= self.plausible_values[0].min)
    else:
      rval = ~self.data.isnull()
    return(rval)

  def get_plausible_values(self):
    if self.has_plausible_values():
      rval = pd.DataFrame.from_dict(
        dict(min=self.plausible_values[0].min, max=self.plausible_values[0].max),
        orient='index', columns=self.data.columns
      )
    else:
      rval = pd.DataFrame.from_dict(
        dict(min=self.data.values.min(), max=self.data.values.max()),
        orient='index', columns=self.data.columns
      )
    return(rval)

  def has_classes(self):
    return(hasattr(self, 'classes'))

  def has_period(self):
    return(hasattr(self, 'period'))

  def has_plausible_values(self):
    return(hasattr(self, 'plausible_values'))

  def has_reference(self):
    return(hasattr(self, 'reference'))

  def is_disabled(self):
    return(hasattr(self, 'disabled'))

  def plausible_values_default(self, which=0):
    if self.has_plausible_values():
      idx = which if type(which) is int else [x.source for x in self.plausible_values].index(which)
      return(self.plausible_values[which])

class SubKeys:

  def __init__(self, **subkeydict):
    self.__dict__.update(subkeydict)

  def __str__(self):
    rval = ''
    for item in self.__dict__.keys():
      if item == 'comment':
        rval += f'    {item}:\n{indent_text(self[item], 6)}\n'
      else:
        rval += f'    {item}: {self[item]}\n'
    return(rval)

  def __getitem__(self, item):
    return(self.__dict__[item])

def load_from_files(pattern, skip_disabled = False, skip_cause = '', resolve_doi = False):
  alldata = []
  for fname in glob.glob(pattern):
    with open(fname) as fp:
      entrylist = yaml.load(fp, Loader=yaml.FullLoader)
      for x in entrylist: x['file'] = fname
      alldata.extend(entrylist)
  if skip_disabled:
    rval = [MetricEntry(x, resolve_doi = resolve_doi) for x in alldata if not 'disabled' in x]
  elif skip_cause:
    rval = [MetricEntry(x, resolve_doi = resolve_doi) for x in alldata if not ('disabled' in x and x['disabled']['cause'] == skip_cause)]
  else:
    rval = [MetricEntry(x, resolve_doi = resolve_doi) for x in alldata]
  return(rval)

if __name__ == '__main__':
  resolve_doi = False
  allmetrics = load_from_files('CMIP6_studies/*.yaml', skip_cause = 'incomplete', resolve_doi = resolve_doi)
  for field in ['type', 'spatial_scope', 'temporal_scope', 'data_source']:
    values = sorted(set([x[field] for x in allmetrics if hasattr(x, field)]))
    print(f'Current {field}s:')
    [print(f'  - {x}') for x in values]
  for field,subfield in [('disabled','cause')]:
    values = sorted(set([x[field][subfield] for x in allmetrics if hasattr(x, field)]))
    print(f'Current {field}.{subfield}s:')
    [print(f'  - {x}') for x in values]
  if resolve_doi:
    print(set([x.reference for x in allmetrics if x.has_reference()]))
  print(allmetrics[6])
