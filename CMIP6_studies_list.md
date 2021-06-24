## Incomplete entries

 * [Beo21](CMIP6_studies/Beo21.yaml)
## Disabled entries

 · [Atlas Dtas NEU DJF](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dtas WCE DJF](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dtas MED DJF](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dtas world DJF](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dtas WCE JJA](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dtas MED JJA](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dtas world JJA](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dpr NEU DJF](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dpr WCE DJF](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dpr MED DJF](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dpr world DJF](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dpr NEU JJA](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dpr WCE JJA](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dpr MED JJA](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dpr world JJA](CMIP6_studies/AtlasIPCC.yaml)
 · [Beo21](CMIP6_studies/Beo21.yaml)
## Available entries (EUR scope)
### Performance
#### Rib21 Constrained TCR

Located in [CMIP6_studies/Rib21.yaml](CMIP6_studies/Rib21.yaml)

Aur\'elien Ribes et al. (2021) Making climate projections conditional on historical observations, https://doi.org/10.1126%2Fsciadv.abc0671

```
- key: Rib21 Constrained TCR
  doi: 10.1126/sciadv.abc0671
  type: performance
  spatial_scope: Global
  temporal_scope: Annual
  data_source: reference
  metric:
    name: TCR
    long_name: Transient Climate Response
    units: K
    variables: tas
    comment:
      TCR is calculated from the CO2-only simulation, where the atmospheric CO2
      concentration increases at a rate of 1% per year, centered on the time of
      doubling of the atmospheric CO2, which occurs during simulation year 70
      (we use the mean of the years 61 to 80). The values of the GCM TCR  can be
      found in Suppl. Mat Table S1. Some model TCR are missing. This study is
      based on multi-member for each model, not on only one member.
  period:
    reference: 1850-2019
    comment:
      This is not the period for the metric values (these are model years at the
      time of doubling CO2), but the one used in the observational constraint.
  plausible_values:
  - min: 1.33
    max: 2.36
    source: reference
    comment:
      This is a 90% likely range (5-95%) for the TCR. HadCRUT4-CW (Cowtan & Way,
      2014) used as observational reference.

```

#### Tok20 Constrained TCR

Located in [CMIP6_studies/Tok20.yaml](CMIP6_studies/Tok20.yaml)

Katarzyna B. Tokarska et al. (2020) Past warming trend constrains future warming in CMIP6 models, https://doi.org/10.1126%2Fsciadv.aaz9549

```
- key: Tok20 Constrained TCR
  doi: 10.1126/sciadv.aaz9549
  type: performance
  spatial_scope: Global
  temporal_scope: Annual
  data_source: reference
  metric:
    name: TCR
    long_name: Transient Climate Response
    units: K
    variables: tas
    comment:
      TCR is calculated from the CO2-only simulation, where the atmospheric CO2
      concentration increases at a rate of 1% per year, centered on the time of
      doubling of the atmospheric CO2, which occurs during simulation year 70
      (we use the mean of the years 61 to 80). The values of the GCM TCR  can be
      found in Suppl. Mat Table S1. Some model TCR are missing. This study is
      based on multi-member for each model, not on only one member. https://adva
      nces.sciencemag.org/content/advances/suppl/2020/03/16/6.12.eaaz9549.DC1/aa
      z9549_SM.pdf
  period:
    reference: 1981-2014
    comment:
      This is not the period for the metric values (these are model years at the
      time of doubling CO2), but the one used in the observational constraint.
  plausible_values:
  - min: 0.9
    max: 2.27
    source: reference
    comment:
      Constrained TCR using 1981-2014 temperature past trends, 90% likely range
      (5-95%) for the TCR. See Table S3. On this Table there are also TCR ranges
      based on 1981-2017. This period was selected because it leads to a wider,
      more conservative plausible range.

```

#### Bru20 perf

Located in [CMIP6_studies/Bru20.yaml](CMIP6_studies/Bru20.yaml)

