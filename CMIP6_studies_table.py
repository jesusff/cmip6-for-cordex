import natsort as ns
import numpy as np
import pandas as pd
import YamlStudies as ys
import yaml

def synthesis(binvalues):
  return(np.logical_and.reduce(binvalues, 1)*1)

with open('CMIP6_studies_config.yaml') as fp:
  config = yaml.load(fp, Loader=yaml.FullLoader)

alldata = ys.load_from_files('CMIP6_studies/*.yaml', skip_disabled = False, skip_cause = 'incomplete')
# filter and sort
CORDEX_DOMAIN = 'EUR'
alldata = [x for x in alldata if x.spatial_scope in config['spatial_scope_filter'][CORDEX_DOMAIN]]
alldata.sort(key=lambda x: config['spatial_scope_filter'][CORDEX_DOMAIN].index(x.spatial_scope))

# Performance
tableperf = pd.concat([x.get_formatted_data() for x in alldata if x.type=='performance'], axis=1)

# Plausible range rows
tableprange= pd.concat(
  [x.get_plausible_values() for x in alldata if x.type in ('performance')],
  axis=1
)
tableprange.index = pd.MultiIndex.from_tuples(
  [('. Plausible values', idx) for idx in tableprange.index],
  names = ['model','run']
)

# Classes table (when available)
tableclass = pd.concat([x.get_class_data() for x in alldata], axis=1)
tableclass = tableclass.reindex(ns.natsorted(tableclass.index))

# Binary table
tablebin = pd.concat([x.get_plausible_mask() for x in alldata if x.type=='performance'], axis=1) * 1
# Add synthesis column
tableperf.insert(0, column='Synthesis', value=synthesis(tablebin.values))
tableprange = pd.concat([tableprange, tableperf])
# sort synthesis column first
synthfirst = list(tableprange.columns)
synthfirst.insert(0, synthfirst.pop(synthfirst.index('Synthesis')))
tableprange = tableprange.reindex(synthfirst, axis=1)

# Spread
tablespread = pd.concat(
  [x.get_formatted_data() for x in alldata if x.type=='future_spread'],
  axis=1
)

# Independence
tableindep = pd.concat(
  [x.data for x in alldata if x.type=='independence'],
  axis=1
)

# Availability
tableavail = pd.read_csv('CMIP6_for_CORDEX_Summary.csv').set_index(['model', 'run'])
non_esgf = pd.read_csv('CMIP6_for_CORDEX_availability_non_ESGF.csv').set_index(['model', 'run'])
tableavail.update(non_esgf)
# - update synthesis column
availscenarios = ['ssp126', 'ssp245', 'ssp370', 'ssp585']
tableavail.loc[:,'synthesis'] = np.logical_and.reduce(
  tableavail.loc[:,availscenarios] == 'RCM', axis=1
) * 1
# - filter out entries with less than 2 scenarios unless a metric is available for it
tableavail_row_filter = np.sum(tableavail.loc[:,availscenarios] == 'RCM', axis=1) >= 2
row_filter = set(tableavail.index[tableavail_row_filter]).union(
  tableprange.index,
  tablespread.index,
  tableindep.index
).intersection(tableavail.index)
tableavail = tableavail.loc[row_filter]

# All together
tablefull = pd.concat(
  [tableavail, tableprange,tablespread, tableindep], axis=1, 
  keys=['availability', 'performance', 'spread', 'independence']
)
tablefull = tablefull.reindex(ns.natsorted(tablefull.index))
# Dump final CSV
tablefull.to_csv(
  'CMIP6_studies_table.csv', float_format = '%.2f', index_label = ['model', 'run']
)

# Some fixes for Google Spreadsheet
fp = open('CMIP6_studies_table.csv', 'r')
lines = fp.readlines()
fp.close()
lines[1] = lines[1].replace(',,','model,run,')
fp = open('CMIP6_studies_table.csv', 'w')
fp.writelines([lines[0]]+lines[3:5]+[lines[1]]+lines[5:])
fp.close()
