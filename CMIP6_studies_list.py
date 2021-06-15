import glob
import YamlStudies as ys
import yaml

CORDEX_DOMAIN = 'EUR'

print(f'## Incomplete entries\n')
alldata = []
for fname in glob.glob('CMIP6_studies/*.yaml'):
  with open(fname) as fp:
    entrylist = yaml.load(fp, Loader=yaml.FullLoader)
    for x in entrylist:
      x['file'] = fname
    alldata.extend(entrylist)

def is_incomplete(dic):
  try:
    return(dic['disabled']['cause'] == 'incomplete')
  except:
    return(False)

for x in alldata:
  if is_incomplete(x):
    print(f' * [{x["key"]}]({x["file"]})')

with open('CMIP6_studies_config.yaml') as fp:
  config = yaml.load(fp, Loader=yaml.FullLoader)

alldata = ys.load_from_files('CMIP6_studies/*.yaml', resolve_doi = True, skip_cause = 'incomplete')
# filter and sort
alldata = [x for x in alldata if x.spatial_scope in config['spatial_scope_filter'][CORDEX_DOMAIN]]
alldata.sort(key=lambda x: config['spatial_scope_filter'][CORDEX_DOMAIN].index(x.spatial_scope))

print(f'## Available entries ({CORDEX_DOMAIN} scope)')
for x in alldata:
  print(f'### {x.key}\n')
  print(f'Located in [{x.file}]({x.file})\n')
  print(f'{x.reference}\n')
  print(f'```\n{x.__str__()}\n```\n')
