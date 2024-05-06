## Incomplete entries

 * [Cob21](CMIP6_studies/Cob21.yaml)
 * [Fas20](CMIP6_studies/Fas20.yaml)
 * [Beo21](CMIP6_studies/Beo21.yaml)
## Globally disabled entries

 · [Tok20 Constrained TCR](CMIP6_studies/Tok20.yaml)
 · [Pri20 storm track DJF](CMIP6_studies/Pri20.yaml)
 · [Pri20 storm track JJA](CMIP6_studies/Pri20.yaml)
 · [Cob21](CMIP6_studies/Cob21.yaml)
 · [Atlas Dtas world DJF](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dtas world JJA](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dpr world DJF](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dpr world JJA](CMIP6_studies/AtlasIPCC.yaml)
 · [Fas20](CMIP6_studies/Fas20.yaml)
 · [Dobler SST rmse MED](CMIP6_studies/Dobler.yaml)
 · [Beo21](CMIP6_studies/Beo21.yaml)
 · [Can20 marle](CMIP6_studies/Can20.yaml)
 · [Rib21 Constrained TCR](CMIP6_studies/Rib21.yaml)
 · [Fer21 Lamb TPMS](CMIP6_studies/Fer21.yaml)
## Entries disabled in MED

 · [Sevault MED SST](CMIP6_studies/Sevault.yaml)
 · [Dobler SST rmse EUR](CMIP6_studies/Dobler.yaml)
 · [McSw15 circ DJF](CMIP6_studies/McSw15.yaml)
 · [McSw15 circ JJA](CMIP6_studies/McSw15.yaml)
## Available entries (MED scope)
### Plausibility
#### AR6 TCR

Located in [CMIP6_studies/AR6.yaml](../CMIP6_studies/AR6.yaml)

None

```
- key: AR6 TCR
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

Located in [CMIP6_studies/Bru20.yaml](../CMIP6_studies/Bru20.yaml)

10.5194/esd-11-995-2020

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

#### Dalelane MNQS

Located in [CMIP6_studies/Dalelane.yaml](../CMIP6_studies/Dalelane.yaml)

['pers. comm.', 'C. Dalelane', 'DWD']

```
- key: Dalelane MNQS
  doi: ['pers. comm.', 'C. Dalelane', 'DWD']
  type: performance
  spatial_scope: Global
  temporal_scope: Annual
  data_source: author
  metric:
    name: MNQS
    long_name: Multivariate Network Quality Score for Global Teleconnections
    units: 1
    variables: tos, z500
    comment:
      Data is converted to seasonal anomalies, detrended with season-reliant
      trend-EOFs.  Seasonal variances normalized.  Adjacency-matrix between all
      pairs of grid cell with Spearman's rank correlation.  Maximal domains in
      tos (z500) with average pairwise rank correlation>0.95(0.93)- quantile of
      all pairwise correlations are found. All pairwise links between domains
      (area weighted average time series) calculated with Distance correlation
      in tos,  z500 and cross-links between tos and z500. Tested to level 0.05
      with control of  False Discovery Rate=0.05. New adjacency matrices
      constructed based on domain links. Adjacency matrices compared to
      references with Structural Similarity Index (SSIM).       Exponential
      transform wrt. value 1 for all 3 variables (individual Network Quality
      Score-NQS). Geometric mean of NQSs over variables (Multivariate Network
      Quality Score, MNQS). Average of MNQSs over references.
    best: 1
    worst: 0
  plausible_values:
  - min: 0
    max: 1
    source: author
    comment:
      the higher the better, MNQS between references in the table for comparison

```

#### Qasmi Constr Global Dtas ssp245 2050

Located in [CMIP6_studies/Qasmi.yaml](../CMIP6_studies/Qasmi.yaml)

10.1126/sciadv.abc0671

```
- key: Qasmi Constr Global Dtas ssp245 2050
  doi: 10.1126/sciadv.abc0671
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

#### Bra21 Lamb EUR

