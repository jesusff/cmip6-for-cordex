import glob
import numpy as np
import pandas as pd
import yaml

alldata = []
for fname in glob.glob('yaml/*.yaml'):
  with open(fname) as fp:
    alldata.extend(yaml.load(fp, Loader=yaml.FullLoader))

perfdata = [x for x in alldata if x['metric_scope'] == 'performance']

# Metric values
table = pd.concat(
  [pd.DataFrame.from_dict(x['data'], orient='index', columns=[x['key']]) for x in perfdata],
  axis=1
).sort_index()
table.to_csv('CMIP6_performance.csv', float_format = '%g',
  index_label = ['model_run']
)

# Classes table (where available)
itemlist = []
for item in perfdata:
  pditem = pd.DataFrame.from_dict(item['data'], orient='index', columns=[item['key']])
  if 'classes' in item:
    pditem[item['key']] = pd.cut(
      pditem.values.flat,
      item['classes']['limits'],
      labels=item['classes']['labels']
    )
  itemlist.append(pditem)
tableclass = pd.concat(itemlist, axis=1).sort_index()
tableclass

# Binary table
itemlist = []
for item in perfdata:
  pditem = pd.DataFrame.from_dict(item['data'], orient='index', columns=[item['key']])
  if 'plausible_values' in item:
    pditem = np.logical_and(
      pditem <= item['plausible_values']['max'],
      pditem >= item['plausible_values']['min']
    ) * 1
  else:
    pditem = pditem*0+1 # all 1's (keep all, preserve not available models)
  itemlist.append(pditem)
tablebin = pd.concat(itemlist, axis=1).sort_index()
# Add synthesis column
tablebin.insert(0, column='Synthesis', value=np.logical_and.reduce(tablebin.values, 1)*1)
tablebin.to_csv('CMIP6_performance_binary.csv', float_format = '%g',
  index_label = ['model_run']
)

# Spread data
scenarios = ['ssp126','ssp245','ssp370','ssp585']
spreaddata = [x for x in alldata if x['metric_scope'] == 'future_spread']
itemlist = []
for item in spreaddata:
  for scen in scenarios:
    if scen in item['data']:
      pditem = pd.DataFrame.from_dict(
        item['data'][scen],
        orient='index',
        columns=[f'{item["key"]}-{scen}']
      )
      itemlist.append(pditem)
tablespread = pd.concat(itemlist, axis=1).sort_index()
tablespread.to_csv('CMIP6_spread.csv', float_format = '%.2f',
  index_label = ['model_run']
)

pd.concat([table,tablespread], axis=1).sort_index().to_csv(
  'CMIP6_perfspread.csv', float_format = '%.2f', index_label = ['model_run']
)
