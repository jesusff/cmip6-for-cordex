[![MyBinder](https://img.shields.io/badge/launch-MyBinder-33cc33)](https://mybinder.org/v2/gh/jesusff/pyclimenv/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252FWCRP-CORDEX%252Fcmip6-for-cordex%26urlpath%3Dlab%252Ftree%252Fcmip6-for-cordex%252F%26branch%3Dmain)

CMIP6 input data for CORDEX
===========================

Collection of information in support of the selection of driving Global Climate Models from CMIP6 for CORDEX.
There are two main components:

 1. An automatic search for data availability in the ESGF ([CMIP6_for_CORDEX_availability_ESGF.csv](./docs/CMIP6_for_CORDEX_availability_ESGF.csv)), plus a manual collection of boundaries available directly from the producers ([CMIP6_for_CORDEX_availability_non_ESGF.csv](./CMIP6_for_CORDEX_availability_non_ESGF.csv))
 2. A manual collection of published results ([CMIP6_studies](./CMIP6_studies)) regarding the plausibility, spread of future outcomes and independence of the CMIP6 models.

Data availability
-----------------

Parse ESGF metadata to discover CMIP6 model runs meeting the criteria for
downscaling. In table [CMIP6_for_CORDEX_availability_ESGF.csv](./docs/CMIP6_for_CORDEX_availability_ESGF.csv),
each model run and scenario is tagged according to the availability of 
enough variables to drive a Regional Climate Model (**RCM**), to provide typical
predictors for Empirical-Statistical Downscaling (**ESD**) or for **Basic**
analyses (currenly meaning that daily precipitation and near-surface mean
temperature are available)

CMIP6 studies
-------------

These are collected as YAML files under [CMIP6_studies](./CMIP6_studies) and summarized e.g. in [CMIP6_studies_list_EUR.md](./docs/CMIP6_studies_list_EUR.md). The information from all sources is merged in the [CMIP6_studies_table_EUR.csv](./docs/CMIP6_studies_table_EUR.csv), which are rendered as HTML in [https://wcrp-cordex.github.io/cmip6-for-cordex](https://wcrp-cordex.github.io/cmip6-for-cordex)

Credits
-------
This is an outcome of the EURO-CORDEX Task Team on the CMIP6 GCM/RCM-ESD ensemble design.

> [<img align="right" width="200" src="https://github.com/AEI-CORDyS/AEI-CORDyS.github.io/blob/main/micin-aei-cordys_en.png?raw=true">](https://meteo.unican.es/en/cordys)
The development of this repository was supported by project CORDyS (PID2020-116595RB-I00) funded by MCIN/AEI/10.13039/501100011033 (Spanish Ministry of Science and Innovation / National Reseach Agency).

