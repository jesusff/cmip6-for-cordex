import pandas as pd
import YamlStudies as ys

entries = ys.load_from_files('CMIP6_studies/Pri20.yaml')
max_score = pd.concat([entries[0].data, entries[1].data], axis=1).max(axis=1)

for item in max_score.iteritems():
  print('    %s_%s: '% item[0] + '%d' % item[1])
