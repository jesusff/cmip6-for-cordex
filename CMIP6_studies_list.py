import glob
import YamlStudies as ys
import yaml
import sys

CORDEX_DOMAIN = sys.argv[1]

with open('CMIP6_studies_config.yaml') as fp:
  config = yaml.load(fp, Loader=yaml.FullLoader)

alldata = []
for fname in glob.glob('CMIP6_studies/*.yaml'):
  with open(fname) as fp:
    entrylist = yaml.load(fp, Loader=yaml.FullLoader)
    for x in entrylist:
      x['file'] = fname
    alldata.extend(entrylist)
alldata = [x for x in alldata if x['spatial_scope'] in config['spatial_scope_filter'][CORDEX_DOMAIN]]

def is_incomplete(dic):
  try:
    return(dic['disabled']['cause'] == 'incomplete')
  except:
    return(False)

print(f'## Incomplete entries\n')
for x in alldata:
  if is_incomplete(x):
    print(f' * [{x["key"]}]({x["file"]})')

print(f'## Disabled entries\n')
preferred = {}
for x in alldata:
  if 'disabled' in x:
    print(f' · [{x["key"]}]({x["file"]})')
    if x['disabled']['cause'] == 'preferred_source' and x['disabled']['preferred']:
      preferred.setdefault(x['disabled']['preferred'], []).append(x['key'])

enabled_data = ys.load_from_files('CMIP6_studies/*.yaml', resolve_doi = True, skip_disabled = True)
# filter and sort
enabled_data = [x for x in enabled_data if x.spatial_scope in config['spatial_scope_filter'][CORDEX_DOMAIN]]
enabled_data.sort(key=lambda x: config['spatial_scope_filter'][CORDEX_DOMAIN].index(x.spatial_scope))

typenames = dict(
  performance = 'Plausibility',
  future_spread = 'Spread of future outcomes',
  other = 'Other criteria'
)
print(f'## Available entries ({CORDEX_DOMAIN} scope)')
for t in typenames:
  print(f'### {typenames[t]}')
  for x in enabled_data:
    if x.type == t:
      print(f'#### {x.key}\n')
      print(f'Located in [{x.file}]({x.file})\n')
      if x.key in preferred:
        pref_list = []
        for item in preferred[x.key]:
          pref_list.extend([x['file'] for x in alldata if x['key']==item])
        print(f'Preferred to ', end='')
        [print(f'[{y}]({y})') for y in pref_list]
        print()
      print(f'{x.reference}\n')
      print(f'```\n{x.__str__()}\n```\n')
