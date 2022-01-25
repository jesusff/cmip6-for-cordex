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

facets = (
  'project', 'activity', 'institution', 'model', 'experiment', 'ensemble',
  'table', 'variable', 'grid', 'version'
)

df = pd.read_csv('../CMIP6_for_CORDEX__AerosolExtra.csv')
df.columns = facets

# Drop unnecessary columns
df.drop(
  ['project', 'activity', 'grid', 'table', 'version'],
  axis = 'columns', inplace = True
)
df.drop_duplicates(inplace = True)
df.sort_values(['institution', 'model', 'ensemble', 'experiment', 'variable'])

f = open(f'aerosol_species.html','w')
f.write(f'''<!DOCTYPE html>
<html><head>
<style>
body {{ }}
tr:hover {{background-color:#f5f5f5;}}
th, td {{text-align: center; padding: 3px;}}
table {{border-collapse: collapse;}}
span.planned {{color: #FF9999}}
span.running {{color: #009900}}
span.completed {{color: black; font-weight: bold}}
span.published {{color: #3399FF; font-weight: bold}}
a {{color: DodgerBlue}}
a:link {{ text-decoration: none; }}
a:visited {{ text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
a:active {{ text-decoration: underline;}}
</style>
</head><body>
<h1> CMIP6 ESGF Aerosol variables summary</h1>
<p style="text-align: right;">(Version: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")})</p>
<p style="text-align: justify;">
This refers to the availability of od550* variables (e.g. so4 is aod550so4)
''')
d1 = dict(selector=".level0", props=[('min-width', '100px')])
table = df.pivot_table(
  index = ('model', 'ensemble'),
  columns = 'experiment',
  values = 'variable',
  aggfunc = lambda x: ' '.join(x.dropna())
)
table = table.reindex(ns.natsorted(table.index))
f.write(table.style
   .set_properties(**{'font-size':'8pt', 'border':'1px lightgrey solid !important'})
   .set_table_styles([d1,{
      'selector': 'th',
      'props': [('font-size', '8pt'),('border-style','solid'),('border-width','1px')]
    }])
   .render()
   .replace('nan','')
   .replace('od550','')
)
f.write('</body></html>')
f.close()

table.to_csv('aerosol_species.csv', index_label = ['model', 'run'])

print('''- key: Aer. species
  doi: [pers. comm., Jesus Fernandez]
  metric:
    name: aer_species
    long_name: Aerosol species for which AOD available at ESGF
    units: categorical
    variables: od550bb, od550bc, od550dust, od550no3, od550oa, od550so4, od550ss, od550so4so, aerasymbnd, aeroptbnd, aerssabnd
    comment: >
      Data extracted from ESGF using 
      https://github.com/jesusff/cmip6-for-cordex/blob/main/util/aerosol_species.py
      which feeds from
      https://github.com/jesusff/cmip6-for-cordex/blob/main/CMIP6_for_CORDEX.py
    best: bb, bc, dust, no3, oa, so4, ss, so4so, aerasymbnd, aeroptbnd, aerssabnd
  type: other
  spatial_scope: special
  temporal_scope: Annual
  data_source: author
  data:''')
t370 = table.ssp370.dropna().reset_index()
for item in t370.iterrows():
  print('    %s_%s: %s' % (item[1][0], item[1][1], item[1][2].replace('od550','')))
