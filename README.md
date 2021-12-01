[![Visit website view](https://img.shields.io/badge/www-Website%20view-f39f37)](https://jesusff.github.io/cmip6-for-cordex)
[![EUR table](https://img.shields.io/badge/table-EUR-4078c0)](https://jesusff.github.io/cmip6-for-cordex/CMIP6_studies_table_EUR.html)
[![AUS table](https://img.shields.io/badge/table-Other-4078c0)](https://jesusff.github.io/cmip6-for-cordex/CMIP6_studies_table_AUS.html)
[<img align="right" width="200" src="https://github.com/jesusff/test/blob/master/micin-aei-cordys_en.png?raw=true">](https://meteo.unican.es/en/cordys)

CMIP6 input data for CORDEX
===========================

Collection of information in support of the selection of driving Global Climate Models from CMIP6 for CORDEX.
There are two main components:

 1. An automatic search for data availability in the ESGF ([CMIP6_for_CORDEX_availability_ESGF.csv](./CMIP6_for_CORDEX_availability_ESGF.csv)), plus a manual collection of boundaries available directly from the producers ([CMIP6_for_CORDEX_availability_non_ESGF.csv](./CMIP6_for_CORDEX_availability_non_ESGF.csv))
 2. A manual collection of published results ([CMIP6_studies](./CMIP6_studies)) regarding the plausibility, spread of future outcomes and independence of the CMIP6 models.

Data availability
-----------------

Parse ESGF metadata to discover CMIP6 model runs meeting the criteria for
downscaling. In table [CMIP6_for_CORDEX_availability_ESGF.csv](./CMIP6_for_CORDEX_availability_ESGF.csv),
each model run and scenario is tagged according to the availability of 
enough variables to drive a Regional Climate Model (**RCM**), to provide typical
predictors for Empirical-Statistical Downscaling (**ESD**) or for **Basic**
analyses (currenly meaning that daily precipitation and near-surface mean
temperature are available)

### Usage


```
python3 CMIP6_for_CORDEX.py
```

Does the search and builds a csv table ([CMIP6_for_CORDEX_availability_ESGF.csv](./CMIP6_for_CORDEX_availability_ESGF.csv)) tagging each
simulation depending on the variables available in ESGF.

CMIP6 studies
-------------

These are collected as YAML files under [CMIP6_studies](./CMIP6_studies) and summarized e.g. in [CMIP6_studies_list_EUR.md](./CMIP6_studies_list_EUR.md). The information from all sources is merged in the [CMIP6_studies_table_EUR.csv](./CMIP6_studies_table_EUR.csv), which are rendered as HTML in [https://jesusff.github.io/cmip6-for-cordex](https://jesusff.github.io/cmip6-for-cordex)
