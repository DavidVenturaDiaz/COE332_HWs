# Meteorite Landings Deployed in Kubernetes

## Overview
The current directory containst the files required to deploy the meteorite landings data in Kubernetes. Furthermore, instructions on how to deploy it is provided to the user below.

## Files
### Dockerfile
This dockerfile contains the instructions needed to build the Docker image to run the Flask app alongside using a Redis database to store the data and retrieve it.

### app.py
The file "app.py" contains the python script that builds the Flask application that allows the user to interact with the Redis database. This Flask application utilizes a POST request to load in the Meteorite Landings. The user can use the POST request by typing the following: curl 127.0.0.1:5035/data/load The Flask application also contains a GET request that displays the Meteorite Landings data in JSON format. The user can use the GET request by typing the following: curl 127.0.0.1:5035/data/display


