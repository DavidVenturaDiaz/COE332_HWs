from flask import Flask
from urllib.request import urlopen
import redis
import json

app = Flask(__name__)

def get_redis_client():
    return redis.Redis(host='172.17.0.26', port=6379, db=0)

@app.route('/data/load', methods=['POST'])
def load_data():
    url = 'https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json'
    response = urlopen(url)
    meteorite_landing_data = json.loads(response.read())
   
    get_redis_client()
    rd.set('meteo_land', json.dumps(meteorite_landing_data))

@app.route('/data/display', methods=['GET'])
def display_data():
    get_redis_client()
    json.loads(rd.get('meteo_land'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