Located in [CMIP6_studies/Bra21.yaml](../CMIP6_studies/Bra21.yaml)

10.5194/gmd-2020-418

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

#### Dav20 blocking freq DJF

Located in [CMIP6_studies/Div20.yaml](../CMIP6_studies/Div20.yaml)

10.1175/JCLI-D-19-0862.1

```
- key: Dav20 blocking freq DJF
  doi: 10.1175/JCLI-D-19-0862.1
  type: performance
  spatial_scope: EUR
  temporal_scope: DJF
  data_source: author
  metric:
    name: blocking
    long_name: blocking frequency
    units: categorical
    variables: zg
    comment:
      Scoring of models on performance for blocking frequency. Blocking
      frequency bias has been calculated by the method of Davini and D'Andrea
      (2020). The individual CMIP6 models have then been clustered into
      categories based on their RMSE, bias and correlation compared to multiple
      reanalysis JRA-55, NCEP-NCAR, ERA-40, ERA-Interim. Data for individual
      CMIP6 models and clustering of errors into categories are provided by the
      author for Europe.  Based on the method of qualitative scoring in
      McSweeney et al. (2015) and adapted for CMIP6. The scoring has been
      changed from the traffic light coding to numbers for EURO-CORDEX.  Values
      0 - Low errors over both local and remote regions.     Captures key
      characteristics of the criteria spatially or temporarily, 1 - Some
      substantial errors present but not widespread or not present in     the
      local region of interest. Location of larger remote errors are not
      known to have a downstream impact in the local region of interest.
      Captures key characteristics of the criteria spatially or temporarily, 2 -
      Substantial errors in remote regions where downstream effects could     be
      expected to impact on the reliability of regional information     and/or
      present in the local region of interest, 3 - Large widespread errors to
      the extent that the model is unable to     represent the present-day
      climatology in a useful way and future     projections by the model cannot
      be interpreted in a meaningful way.
    best: 0
    worst: 3
  period:
    reference: 1961-2000
  plausible_values:
  - min: 0
    max: 2
    source: author
    comment:
      Large widespread errors (value 3) lead to consider the model unplausible.

```

#### Dav20 blocking freq JJA

Located in [CMIP6_studies/Div20.yaml](../CMIP6_studies/Div20.yaml)

10.1175/JCLI-D-19-0862.1

```
- key: Dav20 blocking freq JJA
  doi: 10.1175/JCLI-D-19-0862.1
  type: performance
  spatial_scope: EUR
  temporal_scope: JJA
  data_source: author
  metric:
    name: blocking
    long_name: blocking frequency
    units: categorical
    variables: zg
    comment:
      Scoring of models on performance for blocking frequency. Blocking
      frequency bias has been calculated by the method of Davini and D'Andrea
      (2020). The individual CMIP6 models have then been clustered into
      categories based on their RMSE, bias and correlation compared to multiple
      reanalysis JRA-55, NCEP-NCAR, ERA-40, ERA-Interim. Data for individual
      CMIP6 models and clustering of errors into categories are provided by the
      author for Europe.  Based on the method of qualitative scoring in
      McSweeney et al. (2015) and adapted for CMIP6. The scoring has been
      changed from the traffic light coding to numbers for EURO-CORDEX.  Values
      0 - Low errors over both local and remote regions.     Captures key
      characteristics of the criteria spatially or temporarily, 1 - Some
      substantial errors present but not widespread or not present in     the
      local region of interest. Location of larger remote errors are not
      known to have a downstream impact in the local region of interest.
      Captures key characteristics of the criteria spatially or temporarily, 2 -
      Substantial errors in remote regions where downstream effects could     be
      expected to impact on the reliability of regional information     and/or
      present in the local region of interest, 3 - Large widespread errors to
      the extent that the model is unable to     represent the present-day
      climatology in a useful way and future     projections by the model cannot
      be interpreted in a meaningful way.
    best: 0
    worst: 3
  period:
    reference: 1961-2000
  plausible_values:
  - min: 0
    max: 2
    source: author
    comment:
      Large widespread errors (value 3) lead to consider the model unplausible.

```

