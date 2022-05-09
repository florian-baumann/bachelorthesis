# A Coarse Location-Service for Collaborating with Approximately Nearest Neighbors
This GitHub repository contains the source code of the bachelor thesis "A Coarse Location-Service for Collaborating with Approximately Nearest Neighbors".

## Service implementation: `/service`

### Requirements
- Docker=20.10.13


### Starting our service
1. clone the project
2. go to the folder `/service/server`
3. build and start docker containers with `$ docker-compose up`
4. sever sould be live at http://localhost:8000/


## Experiments: `/experiments`
Experiments for measuring execution time of considering if two users are neighours.

## /setupgeohash/main.py:
Experiment with algorithm of our service using Geohashes.

## /setuplonglat/main.py:
Experiment with algorithm calculating the distance between two user longitude-latitude -coordinates and compare it to a predefined threshold for considering if the two users are neighbours.
