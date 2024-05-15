import datetime
import natsort as ns
import numpy as np
import pandas as pd

rcm_source_types = ['ARCM', 'AORCM']

tableavail = pd.read_csv('docs/CMIP6_for_CORDEX_availability_ESGF.csv').set_index(['model', 'run'])
non_esgf = pd.read_csv('CMIP6_for_CORDEX_availability_non_ESGF.csv').set_index(['model', 'run'])
tableavail.update(non_esgf)
# - update synthesis column
mandatory_scenarios = ['historical','ssp126', 'ssp370']
tableavail.loc[:,'synthesis'] = np.logical_and.reduce(
  tableavail.loc[:,mandatory_scenarios].isin(rcm_source_types), axis=1
) * 1
tableavail.loc[:,'synthesis'] = tableavail.loc[:,'synthesis'].astype(int).replace(
  {0: '', 1: '1'}
)
# - filter out entries without 1 scenario
availscenarios = ['ssp126', 'ssp245', 'ssp370', 'ssp585']
tableavail_scen_filter = np.sum(tableavail.loc[:,availscenarios].isin(rcm_source_types), axis=1) >= 1
tableavail_hist_filter = tableavail.loc[:,'historical'].isin(rcm_source_types)
row_filter = set(
    tableavail.index[tableavail_scen_filter]
  ).intersection(
    tableavail.index[tableavail_hist_filter]
  )
tableavail = tableavail.loc[row_filter]
tableavail = tableavail.reindex(ns.natsorted(tableavail.index))

csvout = 'docs/CMIP6_for_CORDEX_availability_RCM.csv'
tableavail.to_csv(csvout, float_format = '%.2f', index_label = ['model', 'run'])

def greyout_non_rcm(df):
  attr = 'color: grey'
# Bug in pandas https://github.com/pandas-dev/pandas/issues/35429
#  return(df.where(df.isin(rcm_source_types), attr))
  rval = df.copy()
  rval.iloc[:] = np.where((rval.isin(rcm_source_types)|(rval == '1')).fillna(False), rval, attr)
  return(rval)

d1 = dict(selector=".level0", props=[('min-width', '50px')])
f = open(f'docs/CMIP6_for_CORDEX_availability_RCM.html','w')
f.write(f'''<!DOCTYPE html>
<html><head>
<style>
body {{ }}
tr:hover {{background-color:#f5f5f5;}}
th, td {{text-align: center; padding: 3px;}}
table {{border-collapse: collapse;}}
a {{color: DodgerBlue}}
a:link {{ text-decoration: none; }}
a:visited {{ text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
a:active {{ text-decoration: underline;}}
</style>
</head><body>
<h1> CMIP6 for CORDEX</h1>
<h2> Lateral boundary conditions availability for RCMs</h2>
<p style="font-size: smaller; text-align: right;">(Version: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")})</p>
<p style="font-size: smaller; text-align: justify;">
Summary of CMIP6 ScenarioMIP simulation availability.
Availability is labeled according to the variables and frequency available:
AORCM (monthly 3D sea potential temperature and salinity, 2D sea surface height, 6h 3D model level data, along with SST, sea ice and AOD),
ARCM (6h 3D model level data, along with SST, sea ice and AOD),
3Dml (6h 3D model level data),
ESD (6h specific or relative humidity, geopotential height, temperature and wind at pressure levels, and mean sea level pressure, precipitation, near-surface mean, minimum and maximum air temperature),
Basic (daily precipitation and mean near-surface air temperature).
A dash (-) indicates that the simulation exists in ESGF, but none of the conditions to get one of the previous labels applied.
Empty cells represent unavailable simulations (either at ESGF or the producing center).
The synthesis column indicates whether the CORDEX-CMIP6 protocol mandatory scenarios (SSP3-7.0 and SSP1-2.6) are available (1) or not (0).
The table shows only those simulations with RCM (ARCM or AORCM) LBC available for some future scenario (plus historical).
</p>
<p style="font-size: smaller; text-align: justify;">
See <a href="http://wcrp-cordex.github.io/cmip6-for-cordex">http://wrcp-cordex.github.io/cmip6-for-cordex</a> for details. A machine-readable (CSV) file version of this table is available <a href="https://github.com/wcrp-cordex/cmip6-for-cordex/blob/main/docs/CMIP6_for_CORDEX_availability_RCM.csv">here</a>.
</p>
''')
f.write(tableavail
    .convert_dtypes(convert_string = False, convert_boolean = False)
    .style
      .set_properties(**{'font-size':'8pt', 'border':'1px lightgrey solid !important'})
      .set_table_styles([d1,{
        'selector': 'th',
        'props': [('font-size', '8pt'),('border-style','solid'),('border-width','1px')]
      }])
      .apply(greyout_non_rcm, axis=None)
      .render()
      .replace('nan','')
  )
f.write('</body></html>')
f.close()
