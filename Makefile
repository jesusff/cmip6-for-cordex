default:
	echo "You probably want to 'make update'"

update: update-esgf update-tables

update-esgf:
	python3 CMIP6_for_CORDEX.py

update-tables: AUS EUR

AUS:
	python3 CMIP6_studies_table.py AUS
	python3 CMIP6_studies_list.py AUS > CMIP6_studies_list_AUS.md
EUR:
	python3 CMIP6_studies_table.py EUR
	python3 CMIP6_studies_list.py EUR > CMIP6_studies_list_EUR.md
SEA:
	python3 CMIP6_studies_table.py SEA
	python3 CMIP6_studies_list.py SEA > CMIP6_studies_list_SEA.md
