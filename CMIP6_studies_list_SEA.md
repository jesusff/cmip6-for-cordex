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
## Available entries (SEA scope)
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
      Evaluation of the model using global criteria performance criteria (past
      trends + spatial pattern) Model with performance scores below 0.006 are
      considered as irrealistic.  This study is based on multi-member for each
      model, not on only one member. Wrt to the original article, we consider
      here only the performance criteria and not the combined criteria that
      takes also into account the independence.
  period:
    reference: 1980-2014
  plausible_values:
  - min: 0.006
    max: 0.2
    source: author
    comment:
      The 0.006 threshold has been provided by the author (expert judgment)
      after email exchanges with S. Somot

```

#### Qasmi Constr Global Dtas ssp245 2050

Located in [CMIP6_studies/Qasmi.yaml](CMIP6_studies/Qasmi.yaml)

None

```
- key: Qasmi Constr Global Dtas ssp245 2050
  doi: None
  type: performance
  spatial_scope: Global
  temporal_scope: Annual
  data_source: author
  metric:
    name: Constrained-Dtas
    long_name: Observationally-contrained future climate change
    units: binary
    variables: tas
    comment:
      Constrained global annual temperature future climate change range,
      2041-2060 vs 1850-1900, SSP245 (adapted from Ribes et al. 2021 by S.
      Qasmi). In particular by adding recently available CMIP6 GCM, now 40 GCMs.
  period:
    reference: 1850-1900
    target: 2041-2060
  plausible_values:
  - min: 1
    max: 1
    source: author
    comment:
      models lying outside the observationally-constrained 90% interval obtained
      by the method are considered as implausible. The 90% interval is [1.5 ;
      2.1]degC for the period 2041-2060 vs 1850-1900, SSP245. Multi-member
      ensemble mean is used in this study for every model. Note that this
      criteria is very strict and can potentially eliminate a large number of
      GCMs.

```

### Spread of future outcomes
#### AR6 TCR as spread

Located in [CMIP6_studies/AR6.yaml](CMIP6_studies/AR6.yaml)

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
  - limits: [-10, 1.2, 1.6, 2.0, 2.4, 10]
    labels: ['very low', 'low', 'moderate', 'high', 'very high']
    source: eurocordex_gcm_selection_team
    comment:
      A proposal with 0.4 degree bins in the very likely range (1.2, 2.4)
      provided by the IPCC AR6

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
      Using this figure 5, we have put in the same family, the GCM lines that
      merge before the dashed line, that correponds to the independence shape
      parameter. We have given family names only to families with at least 2
      members. Note that we are not using the Figure 5 color code to determine
      the family. This leads to some surprise such as  Strangely, ACCESS-CM2 is
      in the same family as UKESM and HadGEM3, but not ACCESS-ESM1-5. This was
      confirmed as ok by the Australian group. Also the two FGOALS model are not
      belonging to the same family with this criteria.
  period:
    reference: 1980-2014

```