#### Nabat EUR AOD

Located in [CMIP6_studies/Nabat.yaml](../CMIP6_studies/Nabat.yaml)

['pers_comm', 'Pierre Nabat']

```
- key: Nabat EUR AOD
  doi: ['pers_comm', 'Pierre Nabat']
  type: performance
  spatial_scope: EUR
  temporal_scope: Annual
  data_source: author
  metric:
    name: aod_rmse
    long_name: plausibillity of RMSE of the European Aerosol Optical Depth
    units: aod
    variables: aod550
    comment:
      Aerosol Optical Depth (AOD) spatial RMSE, annual mean, satellite reference
      dataset (MACv2, 2000-2014)
    best: 0
    worst: +inf
  plausible_values:
  - min: 0
    max: 0.2
    source: author
    comment:
      Plausibility threshold is set at 0.2. All models are below 0.2 except for
      2 GCMs from the same institute that are above 0.7

```

#### Nabat EUR AOD hist trend

Located in [CMIP6_studies/Nabat.yaml](../CMIP6_studies/Nabat.yaml)

['pers_comm', 'Pierre Nabat']

```
- key: Nabat EUR AOD hist trend
  doi: ['pers_comm', 'Pierre Nabat']
  type: performance
  spatial_scope: EUR
  temporal_scope: Annual
  data_source: author
  metric:
    name: aod_histtrend
    long_name: plausibillity of past trend of the European Aerosol Optical Depth
    units: aod
    variables: aod550
    comment:
      Change in Aerosol Optical Depth (AOD) between 2 sub-periods of the
      historical run, annual mean Difference in AOD is computed between
      2000-2014 and 1976-1990.  This period corresponds to the well-known
      brightening period in Europe during which it is virtual certain that AOD
      has decreased over Europe This metrics is inspired by Nabat et al. 2014,
      doi:10.1002/2014GL060798 The MACv2 dataset can be used to obtain a low-
      confidence estimate of the real value.  MACv2 shows a AOD decrease of
      -0.0315 between 1976-1990 and 2000-2014. Any GCM having a trend more than
      2 times MACv2 (<-0.08) can be considered as showing a strong AOD past
      trend that will contribute to re-inforce the historical warming in the RCM
    best: 0
    worst: +inf
  plausible_values:
  - min: -999
    max: 0
    source: author
    comment:
      Plausibility threshold is set at 0, meaning that any postive value
      (increase in AOD over the period) is considered as implausible.

```

#### Oud20 jetpos

Located in [CMIP6_studies/Oud20.yaml](../CMIP6_studies/Oud20.yaml)

10.1029/2019GL086695

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
  - min: -3
    max: 3
    source: author

```

#### Palmer23 EUR Circ DJF

Located in [CMIP6_studies/Palmer23.yaml](../CMIP6_studies/Palmer23.yaml)

10.5194/esd-14-457-2023

```
- key: Palmer23 EUR Circ DJF
  doi: 10.5194/esd-14-457-2023
  type: performance
  spatial_scope: EUR
  temporal_scope: DJF
  data_source: author
  metric:
    name: circulation
    long_name: plausibillity of the large scale atmospherc circulation pattern for Europe
    units: categorical
    variables: ua850 va850
    comment:
      Qualitative large scale circulation patter score based on overall pattern,
      bias and RMSE. Based on 20 year climatology comparison with ERA5
      1995-2014. criteria is an updated on the work by McSweeney et al. 2015 but
      for CMIP6 Based on the method of qualitative scoring in McSweeney et al.
      (2015) and adapted for CMIP6. The scoring has been changed from the
      traffic light coding in the paper to numbers here 1 (white)  -
      Satisfactory. It gathers two categories: Low errors over both local and
      remote regions and Some substantial errors present but not widespread or
      not present in the local region of interest.               Location of
      larger remote errors are not known to have a downstream impact in the
      local region of interest. Captures key characteristics of the criteria
      spatially or temporarily. 2 (orange) - Unsatisfactory, substantial errors
      in remote regions where downstream effects could be expected to impact on
      the reliability of regional information and/or present in the local region
      of interest. 3 (red)    - Inadequate. Large widespread errors to the
      extent that the model is unable to represent the present-day climatology
      in a useful way and future projections by the model cannot be interpreted
      in a meaningful way.   (grey)   - Data/ analysis not available for a given
      model. This category ha sno number here
    best: 1
    worst: 3
  plausible_values:
  - min: 1
    max: 2
    source: author
    comment:
      In agreement with the authors we decided to eliminate only models with the
      Red flag (Inadequate, value = 3)

