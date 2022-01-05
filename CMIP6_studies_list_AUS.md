## Incomplete entries

 * [Fas20](CMIP6_studies/Fas20.yaml)
 * [Beo21](CMIP6_studies/Beo21.yaml)
## Disabled entries

 · [Rib21 Constrained TCR](CMIP6_studies/Rib21.yaml)
 · [Fas20](CMIP6_studies/Fas20.yaml)
 · [Atlas Dtas world DJF](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dtas world JJA](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dpr world DJF](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dpr world JJA](CMIP6_studies/AtlasIPCC.yaml)
 · [Beo21](CMIP6_studies/Beo21.yaml)
 · [Tok20 Constrained TCR](CMIP6_studies/Tok20.yaml)
 · [Tok20 TCR as spread](CMIP6_studies/Tok20.yaml)
## Available entries (AUS scope)
### Plausibility
#### AR6 TCR very likely range

Located in [CMIP6_studies/AR6.yaml](CMIP6_studies/AR6.yaml)

Preferred to [CMIP6_studies/Rib21.yaml](CMIP6_studies/Rib21.yaml)

None

```
- key: AR6 TCR very likely range
  doi: None
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
      TCR as provided by th IPCC WGI AR6 on Table 7.SM.5 (https://www.ipcc.ch/re
      port/ar6/wg1/downloads/report/IPCC_AR6_WGI_Chapter_07_Supplementary_Materi
      al.pdf).
  plausible_values:
  - min: 1.2
    max: 2.4
    source: reference
    comment:
      This is a 90% (very likely) range for the TCR according to AR6 Technical
      Summary: Based on  process understanding, warming over the instrumental
      record, and emergent constraints, the best estimate of TCR is 1.8 degC,
      the likely range is 1.4 to 2.2 degC and the very likely range is 1.2 to
      2.4 DegC. There is a high level of agreement among the different lines of
      evidence (Figure TS.16c) (high confidence). {7.5.5}

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

### Spread of future outcomes
#### AR6 TCR as spread

Located in [CMIP6_studies/AR6.yaml](CMIP6_studies/AR6.yaml)

Preferred to [CMIP6_studies/Tok20.yaml](CMIP6_studies/Tok20.yaml)

None

```
- key: AR6 TCR as spread
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
      TCR as provided by th IPCC WGI AR6 on Table 7.SM.5 (https://www.ipcc.ch/re
      port/ar6/wg1/downloads/report/IPCC_AR6_WGI_Chapter_07_Supplementary_Materi
      al.pdf).
  classes:
  - limits: [-10, 1.5, 2, 2.5, 10]
    labels: ['low', 'moderate', 'high', 'very high']
    source: eurocordex_gcm_selection_team
    comment:
      Test values

```

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

### Other criteria
#### Bru20 mfamily

Located in [CMIP6_studies/Bru20.yaml](CMIP6_studies/Bru20.yaml)

Lukas Brunner et al. (2020) Reduced global warming from CMIP6 projections when weighting models by performance and independence, https://doi.org/10.5194%2Fesd-11-995-2020

```
- key: Bru20 mfamily
  doi: 10.5194/esd-11-995-2020
  type: other
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

#### atm. res. km

Located in [CMIP6_studies/Resolution.yaml](CMIP6_studies/Resolution.yaml)

None

```
- key: atm. res. km
  doi: None
  type: other
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
  type: other
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
      order Atm-Lnd-Ocn-SI-Veg-Tbgc-Aer-Chem-Obgc-Gla
  plausible_values:
  - min: 2222000000
    max: 2222222222
    source: eurocordex_gcm_selection_team
    comment:
      At least coupled Atm-Lnd-Ocn-SI with some form of aerosol consideration

```