Lukas Brunner et al. (2020) Reduced global warming from CMIP6 projections when weighting models by performance and independence, https://doi.org/10.5194%2Fesd-11-995-2020

```
- key: Bru20 perf
  doi: 10.5194/esd-11-995-2020
  type: performance
  spatial_scope: Global
  data_source: reference
  metric:
    name: perf
    long_name: None
    units: None
    variables: None
    comment:
      Evaluation of the model using global criteria (past trends + spatial
      pattern) and independence criteria. Model with perfromance scores below
      0.006 are considered as irrealistic. This study is based on multi-member
      for each model, not on only one member.
  period:
    reference: None
  plausible_values:
  - min: 0.006
    max: 0.2
    source: reference

```

#### Qas21 Constrained Dtas ssp245

Located in [CMIP6_studies/Qasmi.yaml](CMIP6_studies/Qasmi.yaml)

None

```
- key: Qas21 Constrained Dtas ssp245
  doi: None
  type: performance
  spatial_scope: Global
  temporal_scope: Annual
  data_source: author
  metric:
    name: TCRbin
    long_name: Transient Climate Response
    units: binary
    variables: tas
    comment:
      Constrained global annual temperature future climate change range,
      2041-2060 vs 1850-1900, SSP245 (adapted from Ribes et al. 2021 by S.
      Qasmi)
  period:
    reference: 1850-1900
    target: 2041-2060
  plausible_values:
  - min: 1
    max: 1
    source: author

```

#### Can20 marle

Located in [CMIP6_studies/Can20.yaml](CMIP6_studies/Can20.yaml)

Alex J Cannon (2020) Reductions in daily continental-scale atmospheric circulation biases between generations of global climate models: CMIP5 to CMIP6, https://doi.org/10.1088%2F1748-9326%2Fab7e4f

```
- key: Can20 marle
  doi: 10.1088/1748-9326/ab7e4f
  type: performance
  spatial_scope: EUR
  temporal_scope: ONDJFM+AMJJAS
  data_source: reference_extracted_from_plot
  metric:
    name: marle
    long_name: Median absolute run length error
    units: rank
    variables: psl
    comment:
      Evaluation of automatic classification of weather types in 6 regions
      including Europe. This metric is the rank of CMIP6 models according to
      Median absolute run length error (MARLE; Figure 3) classified by MRT using
      JRA55 as reference. Ranks vary wildly depending on classification method
      and reference reanalysis. Ranks according to frecuency errors are also
      available.
    best: 1
    worst: 27
  period:
    reference: 1960-2004

```

#### Oud20 jetpos

Located in [CMIP6_studies/Oud20.yaml](CMIP6_studies/Oud20.yaml)

Thomas Oudar et al. (2020) Drivers of the Northern Extratropical Eddy-Driven Jet Change in CMIP5 and CMIP6 Models, https://doi.org/10.1029%2F2019gl086695

```
- key: Oud20 jetpos
  doi: 10.1029/2019GL086695
  type: performance
  spatial_scope: EUR
  temporal_scope: ONDJFM
  data_source: author
  metric:
    name: jetpos
    long_name: Jet Stream North-South relative position
    units: degrees_north
    variables: ua850
    comment:
      Jet position bias against ERA5 in the Central Atlantic region. Note that
      the bias is estimated by subtracting the ONDJFM mean eddy-driven jet
      position over the period 1979-2018 in ERA5 to each model mean eddy-driven
      jet position over the same period.
    best: 0
    worst: [90, -90]
  period:
    reference: 1979-2018
  plausible_values:
  - min: -4
    max: 4
    source: eurocordex_gcm_selection_team
    comment:
      Decided on meeting 2021-06-25 to enlarge the strict range provided in the
      reference. Just a mock up to illustrate this comment and the possibility
      to have plausible values from different sources. We can decide e.g. that
      the one applied by default is the first in the list. Or we can always
      check how it looks if we apply any priority to the sources.
  - min: -3
    max: 3
    source: reference

```

#### Bra21 Lamb EUR