```

#### Palmer23 Circ EUR Circ JJA

Located in [CMIP6_studies/Palmer23.yaml](../CMIP6_studies/Palmer23.yaml)

10.5194/esd-14-457-2023

```
- key: Palmer23 Circ EUR Circ JJA
  doi: 10.5194/esd-14-457-2023
  type: performance
  spatial_scope: EUR
  temporal_scope: DJF
  data_source: author
  metric:
    name: circulation
    long_name: plausibillity of the large scale atmospherc circulation pattern for Europe
    units: categorical
    variables: ua850 va850
    comment:
      Qualitative large scale circulation patter score based on overall pattern,
      bias and RMSE. Based on 20 year climatology comparison with ERA5
      1995-2014. criteria is an updated on the work by McSweeney et al. 2015 but
      for CMIP6 Based on the method of qualitative scoring in McSweeney et al.
      (2015) and adapted for CMIP6. The scoring has been changed from the
      traffic light coding in the paper to numbers here 1 (white)  -
      Satisfactory. It gathers two categories: Low errors over both local and
      remote regions and Some substantial errors present but not widespread or
      not present in the local region of interest.               Location of
      larger remote errors are not known to have a downstream impact in the
      local region of interest. Captures key characteristics of the criteria
      spatially or temporarily. 2 (orange) - Unsatisfactory, substantial errors
      in remote regions where downstream effects could be expected to impact on
      the reliability of regional information and/or present in the local region
      of interest. 3 (red)    - Inadequate. Large widespread errors to the
      extent that the model is unable to represent the present-day climatology
      in a useful way and future projections by the model cannot be interpreted
      in a meaningful way.   (grey)   - Data/ analysis not available for a given
      model. This category ha sno number here
    best: 1
    worst: 3
  plausible_values:
  - min: 1
    max: 2
    source: author
    comment:
      In agreement with the authors we decided to eliminate only models with the
      Red flag (Inadequate, value = 3)

```

#### Pri20 storm track

Located in [CMIP6_studies/Pri20.yaml](../CMIP6_studies/Pri20.yaml)

10.1175/JCLI-D-19-0928.1

```
- key: Pri20 storm track
  doi: 10.1175/JCLI-D-19-0928.1
  type: performance
  spatial_scope: EUR
  temporal_scope: DJF+JJA
  data_source: author
  metric:
    name: storm_track
    long_name: zonal mean North Atlantic storm track
    units: categorical
    variables: ua850 va850 MSLP 850 relative vorticity
    comment:
      Scoring of models on performance for the North Atlantic storm track. Based
      on RMSE of the zonal mean track profile between 25-80N compared to ERA5
      and qualitative assessment of the trimodal structure of the storm track.
      Storm track calculated by method in Priestly et al. (2020), data and
      scores provided by author. Based on the method of qualitative scoring in
      McSweeney et al. (2015) and adapted for CMIP6. The scoring has been
      changed from the traffic light coding to numbers for EURO-CORDEX.  Values
      0 - Low errors over both local and remote regions.     Captures key
      characteristics of the criteria spatially or temporarily, 1 - Some
      substantial errors present but not widespread or not present in     the
      local region of interest. Location of larger remote errors are not
      known to have a downstream impact in the local region of interest.
      Captures key characteristics of the criteria spatially or temporarily, 2 -
      Substantial errors in remote regions where downstream effects could     be
      expected to impact on the reliability of regional information     and/or
      present in the local region of interest, 3 - Large widespread errors to
      the extent that the model is unable to     represent the present-day
      climatology in a useful way and future     projections by the model cannot
      be interpreted in a meaningful way.
    best: 0
    worst: 3
  period:
    reference: 1979-2014
  plausible_values:
  - min: 0
    max: 2
    source: author
    comment:
      Large widespread errors (value 3) lead to consider the model unplausible.

