import json
from urllib.request import urlopen
  
url = "https://raw.githubusercontent.com/WCRP-CMIP/CMIP6_CVs/master/CMIP6_source_id.json"
  
response = urlopen(url)
data_json = json.loads(response.read())
sid = data_json['source_id']
print(
  '\n'
  .join([f'    {k}: {sid[k]["model_component"]["atmos"]["native_nominal_resolution"]}' for k in sid if "ScenarioMIP" in sid[k]["activity_participation"]])
  .replace('none','')
  .replace(' km', '')
)
