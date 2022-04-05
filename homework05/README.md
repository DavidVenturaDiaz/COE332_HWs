# Meteorite Landings Redis Database

## Overview
The following repository contains the files required to set up a Redis database that contains the meteorite landings data. Paired with Flask, the user can also send POST and GET requests to interact with the database.

## Files 
### app.py
The file "app.py" contains the python script that builds the Flask application that allows the user to interact with the Redis database. 
This Flask application utilizes a POST request to load in the Meteorite Landings. The user can use the POST request by typing the following:
`curl 127.0.0.1:5035/data/load`
The Flask application also contains a GET request that displays the Meteorite Landings data in JSON format. The user can use the GET request by typing the following:
`curl 127.0.0.1:5035/data/display`

### Dockerfile
The Dockerfile in this repository contains the instructions necessary to build the Docker image to run the Flask app alongside using a Redis database to store the data and retrieve it.

## Meteorite Landings Data
Although the Meteorite Landings Data is not included in the current repository, such data can be found in the following link:
`https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json`
Note that it is not required to download the data since the python script automatically loads it in when the user utilzes the POST request.

## Redis
The Redis database utilized for this Flask app automatically saves the data once every second, and stores the data permanetely such that if the Redis database is closed, the data stored is not lost. This was achieved using the following command:
`docker run -d -p 6379:6435 -v $(pwd)/data:/data:rw --name=david-redis redis:6 --save 1 1`