```

#### Winderlich SCQS

Located in [CMIP6_studies/Winderlich.yaml](../CMIP6_studies/Winderlich.yaml)

['pers_comm', 'K. Winderlich', 'DWD']

```
- key: Winderlich SCQS
  doi: ['pers_comm', 'K. Winderlich', 'DWD']
  type: performance
  spatial_scope: EUR
  temporal_scope: Annual
  data_source: author
  metric:
    name: SCQS
    long_name: Synoptic Circulation Quality Score
    units: 1
    variables: z500
    comment:
      Domain is CORDEX-EUR. Data z500 is converted to daily anomalies and
      normalized by daily standard deviation. Data are then attributed to
      previously obtained Synoptic Circulation (SP) classes. Number of Synoptic
      Circulation classes is 43 (derived on daily ERA-Interim data, 1979-2018).
      For each model, 7 variables are computed from the attributed daily data.
      1) HIST - frequency of each SP-class (year through) 2) HIST_JFD -
      frequency of each SP-class (winter) 3) HIST_MAM - frequency of each SP-
      class (spring) 4) HIST_JJA - frequency of each SP-class (summer) 5)
      HIST_SON - frequency of each SP-class (autumn) 6) SEQUENCE - matrix of
      frequencies for the subsequent occurrence               of the pair of two
      synoptic patterns SPi?SPj. 7) PERSISTENCE - matrix of frequency for
      persistence of each                  SP-class for 1,2,3,.. N days in a
      row.   The SCQS is computed as the mean of 7 individual Quality Scores
      computed on each of these variables.
    best: 1
    worst: 0
  plausible_values:
  - min: 0
    max: 1
    source: author
    comment:
      The higher the better, SCQS between reference reanalysis (ERA-Interim) and
      an alternative reanalysis (NCAR-NCEP1) is in the table for comparison.

```

#### Dobler SST rmse SNA

Located in [CMIP6_studies/Dobler.yaml](../CMIP6_studies/Dobler.yaml)

Preferred to [CMIP6_studies/Dobler.yaml](../CMIP6_studies/Dobler.yaml)

['pers. comm.', 'A. Dobler']

```
- key: Dobler SST rmse SNA
  doi: ['pers. comm.', 'A. Dobler']
  type: performance
  spatial_scope: SNA
  temporal_scope: Annual
  data_source: author
  metric:
    name: sstrmse
    long_name: Sea Surface Temperature RMSE w.r.t. HadISST
    units: K
    variables: tos
    comment:
      Analogue to the MED SST RMSE, we compute the spatial RMSE on the 12-month
      bias maps over the period 1985-2014: first the average monthly SST are
      computed. Then, over all 12 maps of biases the RMSEs are calculated. All
      the models are interpolated onto the grid of the refererence HadISST 1.1
      monthly average sea surface temperature (Rayner et al. 2003,
      DOI:10.1029/2002JD002670) Missing values due to non-existing sea areas (in
      the GCM) are coded as -99 (RMSE is strictly positive). ----- Numbers are
      provided in: https://docs.google.com/spreadsheets/d/1xvqc2CtKmi1UOCftX5hTB
      z9ctgRrCHqw5xGAmnNSIiI/edit#gid=0 Area definitions: BNS: Baltic and North
      Sea NBS: Norwegian and Barents Sea NAtl: Nordic Atlantic (replaced by NBS)
      SNA: (Southern) Nord Atlantic MED: Mediterranean (disabled, use Sevault
      MED SST instead.  ) BLK: Black Sea EUR: Europe box Maps are provided in: h
      ttps://docs.google.com/spreadsheets/d/1xvqc2CtKmi1UOCftX5hTBz9ctgRrCHqw5xG
      AmnNSIiI/edit#gid=334563502 R-script reports (PDF files) used for the
      calcualtions are available at
      https://drive.google.com/drive/folders/1MRNO_h6EGcyGs4d82vqtTLyTLtNxHaQ0
    best: 0
    worst: +inf
  period:
    reference: 1985-2014
  plausible_values:
  - min: 0
    max: 2.5
    source: eurocordex_gcm_selection_team
    comment:
      Upper limit: (Mean + 2*sd) of the RMSEs of 29 models, rounded up to the
      next half integer.

