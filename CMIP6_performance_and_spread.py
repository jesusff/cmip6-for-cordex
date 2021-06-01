import glob
import numpy as np
import pandas as pd
import yaml

def synthesis(binvalues):
  return(np.logical_and.reduce(binvalues, 1)*1)

def split_index(df):
  return(pd.MultiIndex.from_tuples([idx.split('_') for idx in df.index]))

alldata = []
for fname in glob.glob('CMIP6_studies/*.yaml'):
  with open(fname) as fp:
    alldata.extend(yaml.load(fp, Loader=yaml.FullLoader))

perfdata = [x for x in alldata if x['type'] == 'performance']

# Metric values
table = pd.concat(
  [pd.DataFrame.from_dict(x['data'], orient='index', columns=[x['key']]) for x in perfdata],
  axis=1
).sort_index()
table.index = split_index(table)

# Plausible range
itemlist = []
for item in perfdata:
  if 'plausible_values' in item:
    values = item['plausible_values'][0] if type(item['plausible_values']) == type([]) else item['plausible_values']
    pditem = pd.DataFrame.from_dict(dict(min=values['min'], max=values['max']), orient='index', columns=[item['key']])
    itemlist.append(pditem)
tableprange = pd.concat(itemlist, axis=1)
tableprange.index = pd.MultiIndex.from_tuples([('. Plausible values', idx) for idx in tableprange.index])

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
tableclass.index = split_index(tableclass)

# Binary table
itemlist = []
for item in perfdata:
  pditem = pd.DataFrame.from_dict(item['data'], orient='index', columns=[item['key']])
  if 'plausible_values' in item:
    values = item['plausible_values'][0] if type(item['plausible_values']) == type([]) else item['plausible_values']
    pditem = np.logical_and(
      pditem <= values['max'],
      pditem >= values['min']
    ) * 1
  else:
    pditem = pditem*0+1 # all 1's (keep all, preserve not available models)
  itemlist.append(pditem)
tablebin = pd.concat(itemlist, axis=1).sort_index()
tablebin.index = split_index(tablebin)
# Add synthesis column
table.insert(0, column='Synthesis', value=synthesis(tablebin.values))
tableprange = pd.concat([tableprange, table])

# Spread data
spreaddata = [x for x in alldata if x['type'] == 'future_spread']
itemlist = []
for item in spreaddata:
  for scen in item['data'].keys():
    pditem = pd.DataFrame.from_dict(
      item['data'][scen],
      orient='index',
      columns=[f'{item["key"]} {scen}']
    )
    itemlist.append(pditem)
tablespread = pd.concat(itemlist, axis=1).sort_index()
tablespread.index = split_index(tablespread)
tablespread.to_csv('CMIP6_spread.csv', float_format = '%.2f',
  index_label = ['model','run']
)

# Independence criteria
indepdata = [x for x in alldata if x['type'] == 'independence']
itemlist = []
for item in indepdata:
  pditem = pd.DataFrame.from_dict(
    item['data'],
    orient='index',
    columns=[item['key']]
  )
  itemlist.append(pditem)
tableindep = pd.concat(itemlist, axis=1).sort_index()
tableindep.index = split_index(tableindep)
tableindep.to_csv('CMIP6_indep.csv', index_label = ['model', 'run'])

# All together
tablefull = pd.concat([tableprange,tablespread, tableindep], axis=1)
tablefull.to_csv(
  'CMIP6_perfspread.csv', float_format = '%.2f', index_label = ['model', 'run']
)
