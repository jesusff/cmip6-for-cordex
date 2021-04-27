import itertools
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn

varcount = pd.read_csv('CMIP6_summary_tags.csv')

rcm_bc_avail = varcount.iloc[:,4:] == 'RCM'
rcm_bc_avail_crosscount = rcm_bc_avail.T.dot(rcm_bc_avail*1)
fout = open('scenario_stats.txt', 'w')
print(rcm_bc_avail_crosscount, file=fout)
trinan = np.where(1-np.tril(np.ones([5,5])),np.nan, 0)
snplot = sn.heatmap(rcm_bc_avail_crosscount + trinan, annot = True, cmap='mako_r')
snplot.get_figure().savefig('scenario_stats.png')
# 3 scenario combination availability
for comb in itertools.combinations(rcm_bc_avail.columns, 3):
  mem_avail = rcm_bc_avail[list(comb)].sum(axis=1)==3
  models_avail = sorted(set(varcount['model'][mem_avail]))
  print(f'\n{comb}: {mem_avail.sum()} ({len(models_avail)} models)', file=fout)
  [print(f'  {x}', file=fout) for x in models_avail]
  print(varcount[["model","run"]][mem_avail].to_string(index=False), file=fout)
fout.close()

