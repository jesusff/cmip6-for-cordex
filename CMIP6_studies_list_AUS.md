## Incomplete entries

 * [Fas20](CMIP6_studies/Fas20.yaml)
 * [Beo21](CMIP6_studies/Beo21.yaml)
## Disabled entries

 · [Fas20](CMIP6_studies/Fas20.yaml)
 · [Atlas Dtas world DJF](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dtas world JJA](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dpr world DJF](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dpr world JJA](CMIP6_studies/AtlasIPCC.yaml)
 · [Beo21](CMIP6_studies/Beo21.yaml)
 · [Tok20 Constrained TCR](CMIP6_studies/Tok20.yaml)
## Available entries (AUS scope)
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

