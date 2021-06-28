## Incomplete entries

 * [Fas20](CMIP6_studies/Fas20.yaml)
 * [Beo21](CMIP6_studies/Beo21.yaml)
## Disabled entries

 · [Fas20](CMIP6_studies/Fas20.yaml)
 · [Atlas Dtas MED DJF](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dtas world DJF](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dtas NEU JJA](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dtas MED JJA](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dtas world JJA](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dpr NEU DJF](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dpr MED DJF](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dpr world DJF](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dpr NEU JJA](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dpr world JJA](CMIP6_studies/AtlasIPCC.yaml)
 · [Can20 marle](CMIP6_studies/Can20.yaml)
 · [Beo21](CMIP6_studies/Beo21.yaml)
 · [Tok20 Constrained TCR](CMIP6_studies/Tok20.yaml)
 · [Fer21 Lamb TPMS](CMIP6_studies/Fer21.yaml)
## Available entries (EUR scope)
### Plausibility
#### Rib21 Constrained TCR

Located in [CMIP6_studies/Rib21.yaml](CMIP6_studies/Rib21.yaml)

Preferred to [CMIP6_studies/Tok20.yaml](CMIP6_studies/Tok20.yaml)

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
    variables: ['tas', 'psl']
    comment:
      Evaluation of the model using global criteria (past trends + spatial
      pattern) and independence criteria. Model with performance scores below
      0.006 are considered as irrealistic. This study is based on multi-member
      for each model, not on only one member. Here only the performance criteria
      and not the combined criteria that takes also into account the
      independence.
  period:
    reference: 1980-2014
  plausible_values:
  - min: 0.006
    max: 0.2
    source: reference
    comment:
      author provided? to be checked

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

Preferred to [CMIP6_studies/Can20.yaml](CMIP6_studies/Can20.yaml)
[CMIP6_studies/Fer21.yaml](CMIP6_studies/Fer21.yaml)

Swen Brands et al. (2021) A circulation-based performance atlas of the CMIP5 and 6 models, https://doi.org/10.5194%2Fgmd-2020-418

