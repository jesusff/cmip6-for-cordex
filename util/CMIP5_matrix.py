import datetime
import pandas as pd

collapse_institutions = True

url = 'https://raw.githubusercontent.com/euro-cordex/esgf-table/master/euro-cordex-esgf.csv'
plans = pd.read_csv(url, na_filter=False)
domains = sorted(list(set(plans.domain)))
plans = plans.assign(status='published') # This file contains only ESGF published data
plans.drop_duplicates(subset=['institute', 'driving_model_id', 'experiment_id', 'member', 'model_id',], inplace=True)

f = open(f'CMIP5_matrix.html','w')
f.write(f'''<!DOCTYPE html>
<html><head>
<style>
body {{ padding-bottom: 600px; }}
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
<h1> CORDEX-CMIP5 ESGF summary tables</h1>
<p style="text-align: right;">(Version: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")})</p>
<p style="text-align: justify;">
Currently only from EURO-CORDEX EUR-11 ...
<p style="text-align:left"> Source: <a href="{url}">{url}</a>
<p style="text-align:left"> Domains: |
''')
[f.write(f'<a href="#{dom}">{dom}</a> | ') for dom in domains]
d1 = dict(selector=".level0", props=[('min-width', '150px')])
for domain in domains:
  dom_plans = plans[plans.domain == domain]
  dom_plans = dom_plans.assign(htmlstatus=pd.Series('<span class="' + dom_plans.status + '">' + dom_plans.experiment_id + '</span>', index=dom_plans.index))
  dom_plans = dom_plans.assign(model_id=pd.Series(dom_plans.institute + '-' + dom_plans.model_id, index=dom_plans.index))
  column_id = 'model_id' if collapse_institutions else 'model_id'
  dom_plans_matrix = dom_plans.pivot_table(
    index = ('driving_model_id', 'member'),
    columns = column_id,
    values = 'htmlstatus',
    aggfunc = lambda x: ' '.join(x.dropna())
  )
  dom_plans_matrix.drop('ECMWF-ERAINT', level=0, axis=0, inplace=True)
  f.write(f'''<h2 id="{domain}">{domain}</h2>
    <p style="font-size: smaller;"> Colour legend:
      <span class="planned">planned</span>
      <span class="running">running</span>
      <span class="completed">completed</span>
      <span class="published">published</span>
    </p>
  ''')
  f.write(dom_plans_matrix.style
     .set_properties(**{'font-size':'8pt', 'border':'1px lightgrey solid !important'})
     .set_table_styles([d1,{
        'selector': 'th',
        'props': [('font-size', '8pt'),('border-style','solid'),('border-width','1px')]
      }])
     .render()
     .replace('nan','')
     .replace('historical','hist')
 )
f.write('</body></html>')
f.close()
