# Dirty stuff to add row tooltips
import re
import sys

domain = sys.argv[1]

def get_value(str):
  p = re.compile(r'.*\>(.*)\<.*')
  m = p.match(str)
  return(m.group(1) if m else [])

with open(f'CMIP6_studies_table_{domain}.html','r') as f:
  fulltext = f.readlines()

model = ''
for i,line in enumerate(fulltext):
  if line == '            <tr>\n':
    if 'row_heading level0' in fulltext[i+1]:
      model = get_value(fulltext[i+1])
      run = get_value(fulltext[i+2])
    elif 'row_heading level1' in fulltext[i+1]:
      run = get_value(fulltext[i+1])
    else:
      continue
    if run.startswith('r'):
      fulltext[i] = f'            <tr title="{model} {run}">\n'

with open(f'CMIP6_studies_table_{domain}.html','w') as f:
  f.writelines(fulltext)

