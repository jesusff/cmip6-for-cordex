import datetime
import pandas as pd
import seaborn as sns
import sys

plans = pd.read_csv('CMIP6_downscaling_plans.csv')

domains = sorted(list(set(plans.domain)))

f = open(f'CMIP6_downscaling_plans_tables.html','w')
f.write(f'''<!DOCTYPE html>
<html><head>
<style>
body {{ padding-bottom: 600px; }}
tr:hover {{background-color:#f5f5f5;}}
th, td {{text-align: center; padding: 3px;}}
table {{border-collapse: collapse;}}
span.planned {{color: red}}
span.running {{color: blue}}
span.completed {{color: black}}
span.published {{color: black; font-weight: bold}}
a {{color: DodgerBlue}}
a:link {{ text-decoration: none; }}
a:visited {{ text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
a:active {{ text-decoration: underline;}}
</style>
</head><body>
<h1> CORDEX-CMIP6 downscaling plans summary tables</h1>
<p style="text-align: right;">(Version: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")})</p>
<p style="text-align: justify;">
Simulation status according to CORDEX-CMIP6 downscaling plans reported by the groups and collected in <a href="https://github.com/jesusff/cmip6-for-cordex/blob/main/CMIP6_downscaling_plans.csv">CMIP6_downscaling_plans.csv</a>. Check that file for further details or to contribute/update simulations. Colours indicate status as:
<span class="planned">planned</span>
<span class="running">running</span>
<span class="completed">completed</span>
<span class="published">published</span>
<p style="text-align:left"> Domains: |
''')
[f.write(f'<a href="#{dom}">{dom}</a> | ') for dom in domains]
d1 = dict(selector=".level0", props=[('min-width', '150px')])
for domain in domains:
  dom_plans = plans[(plans.domain == domain) & (plans.experiment.isin(['historical','ssp119','ssp126','ssp245','ssp370','ssp585']))]
  dom_plans = dom_plans.assign(htmlstatus=pd.Series('<span class="' + dom_plans.status + '">' + dom_plans.experiment + '</span>', index=dom_plans.index))
  dom_plans = dom_plans.assign(model_id=pd.Series(dom_plans.institute + '-' + dom_plans.rcm_name, index=dom_plans.index))
  f.write(f'<h2 id="{domain}">{domain}</h2>')
  f.write(dom_plans.pivot_table(
    index = ('driving_model', 'ensemble'),
    columns = 'model_id',
    values = 'htmlstatus',
    aggfunc = lambda x: ' '.join(x.dropna())
  ).style
     .set_properties(**{'font-size':'8pt', 'border':'1px lightgrey solid !important'})
     .set_table_styles([d1,{
        'selector': 'th',
        'props': [('font-size', '8pt'),('border-style','solid'),('border-width','1px')]
      }])
     .render()
     .replace('nan','')
 )
f.write('</body></html>')
f.close()
