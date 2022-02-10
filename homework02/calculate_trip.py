import json
import math

mars_radius = 3389.5    # km
max_speed = 10          #km/hr

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )

def calc_time(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float):
    travel_time = (calc_gcd(latitude_1, longitude_1, latitude_2, longitude_2)) / max_speed
    return(travel_time)

def map_trip(a_list_of_dicts):
    total_time = 0.0
    trav_time = []
    samp_time = []
    trav_time.append(calc_time(16.0, 82.0, float(ms_data['meteorite_sites'][0]['northlat']), float(ms_data['meteorite_sites'][0]['eastlon'])))
    for i in range(1,5):
	trav_time.append(calc_time(float(ms_data['meteorite_sites'][i-1]['northlat']),float(ms_data['meteorite_sites'][i-1]['eastlon']),float(ms_data['meteorite_sites'][i]['northlat']),float(ms_data['meteorite_sites'][i]['eastlon'])))


with open('meteorite_sites.json', 'r') as f:
    ms_data = json.load(f)

map_trip(ms_data)