```

#### Dobler SST rmse BLK

Located in [CMIP6_studies/Dobler.yaml](../CMIP6_studies/Dobler.yaml)

['pers. comm.', 'A. Dobler']

```
- key: Dobler SST rmse BLK
  doi: ['pers. comm.', 'A. Dobler']
  type: performance
  spatial_scope: BLK
  temporal_scope: Annual
  data_source: author
  metric:
    name: sstrmse
    long_name: Sea Surface Temperature RMSE w.r.t. HadISST
    units: K
    variables: tos
    comment:
      Analogue to the MED SST RMSE, we compute the spatial RMSE on the 12-month
      bias maps over the period 1985-2014: first the average monthly SST are
      computed. Then, over all 12 maps of biases the RMSEs are calculated. All
      the models are interpolated onto the grid of the refererence HadISST 1.1
      monthly average sea surface temperature (Rayner et al. 2003,
      DOI:10.1029/2002JD002670) Missing values due to non-existing sea areas (in
      the GCM) are coded as -99 (RMSE is strictly positive). ----- Numbers are
      provided in: https://docs.google.com/spreadsheets/d/1xvqc2CtKmi1UOCftX5hTB
      z9ctgRrCHqw5xGAmnNSIiI/edit#gid=0 Area definitions: BNS: Baltic and North
      Sea NBS: Norwegian and Barents Sea NAtl: Nordic Atlantic (replaced by NBS)
      SNA: (Southern) Nord Atlantic MED: Mediterranean (disabled, use Sevault
      MED SST instead.  ) BLK: Black Sea EUR: Europe box Maps are provided in: h
      ttps://docs.google.com/spreadsheets/d/1xvqc2CtKmi1UOCftX5hTBz9ctgRrCHqw5xG
      AmnNSIiI/edit#gid=334563502 R-script reports (PDF files) used for the
      calcualtions are available at
      https://drive.google.com/drive/folders/1MRNO_h6EGcyGs4d82vqtTLyTLtNxHaQ0
    best: 0
    worst: +inf
  period:
    reference: 1985-2014
  plausible_values:
  - min: 0
    max: 2.5
    source: eurocordex_gcm_selection_team
    comment:
      Upper limit: (Mean + 2*sd) of the RMSEs of 29 models, rounded up to the
      next half integer.

```

### Spread of future outcomes
#### AR6 TCR as spread

Located in [CMIP6_studies/AR6.yaml](../CMIP6_studies/AR6.yaml)

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

#### Mindlin21 tropampl

Located in [CMIP6_studies/Mindlin2021.yaml](../CMIP6_studies/Mindlin2021.yaml)

10.1029/2021GL092568

```
- key: Mindlin21 tropampl
  doi: 10.1029/2021GL092568
  type: future_spread
  spatial_scope: Global
  temporal_scope: Annual
  metric:
    name: tropampl
    long_name: Tropical Amplification
    units: K_K-1
    variables: ta250
    comment:
      These metrics are inspired by the work done in Mindlin and Shepherd, 2020,
      Clim Dyn but for CMIP6 GCMs and in Mindlin et al. 2021, GRL. It includes
      29 CMIP6 GCMs for SSP585 and extended to include 37 models Tropical
      warming (TW), the latter evaluated as the long-term change in temperature
      (ta) at 250 hPa zonally averaged between 15°S and 15°N (ΔT trop ) divided
      by the global surface temperature change (ΔT). Here Δ indicates the
      difference between 2070–2099 in the SSP5-8.5 experiment and 1950–1979 in
      the historical experiment. The limit between weak and strong tropical
      warming is not easy to set. We use the value of 1.7 K/K, choosing to have
      only 2 categories
  period:
    reference: 1950-1979
    target: 2070-2099
  classes:
  - limits: [0, 1.7, 10]
    labels: ['weak tropical warming', 'strong tropical warming']
    source: author