Located in [CMIP6_studies/Bra21.yaml](CMIP6_studies/Bra21.yaml)

Swen Brands et al. (2021) A circulation-based performance atlas of the CMIP5 and 6 models, https://doi.org/10.5194%2Fgmd-2020-418

```
- key: Bra21 Lamb EUR
  doi: 10.5194/gmd-2020-418
  type: performance
  spatial_scope: EUR
  temporal_scope: Annual
  data_source: reference
  metric:
    name: lwtmae
    long_name: MAE of 27 Lamb Weather Type relative frequencies
    units: percent
    variables: psl
    comment:
      Mean absolute error (MAE) of the simulated vs. quasi-observed (reanalysis)
      relative frequencies for the 27 Lamb Weather Types representing recurrent
      regional atmospheric circulation patterns. The MAE was calculated
      separately for each grid box of a regular 2.5 deg lat-lon mesh extending
      from 22.5W to 42.5E and 30N to 70N. The spatial median MAE is provided
      here. Reference dataset to compute the metric is ERA-Interim. As
      reference, the value for the JRA-55 reanalysis (EUR) is 0.0956
    best: 0
    worst: 100
  period:
    reference: 1979-2005
  plausible_values:
  - min: 0
    max: 5
    source: reference
    comment:
      The range of plausible values is directly obtained from doi:
      10.5194/gmd-2020-418, the maximum MAE obtained there is here rounded to
      the next integer.

```

#### P. Nabat EUR AOD

Located in [CMIP6_studies/Nabat.yaml](CMIP6_studies/Nabat.yaml)

['pers_comm', 'Pierre Nabat']

```
- key: P. Nabat EUR AOD
  doi: ['pers_comm', 'Pierre Nabat']
  type: performance
  spatial_scope: EUR
  temporal_scope: Annual
  data_source: author
  metric:
    name: aod_rmse_bin
    long_name: plausibillity of RMSE of the Aerosol Optical Depth
    units: binary
    variables: aod550
    comment:
      Numerical values of the RMSE over Europe can be provided later. Only the
      GISS models are eliminated on this criteria (RMSE>0.7 whereas all other
      GCMs are below 0.2)  TO-DO Reference data set and period?
    best: 1
    worst: 0
  plausible_values:
  - min: 1
    max: 1
    source: author

```

#### F. Sevault MED SST

Located in [CMIP6_studies/Sevault.yaml](CMIP6_studies/Sevault.yaml)

['pers_comm', 'F. Sevault']

```
- key: F. Sevault MED SST
  doi: ['pers_comm', 'F. Sevault']
  type: performance
  spatial_scope: MED
  temporal_scope: Annual
  data_source: author
  metric:
    name: sst_rmse
    long_name: Sea surface temperature RMSE
    units: K
    variables: sst
    comment:
      TO-DO what is the reference data set and period?
    best: 0
    worst: inf
  plausible_values:
  - min: 0
    max: 2
    source: author

```

#### Dobler SICE rmse NAtl

Located in [CMIP6_studies/Dobler.yaml](CMIP6_studies/Dobler.yaml)

['pers. comm.', 'A. Dobler']

```
- key: Dobler SICE rmse NAtl
  doi: ['pers. comm.', 'A. Dobler']
  type: performance
  spatial_scope: NAtl
  temporal_scope: Annual
  data_source: author
  metric:
    name: siconcrmse
    long_name: Sea Ice RMSE w.r.t. HadICE
    units: percent
    variables: siconc
    comment:
      Root mean squared error of the annual mean sea ice concentration as
      compared to the HadICE data set. https://docs.google.com/spreadsheets/d/1x
      vqc2CtKmi1UOCftX5hTBz9ctgRrCHqw5xGAmnNSIiI/edit?usp=sharing
    best: 0
    worst: +inf
  period:
    reference: 1985-2014
  plausible_values:
  - min: 0
    max: 50
    source: eurocordex_gcm_selection_team
    comment:
      Just a test value

```

#### Dobler SST rmse NAtl

