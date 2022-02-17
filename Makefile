default:
	echo "You probably want to 'make update'"

update: update-esgf update-tables

update-esgf:
	python3 CMIP6_for_CORDEX.py

update-plans:
	python3 CMIP6_downscaling_plans_tables.py
	python3 CORDEX_CMIP6_experiments.py
	cd util; python3 CMIP6_matrix.py

update-tables: AUS EUR MED SEA

AUS:
	python3 CMIP6_studies_table.py AUS
	python3 CMIP6_studies_list.py AUS > CMIP6_studies_list_AUS.md
EUR:
	python3 CMIP6_studies_table.py EUR
	python3 util/row_tooltips.py
	python3 CMIP6_studies_list.py EUR > CMIP6_studies_list_EUR.md
MED:
	python3 CMIP6_studies_table.py MED
	python3 CMIP6_studies_list.py MED > CMIP6_studies_list_MED.md
SEA:
	python3 CMIP6_studies_table.py SEA
	python3 CMIP6_studies_list.py SEA > CMIP6_studies_list_SEA.md