```

#### Sch20 ECS

Located in [CMIP6_studies/Sch20.yaml](../CMIP6_studies/Sch20.yaml)

10.5194/esd-11-1233-2020

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

#### Nabat EUR AOD future change

Located in [CMIP6_studies/Nabat.yaml](../CMIP6_studies/Nabat.yaml)

['pers_comm', 'Pierre Nabat']

```
- key: Nabat EUR AOD future change
  doi: ['pers_comm', 'Pierre Nabat']
  type: future_spread
  spatial_scope: EUR
  temporal_scope: Annual
  data_source: author
  metric:
    name: aod_futurechange
    long_name: Future evolution of the European Aerosol Optical Depth
    units: aod
    variables: aod550
    comment:
      Change in Aerosol Optical Depth (AOD) between periods over Europe, annual
      mean Difference in AOD is computed between 2086-2100 (SSP585) and
      2000-2014 (HIST)
  period:
    reference: 2000-2014
    target: 2086-2100
  classes:
  - limits: [-99, -0.04, 0, 99]
    labels: ['strong decrease', 'decrease', 'increase']
    source: author
    comment:


```

#### Oud20 jetposdelta

Located in [CMIP6_studies/Oud20.yaml](../CMIP6_studies/Oud20.yaml)

10.1029/2019GL086695

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
      driven jet position over the period 2080-2099 (ssp585) w.r.t.
      preindustrial 1860-1900
  period:
    reference: 1860-1900
    target: 2080-2099
  classes:
  - limits: [-90, -0.5, 0.5, 90]
    labels: ['strong south change', 'weak change', 'strong north change']
    source: author

```

#### Qasmi Constr EUR Dtas ssp245 2050 JJA

Located in [CMIP6_studies/Qasmi.yaml](../CMIP6_studies/Qasmi.yaml)

10.1126/sciadv.abo6872

```
- key: Qasmi Constr EUR Dtas ssp245 2050 JJA
  doi: 10.1126/sciadv.abo6872
  type: future_spread
  spatial_scope: MED+NEU+CEU
  temporal_scope: JJA
  data_source: author
  metric:
    name: deltatas_class
    long_name: Warming classes according to Observationally-constrained Summer European future surface air temperature change in 2041-2060 in Summer
    units: categorical
    variables: tas
    comment:
      Regional tas change in Europe MED, NEU, CEU, MED+NEU+CEU, DJF, JJA,
      2041-2060 vs 1850-1900, SSP245. Values are given only for land points.
      Adapted from Qasmi and Ribes 2022, Sci. Adv. by S. Qasmi following S.
      Somot's request Numerical values available soon. Only warming classes for
      now. We report here only warming classes for JJA and for the joined
      MED+NEU+CEU domain
  period:
    reference: 1850-1900
    target: 2041-2060
  classes:
  - limits: [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
    labels: ['implausible cold', 'weak warming', 'medium warming', 'strong warming', 'implausible warm']
    source: author
    comment:
      Warming classes are determined wrt an observationally-constrained range
      for the future regional warming based on Ribes et al. 2021, Qasmi et al.
      (in rev). The observational constraint is a global constraint on the GMST
      but it allows to constraint the regional climate warming. The 90% interval
      of future warming plausible range is [2.3 ; 3.3]degC The 50% interval of
      future warming plausible range is [2.5 ; 3.0]degC The best estimate is a
      warming of 2.8 degC Category definition (new since 5 jan 2022): Categories
      1 and 5 are considered as implausible by S. Qasmi. Category 2, 3, 4 are
      plausible. Class 1 is below the Q5 of the constrained range. Class 2 is
      between Q5 and Q25 Class 3 is between Q25 and Q75 Class 4 is between Q75
      and Q95 Class 5 is above Q95

```

