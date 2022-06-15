#!/usr/bin/env python3
import datetime
from pyesgf.search import SearchConnection
import logging
import natsort as ns
import numpy as np
import pandas as pd
import re

loglevel = logging.INFO
logger = logging.getLogger('root')
logger.setLevel(loglevel)
loghandler = logging.StreamHandler()
loghandler.setFormatter(logging.Formatter('[%(asctime)s] %(message)s'))
logger.addHandler(loghandler)

scenarios = ['ssp119', 'ssp126', 'ssp245', 'ssp370', 'ssp585']
contexts = {
  '6hrLev' : {
    'project': 'CMIP6',
    'experiment_id': ['historical']+scenarios,
    'table_id': '6hrLev',
  },
  '3Dpl' : {
    'project': 'CMIP6',
    'experiment_id': ['historical']+scenarios,
    'variable_id': ['ua','va','ta','zg','hus','hur'],
    'table_id': 'day',
  },
  'LowerBoundaries' : {
    'project': 'CMIP6',
    'experiment_id': ['historical']+scenarios,
    'variable_id': ['tos','siconc','od550aer'],
  },
   'AerosolExtra' : {
    'project': 'CMIP6',
    'experiment_id': ['historical']+scenarios,
    'variable_id': [
      # P2 (different types of aerosols, strongly advised)
      'od550bb', 'od550bc', 'od550dust', 'od550no3',
      'od550oa', 'od550so4', 'od550ss', 'od550so4so',
      # P3 (in option)
      'aerasymbnd', 'aeroptbnd', 'aerssabnd'
    ],
  },
  'Basic' : {
    'project': 'CMIP6',
    'experiment_id': ['historical']+scenarios,
    'variable_id': ['tas','pr','psl','tasmax','tasmin'],
    'frequency': 'day',
  },
}
facets = (
  'project', 'activity', 'institution', 'model', 'experiment',
  'run', 'table', 'variable', 'grid', 'version'
)
tags = { # Values are python sets
  'RCM': {'hus-ml', 'ta-ml', 'ua-ml', 'va-ml', 'tos', 'siconc', 'od550aer'},
  '3Dml': {'hus-ml', 'ta-ml', 'ua-ml', 'va-ml'},
  'ESD': [
    {'hus', 'zg', 'ta', 'ua', 'va', 'psl', 'pr', 'tas', 'tasmax', 'tasmin'},
    {'hur', 'zg', 'ta', 'ua', 'va', 'psl', 'pr', 'tas', 'tasmax', 'tasmin'},
    ],
  'Basic': {'pr', 'tas'},
}

def aggfun(x):
  xset = set(x)
  for k in tags:
    if type(tags[k]) != type([]):
      alternative_sets = [tags[k]]
    else:
      alternative_sets = tags[k]
    for altset in alternative_sets:
      if altset.issubset(xset):
        return(k)
  return('-')

#
#   Load search results
#
conn = SearchConnection('http://esgf-data.dkrz.de/esg-search', distrib=True)
logging.getLogger('pyesgf.search.connection').setLevel(loglevel)
df = pd.DataFrame()
for context in contexts.keys():
  logger.info(f'Retrieving {context} variables ...')
  ctx = conn.new_context(**contexts[context])
  dids = [result.dataset_id for result in ctx.search(batch_size=1000, ignore_facet_check=True)]
  open('CMIP6_for_CORDEX__%s.txt' % context, 'w').writelines([did+'\n' for did in sorted(dids)])
  datanode_part = re.compile('\|.*$')
  dataset_ids = [datanode_part.sub('', did).split('.') for did in dids]
  df = df.append(pd.DataFrame(dataset_ids))

df.columns = facets
df['modelrun'] = df[['model','run']].apply(lambda x: '_'.join(x), axis = 1)
# Add ml and pl tags to distinguish model and pressure level variables
df[df[['table']]=='6hrLev'] = '-ml'
df[(df[['table']]!='-ml') & (df[['table']]!='-pl')] = ''
df['variable'] = df[['variable', 'table']].apply(lambda x: ''.join(x), axis = 1)
# Sort the runs naturally
df['nsrun'] = ns.natsort_key(df.run)
df.sort_values(by=['model','experiment','nsrun','variable'], inplace = True)
# Drop unnecessary columns
df.drop(
  ['project', 'activity', 'grid', 'version', 'table', 'nsrun'],
  axis = 'columns', inplace = True
)
# Disregard replicas and different versions and different tables (frequencies!)
df.drop_duplicates(inplace = True)
df.to_csv('df.csv', float_format = '%g', sep = ';', decimal = ',', index = False)

#
#   Variable availability table
#
# One-liner to tag variable availability by model run and experiment
varcount = df.groupby(['modelrun', 'experiment'])['variable'].agg(aggfun).unstack()
# Sort also this table by runs in a natural way
varcount['nsmodelrun'] = ns.natsort_key(varcount.index)
varcount.sort_values(by=['nsmodelrun'], inplace = True)
varcount.drop(['nsmodelrun'], axis = 'columns', inplace = True)
# Split model and run
varcount.index = varcount.index.str.split('_', expand = True)
# Add synthesis column (ssp126 and ssp370 available for dyn. downscaling)
varcount.insert(0, 'synthesis',
  np.multiply((varcount['ssp126'] == 'RCM') & (varcount['ssp370'] == 'RCM'),1)
)
#
#   CSV output
#
varcount.to_csv('docs/CMIP6_for_CORDEX_availability_ESGF.csv', float_format = '%g',
  index_label = ['model', 'run']
)
#
#   Time stamp
#
with open('LASTUPDATE', 'w') as fp:
  fp.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
