import xarray as xr
from pyprojroot import here

ds = xr.open_dataset(here() / 'zhongfeng/Eval_TC/Eval_TC/Mean_NW_Pacific_centered.nc')

ds['models'] = xr.Variable('case',[
  'ACCESS-CM2',
  'ACCESS-ESM1-5',
  'AWI-CM-1-1-MR',
  'BCC-CSM2-MR',
  'BCC-ESM1',
  'CAMS-CSM1-0',
  'CanESM5',
  'CESM2',
  'CESM2-FV2',
  'CESM2-WACCM',
  'CESM2-WACCM-FV2',
  'CIESM',
  'E3SM-1-0',
  'EC-Earth3',
  'FGOALS-g3',
  'FIO-ESM-2-0',
  'GISS-E2-1-G',
  'GISS-E2-1-H',
  'INM-CM4-8',
  'INM-CM5-0',
  'IPSL-CM6A-LR',
  'KACE-1-0-G',
  'MCM-UA-1-0',
  'MIROC6',
  'MPI-ESM-1-2-HAM',
  'MPI-ESM1-2-HR',
  'MPI-ESM1-2-LR',
  'MRI-ESM2-0',
  'NESM3',
  'NorCPM1',
  'NorESM2-LM',
  'NorESM2-MM',
  'SAM0-UNICON',
  'JRA55',
  'ERA5'
])

for m,val in zip(ds['models'].values, ds['MIEI'].values):
  print(f'    {m}_r1i1p1f1: {val:.3f}')
