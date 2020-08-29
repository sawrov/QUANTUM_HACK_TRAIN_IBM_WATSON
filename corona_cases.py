import json
import requests

url="https://api.covid19api.com/countries"
response=requests.request("GET",url)
info=json.loads(response.text)
for country in info:
	if country['Country'] == "Nepal":
		print (country['Slug'])
		break;