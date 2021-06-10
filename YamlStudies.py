import glob
import natsort as ns
import numpy as np
import pandas as pd
import re
import yaml

def synthesis(binvalues):
  return(np.logical_and.reduce(binvalues, 1)*1)

def split_index(df):
  return(pd.MultiIndex.from_tuples([idx.split('_') for idx in df.index], names=['model','run']))

def parse_ripf(str):
  p = re.compile(r'r(?P<r>[0-9-]+)i(?P<i>[0-9-]+)p(?P<p>[0-9-]+)f(?P<f>[0-9-]+)')
  m = p.match(str)
  return(m.groupdict() if m else [])

class MetricEntry:

  def __init__(self, yamlentry):
    self.__dict__.update(yamlentry)
    # print(f'instantiating {self.key} ...')
    self.metric = Metric(**self.metric)
    self.period = Period(**self.period)
    if self.has_plausible_values():
      if type(self.plausible_values) is list:
        self.plausible_values = [Plausible(**x) for x in self.plausible_values]
      else:
        self.plausible_values = [Plausible(**self.plausible_values)]
    if type(list(self.data.values())[0]) is dict:
      self.data = pd.DataFrame.from_dict(self.data, orient='columns') 
      self.data.columns = [f'{self.key} {x}' for x in self.data.columns]
    else:
      self.data = pd.DataFrame.from_dict(self.data, orient='index', columns=[self.key])
    self.expand_data()
    self.data = self.data.reindex(ns.natsorted(self.data.index))
    self.data.index = split_index(self.data)

  def __str__(self):
    rval = f'- {self.key}\n'
    rval += self.metric.__str__() + '\n' + self.period.__str__() + '\n'
    if self.has_plausible_values():
      for x in self.plausible_values:
        rval += str(x)
    rval += '\n'
    return(rval)

  def __getitem__(self, item):
    return(self.__dict__[item])

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
        self.classes['limits'],
        labels=self.classes['labels']
      )
    else:
      rval = self.data
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

  def has_plausible_values(self):
    return(hasattr(self, 'plausible_values'))

  def is_disabled(self):
    return(hasattr(self, 'disabled'))

  def plausible_values_default(self, which=0):
    if self.has_plausible_values():
      idx = which if type(which) is int else [x.source for x in self.plausible_values].index(which)
      return(self.plausible_values[which])

class Period:

  def __init__(self, **period_dict):
    self.__dict__.update(period_dict)

  def __str__(self):     
    if hasattr(self, 'target'):
      return(f'Period: {self.target} w.r.t. {self.reference}')
    else:
      return(f'Period: {self.reference}')

class Plausible:

  def __init__(self, **plausible_dict):
    self.__dict__.update(plausible_dict)

  def __str__(self):     
    rval = f'  - Plausible range: [{self.min}, {self.max}] | source: {self.source}\n'
    if hasattr(self, 'comment'):
      rval += '      ' + self.comment
    return(rval)

class Metric:

  def __init__(self, **metric_dict):
    self.__dict__.update(metric_dict)

  def __str__(self):
    rval = f'{self.name} - {self.long_name} [{self.units}]\n'
    if hasattr(self, 'comment'):
      rval += f'{self.comment}'
    rval += f'Variables: {self.variables}'
    if hasattr(self, 'best'):
      rval += f'\nBest score: {self.best} worst: {self.worst}'
    return(rval)

  def repr(self):
    return(f'{self.__class__} instance\n\n{self.__str()}')

def load_from_files(pattern, skip_disabled = False, skip_cause = ''):
  alldata = []
  for fname in glob.glob(pattern):
    with open(fname) as fp:
      alldata.extend(yaml.load(fp, Loader=yaml.FullLoader))
  if skip_disabled:
    rval = [MetricEntry(x) for x in alldata if not 'disabled' in x]
  elif skip_cause:
    rval = [MetricEntry(x) for x in alldata if not ('disabled' in x and x['disabled']['cause'] == skip_cause)]
  else:
    rval = [MetricEntry(x) for x in alldata]
  return(rval)

if __name__ == '__main__':
  allmetrics = load_from_files('CMIP6_studies/*.yaml', skip_cause = 'incomplete')
  for field in ['type', 'spatial_scope', 'temporal_scope', 'data_source']:
    values = sorted(set([x[field] for x in allmetrics if hasattr(x, field)]))
    print(f'Current {field}s:')
    [print(f'  - {x}') for x in values]
  for field,subfield in [('disabled','cause')]:
    values = sorted(set([x[field][subfield] for x in allmetrics if hasattr(x, field)]))
    print(f'Current {field}.{subfield}s:')
    [print(f'  - {x}') for x in values]