#### Atlas Dtas MED DJF

Located in [CMIP6_studies/AtlasIPCC.yaml](../CMIP6_studies/AtlasIPCC.yaml)

['Pers. Comm.', 'Jesus Fernandez']

```
- key: Atlas Dtas MED DJF
  doi: ['Pers. Comm.', 'Jesus Fernandez']
  type: future_spread
  spatial_scope: MED
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

#### Atlas Dtas MED JJA

Located in [CMIP6_studies/AtlasIPCC.yaml](../CMIP6_studies/AtlasIPCC.yaml)

['Pers. Comm.', 'Jesus Fernandez']

```
- key: Atlas Dtas MED JJA
  doi: ['Pers. Comm.', 'Jesus Fernandez']
  type: future_spread
  spatial_scope: MED
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

#### Atlas Dpr MED DJF

Located in [CMIP6_studies/AtlasIPCC.yaml](../CMIP6_studies/AtlasIPCC.yaml)

['Pers. Comm.', 'Jesus Fernandez']

```
- key: Atlas Dpr MED DJF
  doi: ['Pers. Comm.', 'Jesus Fernandez']
  type: future_spread
  spatial_scope: MED
  temporal_scope: DJF
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

#### Atlas Dpr MED JJA

Located in [CMIP6_studies/AtlasIPCC.yaml](../CMIP6_studies/AtlasIPCC.yaml)

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

Located in [CMIP6_studies/Sevault.yaml](../CMIP6_studies/Sevault.yaml)

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

### Other criteria
#### Bru20 mfamily

Located in [CMIP6_studies/Bru20.yaml](../CMIP6_studies/Bru20.yaml)

10.5194/esd-11-995-2020

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

#### Aer. species

Located in [CMIP6_studies/Aerosol.yaml](../CMIP6_studies/Aerosol.yaml)

['pers. comm.', 'Jesus Fernandez']

```
- key: Aer. species
  doi: ['pers. comm.', 'Jesus Fernandez']
  type: other
  spatial_scope: special
  temporal_scope: Annual
  data_source: author
  metric:
    name: aer_species
    long_name: Aerosol species for which AOD available at ESGF
    units: categorical
    variables: od550bb, od550bc, od550dust, od550no3, od550oa, od550so4, od550ss, od550so4so, aerasymbnd, aeroptbnd, aerssabnd
    comment:
      Data extracted from ESGF using  https://github.com/jesusff/cmip6-for-
      cordex/blob/main/util/aerosol_species.py which feeds from
      https://github.com/jesusff/cmip6-for-cordex/blob/main/CMIP6_for_CORDEX.py
      Also, some pers. comm. for certain models that do not provide AOD by
      aerosol species. S. Yang for the EC-Earth consortium models.
    best: bb, bc, dust, no3, oa, so4, ss, so4so, aerasymbnd, aeroptbnd, aerssabnd

```

#### Bra21 complexity

Located in [CMIP6_studies/Bra21.yaml](../CMIP6_studies/Bra21.yaml)

10.5194/gmd-2020-418

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

#### Calendar

Located in [CMIP6_studies/Calendar.yaml](../CMIP6_studies/Calendar.yaml)

['pers. comm.', 'Andreas Dobler']

```
- key: Calendar
  doi: ['pers. comm.', 'Andreas Dobler']
  type: other
  spatial_scope: special
  temporal_scope: Annual
  data_source: author
  metric:
    name: calendar
    long_name: Model calendar
    units: categorical
    variables: None
    comment:
      Data extracted from ESGF

```

#### atm. res. km

Located in [CMIP6_studies/Resolution.yaml](../CMIP6_studies/Resolution.yaml)

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