Located in [CMIP6_studies/Dobler.yaml](CMIP6_studies/Dobler.yaml)

['pers. comm.', 'A. Dobler']

```
- key: Dobler SST rmse NAtl
  doi: ['pers. comm.', 'A. Dobler']
  type: performance
  spatial_scope: NAtl
  temporal_scope: Annual
  data_source: author
  metric:
    name: sstrmse
    long_name: Sea Surface Temperature RMSE w.r.t. HadISST
    units: K
    variables: tos
    comment:
      Root mean squared error of the annual mean sea surface temperature as
      compared to the HadISST data set. https://docs.google.com/spreadsheets/d/1
      xvqc2CtKmi1UOCftX5hTBz9ctgRrCHqw5xGAmnNSIiI/edit?usp=sharing
    best: 0
    worst: +inf
  period:
    reference: 1985-2014
  plausible_values:
  - min: 0
    max: 4
    source: eurocordex_gcm_selection_team
    comment:
      Just a test value

```

#### Dobler SICE rmse BNS

Located in [CMIP6_studies/Dobler.yaml](CMIP6_studies/Dobler.yaml)

['pers. comm.', 'A. Dobler']

```
- key: Dobler SICE rmse BNS
  doi: ['pers. comm.', 'A. Dobler']
  type: performance
  spatial_scope: BNS
  temporal_scope: Annual
  data_source: author
  metric:
    name: siconcrmse
    long_name: Sea Ice RMSE w.r.t. HadICE
    units: percent
    variables: siconc
    comment:
      Root mean squared error of the annual mean sea ice concentration as
      compared to the HadICE data set. https://docs.google.com/spreadsheets/d/1x
      vqc2CtKmi1UOCftX5hTBz9ctgRrCHqw5xGAmnNSIiI/edit?usp=sharing
    best: 0
    worst: +inf
  period:
    reference: 1985-2014
  plausible_values:
  - min: 0
    max: 50
    source: eurocordex_gcm_selection_team
    comment:
      Just a test value

```

#### Dobler SST rmse BNS

Located in [CMIP6_studies/Dobler.yaml](CMIP6_studies/Dobler.yaml)

['pers. comm.', 'A. Dobler']

```
- key: Dobler SST rmse BNS
  doi: ['pers. comm.', 'A. Dobler']
  type: performance
  spatial_scope: BNS
  temporal_scope: Annual
  data_source: author
  metric:
    name: sstrmse
    long_name: Sea Surface Temperature RMSE w.r.t. HadISST
    units: K
    variables: tos
    comment:
      Root mean squared error of the annual mean sea surface temperature as
      compared to the HadISST data set. https://docs.google.com/spreadsheets/d/1
      xvqc2CtKmi1UOCftX5hTBz9ctgRrCHqw5xGAmnNSIiI/edit?usp=sharing
    best: 0
    worst: +inf
  period:
    reference: 1985-2014
  plausible_values:
  - min: 0
    max: 4
    source: eurocordex_gcm_selection_team
    comment:
      Just a test value

```

### Spread of future outcomes
#### Sch20 ECS

Located in [CMIP6_studies/Sch20.yaml](CMIP6_studies/Sch20.yaml)

Manuel Schlund et al. (2020) Emergent constraints on equilibrium climate  sensitivity in CMIP5: do they hold for CMIP6?, https://doi.org/10.5194%2Fesd-11-1233-2020

```
- key: Sch20 ECS
  doi: 10.5194/esd-11-1233-2020
  type: future_spread
  spatial_scope: Global
  temporal_scope: Annual
  data_source: reference
  metric:
    name: ECS
    long_name: Equilibrium climate sensitivity
    units: K
    variables: tas
    comment:
      ECS is calculated with ESMValTool (Gregory method). CMIP5 range is [2.08,
      4.67]. Ensemble member added to make it comparable to scenarioMIP runs,
      although ECS is derived from 4xCO2 runs, unrelated to scenarioMIP.

```

#### Oud20 jetposdelta

