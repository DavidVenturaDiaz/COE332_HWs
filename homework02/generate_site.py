import json
import random

def populate_sites(a_list_of_dicts):
    for i in range(5):
        a_list_of_dicts['meteorite_sites'].append({})
    latitude_and_longitude(a_list_of_dicts)
    meteorite_composition(a_list_of_dicts) 

def latitude_and_longitude(a_list_of_dicts):
    for i in range(5):
        a_list_of_dicts['meteorite_sites'][i]['northlat'] = random.uniform(16.0,18.0)
        a_list_of_dicts['meteorite_sites'][i]['eastlon'] = random.uniform(82.0,84.0)

def meteorite_composition(a_list_of_dicts):
    meteo_comp = ["stony", "iron", "stony-iron"]
    for i in range(5):
        a_list_of_dicts['meteorite_sites'][i]['meteoriteComp'] = random.choice(meteo_comp)

meteorite_site = {'meteorite_sites': []}
populate_sites(meteorite_site)

with open('meteorite_sites.json', 'w') as out:
    json.dump(meteorite_site, out, indent=2)