```
- key: Bra21 Lamb EUR
  doi: 10.5194/gmd-2020-418
  type: performance
  spatial_scope: EUR
  temporal_scope: Annual
  data_source: author_adapted
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
    max: 1
    source: eurocordex_gcm_selection_team
    comment:
      Test value
  - min: 0
    max: 5
    source: author
    comment:
      The range of plausible values is directly obtained from the reference, the
      maximum MAE obtained there is here rounded to the next integer.

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

#### Sevault MED SST

Located in [CMIP6_studies/Sevault.yaml](CMIP6_studies/Sevault.yaml)

['pers_comm', 'F. Sevault', 'CNRM']

```
- key: Sevault MED SST
  doi: ['pers_comm', 'F. Sevault', 'CNRM']
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
      For the performance criteria, we compute the spatial RMSE on the 12-month
      bias maps over the period 1985-2014. It means that we first compute the
      temporal average to obtain a mean seasonal cycle - 12maps- of the bias
      maps and then we compute the spatio-temporal RMSE). All the models are
      interpolated on the grid of the refererence dataset, and then a mask of
      the Mediterranean Sea is applied (no Black Sea).  The reference dataset is
      a specific CMEMS product developed for the Mediterranean Sea,
      GOS-L4_GHRSST-SSTfnd-OISST_HR_REP-MED-v02.0-fv02.0 data (Pisano et al.
      2016, doi:10.1016/j.rse.2016.01.019, Casey et al. 2010,
      doi:10.1007/978-90-481-8681-5_16 . Generated/provided by Copernicus Marine
      Service and CNR - ISMAR ROME.
    best: 0
    worst: inf
  plausible_values:
  - min: 0
    max: 2
    source: author
    comment:
      The plausibility threshold is difficult to set.

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

#### atm. res. km

Located in [CMIP6_studies/Resolution.yaml](CMIP6_studies/Resolution.yaml)

None

```
- key: atm. res. km
  doi: None
  type: performance
  spatial_scope: special
  temporal_scope: Annual
  data_source: author
  metric:
    name: resolution
    long_name: Nominal resolution of the atmospheric component
    units: km
    variables: None
    comment:
      Data extracted from the CMIP github https://github.com/WCRP-
      CMIP/CMIP6_CVs/blob/master/CMIP6_source_id.json using
      util/resolution_to_yaml.py Manually edited to include appropriate runs.
    best: 0
  plausible_values:
  - min: 0
    max: 300
    source: eurocordex_gcm_selection_team
    comment:
      Test value

```

#### Bra21 complexity

Located in [CMIP6_studies/Bra21.yaml](CMIP6_studies/Bra21.yaml)

Swen Brands et al. (2021) A circulation-based performance atlas of the CMIP5 and 6 models, https://doi.org/10.5194%2Fgmd-2020-418

```
- key: Bra21 complexity
  doi: 10.5194/gmd-2020-418
  type: performance
  spatial_scope: special
  temporal_scope: Annual
  data_source: reference
  metric:
    name: complexity
    long_name: Complexity of model components
    units: categorical
    variables: []
    comment:
      Model complexity from Table 1 is coded with ternary values   0 - not
      considered   1 - prescribed   2 - interactive component in the following
      order Atm-Lnd-Ocn-SI-Aer-Chem-Tbgc-Obgc-Veg-Gla
  plausible_values:
  - min: 2222100000
    max: 2222222222
    source: eurocordex_gcm_selection_team
    comment:
      At least coupled Atm-Lnd-Ocn-SI with some form of aerosol consideration

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

#### Tok20 TCR as spread

Located in [CMIP6_studies/Tok20.yaml](CMIP6_studies/Tok20.yaml)

None

```
- key: Tok20 TCR as spread
  doi: None
  type: future_spread
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
      (we use the mean of the years 61 to 80).
  classes:
  - limits: [-10, 1.5, 2, 2.5, 10]
    labels: ['low', 'moderate', 'high', 'very high']
    source: eurocordex_gcm_selection_team
    comment:
      Test values

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

#### Qasmi tas warming class

Located in [CMIP6_studies/Qasmi.yaml](CMIP6_studies/Qasmi.yaml)

['pers_comm', 'S. Qasmi']

```
- key: Qasmi tas warming class
  doi: ['pers_comm', 'S. Qasmi']
  type: future_spread
  spatial_scope: MED+NEU+CEU
  temporal_scope: DJF+JJA
  data_source: author
  metric:
    name: deltatas_class
    long_name: Warming classes according to future surface air temperature change
    units: categorical
    variables: tas
    comment:
      Regional tas change in Europe MED, NEU, CEU, MED+NEU+CEU, DJF, JJA,
      2041-2060 vs 1850-1900, SSP245. S. Qasmi, numerical values available soon.
      Only warming classes for now.
  period:
    reference: 1850-1900
    target: 2041-2060
  classes:
  - limits: [-0.5, 0.5, 1.5, 2.5, 3.5]
    labels: ['implausible', 'weak warming', 'medium warming', 'strong warming']
    source: author
    comment:
      From Google sheet [Sam] Class 2 lies in the interquartile (Q25-Q75) of the
      constrained range, class 1 is between Q5 and Q25 and classe 3 is between
      Q75 and Q95 of the constrained range. Class 0 means eliminated by the
      plausibility criteria. [Chus] The elimination by plausibility criteria can
      be automatically marked by the greyed out number (it is active now). In
      this way, we can assess whether they also misbehave in the future spread.
      Also, the data are available in case thresholds are adjusted and a model
      comes back to the plausible range. [Sam] agreed. I will modify this when I
      have the numerical values from Said Qasmi. But I guess that it is a
      duplication of your atlas values, except for the fact that it uses pre-
      indust as a reference what is interesting for GWL-based study TO-DO decide
      on the source for these deltas and use classes to assign warming levels.
      Atlas data can be used to generate deltas for any period/region/scenario

```

#### Atlas Dtas NEU DJF

Located in [CMIP6_studies/AtlasIPCC.yaml](CMIP6_studies/AtlasIPCC.yaml)

['Pers. Comm.', 'Jesus Fernandez']

```
- key: Atlas Dtas NEU DJF
  doi: ['Pers. Comm.', 'Jesus Fernandez']
  type: future_spread
  spatial_scope: NEU
  temporal_scope: DJF
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

#### Atlas Dpr MED JJA

Located in [CMIP6_studies/AtlasIPCC.yaml](CMIP6_studies/AtlasIPCC.yaml)

['Pers. Comm.', 'Jesus Fernandez']

```
- key: Atlas Dpr MED JJA
  doi: ['Pers. Comm.', 'Jesus Fernandez']
  type: future_spread
  spatial_scope: MED
  temporal_scope: JJA
  data_source: author_adapted
  metric:
    name: delta_pr
    long_name: Precipitation relative delta change 2071-2100 w.r.t. 1981-2010
    units: percent
    variables: pr
    comment:
      Data derived from https://github.com/IPCC-WG1/Atlas/tree/devel/datasets-
      aggregated-regionally using the pr_land dataset.
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
      For the Future spread, we simply compute the basin-averaged and temporal-
      averaged climate change response (annual mean) over the Mediterranean Sea
      (no Black Sea) for the period 2070-2099 wrt the present-climate 1985-2014
      period for the SSP585 scenario.
  classes:
  - limits: [2, 3, 4, 10]
    labels: ['weak', 'medium', 'strong']
    source: eurocordex_gcm_selection_team
    comment:
      The limits of the warming level categories (weak, medium, strong) are
      arbitrary.

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

