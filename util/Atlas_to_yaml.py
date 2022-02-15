import glob
import pandas as pd
import yaml

var = 'tas'
longname = dict(
  pr = 'Precipitation relative delta change',
  tas = 'Near surface temperature delta change'
)
units = dict(pr='percent', tas='K')
dataset = dict(pr='pr_land', tas='tas_landsea')
basedir = f'/home/chus/zzgit/IPCC-WG1/Atlas/datasets-aggregated-regionally/data/CMIP6/CMIP6_{dataset[var]}'
scenarios = ['ssp585']
period_scen = slice('2071','2100')
period_hist = slice('1981','2010')
regions = ['MDG','SIO']
#seasons = ['DJF', 'MAM', 'JJA', 'SON', 'Annual']
seasons = ['Annual']
months = dict(DJF=[1,2,12], MAM=[3,4,5], JJA=[6,7,8], SON=[9,10,11], Annual=range(1,13))

def get_average(csv, period, region = 'world', season = 'Annual'):
  csvdata = pd.read_csv(csv, comment = '#')
  csvdata['date'] = pd.to_datetime(csvdata['date'], format='%Y-%m')
  rval = csvdata.set_index('date').loc[period,region]
  return(rval[rval.index.month.isin(months[season])].mean())
#
def get_run(filepath):
  return( filepath.split('_')[-1].split('.')[0] )

for season in seasons:
  for region in regions:
    # Compute delta changes for all CMIP6 models
    summary_tags = pd.read_csv('CMIP6_for_CORDEX_availability_ESGF.csv')
    deltas = dict()
    for model in set(summary_tags['model']):
      hist = glob.glob(f'{basedir}/CMIP6_{model}_historical_*.csv')
      if hist:
        val_ref = get_average(hist[0], period_hist, region, season)
      else:
        continue
      for scen in scenarios:
        modelruns = glob.glob(f'{basedir}/CMIP6_{model}_{scen}_*.csv')
        if modelruns:
          if var in ['pr']:
            delta = 100.*(get_average(modelruns[0], period_scen, region, season) - val_ref)/val_ref
          else:
            delta = get_average(modelruns[0], period_scen, region, season) - val_ref
          run = get_run(modelruns[0])
          deltas[(model,run,scen)] = delta
      del(val_ref)
    deltas_atlas = pd.Series(deltas).sort_index()
    # dump yaml
    yaml_header = f'''- key: Atlas D{var} {region} {season}
  doi: [Pers. Comm., Jesus Fernandez]
  metric:
    name: delta_{var}
    long_name: {longname[var]} {period_scen.start}-{period_scen.stop} w.r.t. {period_hist.start}-{period_hist.stop}
    units: {units[var]}
    variables: {var}
    comment: >
      Data derived from
      https://github.com/IPCC-WG1/Atlas/tree/devel/datasets-aggregated-regionally
      using the {dataset[var]} dataset.
  spatial_scope: {'Global' if region=='world' else region}
  temporal_scope: {season}
  period:
    reference: {period_hist. start}-{period_hist.stop}
    target: {period_scen.start}-{period_scen.stop}
  type: future_spread
  data_source: author_adapted
  data:'''
    print(yaml_header)
    for scen in scenarios:
      yamldata = deltas_atlas[deltas_atlas.index.get_level_values(2)==scen]
      yamldata.index = [ f'{x[0]}_{x[1]}' for x in yamldata.index.droplevel(2)]
      print(yaml.dump([[{scen: yamldata.to_dict()}]]).replace('- - ', '    '))