Located in [CMIP6_studies/Oud20.yaml](CMIP6_studies/Oud20.yaml)

Thomas Oudar et al. (2020) Drivers of the Northern Extratropical Eddy-Driven Jet Change in CMIP5 and CMIP6 Models, https://doi.org/10.1029%2F2019gl086695

```
- key: Oud20 jetposdelta
  doi: 10.1029/2019GL086695
  type: future_spread
  spatial_scope: EUR
  temporal_scope: ONDJFM
  metric:
    name: jetposdelta
    long_name: Jet Stream North-South position delta change
    units: degrees_north
    variables: ua850
    comment:
      Jet position delta change estimated by subtracting the ONDJFM mean eddy-
      driven jet position over the period 2080-2099 w.r.t. preindustrial
      1860-1900
  period:
    reference: 1860-1900
    target: 2080-2099
  classes:
  - limits: [-90, -0.5, 0.5, 90]
    labels: ['strong south change', 'weak change', 'strong north change']
    source: eurocordex_gcm_selection_team

```

#### Atlas Dtas NEU JJA

Located in [CMIP6_studies/AtlasIPCC.yaml](CMIP6_studies/AtlasIPCC.yaml)

['Pers. Comm.', 'Jesus Fernandez']

```
- key: Atlas Dtas NEU JJA
  doi: ['Pers. Comm.', 'Jesus Fernandez']
  type: future_spread
  spatial_scope: NEU
  temporal_scope: JJA
  data_source: author_adapted
  metric:
    name: delta_tas
    long_name: Near surface temperature delta change 2071-2100 w.r.t. 1981-2010
    units: K
    variables: tas
    comment:
      Data derived from https://github.com/IPCC-WG1/Atlas/tree/devel/datasets-
      aggregated-regionally using the tas_landsea dataset.
  period:
    reference: 1981-2010
    target: 2071-2100

```

#### Sevault MED SST warming

Located in [CMIP6_studies/Sevault.yaml](CMIP6_studies/Sevault.yaml)

['pers_comm', 'F. Sevault']

```
- key: Sevault MED SST warming
  doi: ['pers_comm', 'F. Sevault']
  type: future_spread
  spatial_scope: MED
  temporal_scope: Annual
  data_source: author
  metric:
    name: deltasst
    long_name: Future sea surface temperature change
    units: K
    variables: sst
    comment:
      Mediterranean SST future evolution, SSP585, end21st (F. Sevault, pers.
      comm.) TO-DO which periods? temporal scope?
  classes:
  - limits: [2, 3, 4, 10]
    labels: ['weak', 'medium', 'strong']
    source: eurocordex_gcm_selection_team
    comment:
      [Sam] I have used a color code for making warming level categories (green:
      weak, orange: medium, red:strong). Arbitrary thresholds for now: green
      (2-3), orange (3-4), red (>4 deg)

```

### Independence
#### Bru20 mfamily

Located in [CMIP6_studies/Bru20.yaml](CMIP6_studies/Bru20.yaml)

Lukas Brunner et al. (2020) Reduced global warming from CMIP6 projections when weighting models by performance and independence, https://doi.org/10.5194%2Fesd-11-995-2020

```
- key: Bru20 mfamily
  doi: 10.5194/esd-11-995-2020
  type: independence
  spatial_scope: Global
  data_source: reference
  metric:
    name: mfamily
    long_name: None
    units: categorical
    variables: ['tas', 'psl']
    comment:
      From Figure 5. Model family tree for all 33 CMIP6 models, similar to
      Knutti et al. (2013). Models branching further to the left are more
      dependent, and models branching further to the right are more independent.
      The analysis is based on global, horizontally resolved tasCLIM and pslCLIM
      in the period from 1980 to 2014. Labels with the same color indicate
      models with obvious dependencies, such as shared components or the same
      origin, whereas models with no clear dependencies are labeled in black.
      Strangely, ACCESS-CM2 is in the same family as UKESM and HadGEM3, but not
      ACCESS-ESM1-5.
  period:
    reference: 1980-2014

```

