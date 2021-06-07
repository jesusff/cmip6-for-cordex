import natsort as ns
import numpy as np
import pandas as pd
import re
import YamlStudies as ys
import importlib

importlib.reload(ys)
alldata = ys.load_from_files('CMIP6_studies/*.yaml', skip_disabled = False)
[x.data for x in alldata]

perfdata = [x for x in alldata if x.type == 'performance']

for x in perfdata: expand_data(x)

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
tableprange.index = pd.MultiIndex.from_tuples(
  [('. Plausible values', idx) for idx in tableprange.index],
  names = ['model','run']
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

# sort synthesis column first
synthfirst = list(tableprange.columns)
synthfirst.insert(0, synthfirst.pop(synthfirst.index('Synthesis')))
tableprange = tableprange.reindex(synthfirst, axis=1)

#
# All together
#
tablefull = pd.concat([tableprange,tablespread, tableindep], axis=1, keys=['performance', 'spread', 'independence'])
# sort rows naturally (ascending member numbering)
tablefull['nsrun'] = ns.natsort_key(tablefull.index.get_level_values(1))
tablefull.sort_values(by=['model','nsrun'], inplace = True)
tablefull.drop(columns='nsrun', inplace = True)
# Dump final CSV
tablefull.to_csv(
  'CMIP6_perfspread.csv', float_format = '%.2f', index_label = ['model', 'run']
)
