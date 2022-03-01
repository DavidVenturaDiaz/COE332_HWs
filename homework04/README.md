# Meteorite Landings Analysis Container

## Overview
The following github repository contains the files utilized in the analysis of meteorite landings. In order to understand the data collected by a rover, the data must be analyzed to obtain crucial information about such exploration. This is achieved by using the python script contained in this repository.

## Files
This repository contains the following files:
### Dockerfile
This file was utilized to create a contained in Docker Hub using the files in the current repository
### ml_data_analysis.py
This python script is used to analyze the data of meteorite landings. This script takes a json file as an input, and this json file contains a list of dictionaries. This script outputs the average mass of the meteorites, their hemisphere, and their class 

## Docker Hub
### Pull Existing Image on Docker Hub
In order to pull the existing image in Docker Hub , which was created using the files in this repository, you can run the following:
`docker pull davidventuradiaz/hw04:1.0`  
