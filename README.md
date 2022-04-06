# A Coarse Location-Service for Collaborating with Approximately Nearest Neighbors
This GitHub repository contains the source code of the bachelor thesis "A Coarse Location-Service for Collaborating with Approximately Nearest Neighbors".

## Service implementation: `/service`

### Requirements
- we recomend to first create an virtual environment  (virtualenv)
- Python 3.8.
- PostgreSQL 12.9 database running on port 5432 with:
	- NAME: mydatabase
	- USER: flo
	- PASSWORD: mypassword
	(you can also update the server settings to your database configuration in `service/server/neighborhood/settings.py`)


### Starting our service
1. clone the project
2. start virtual environment
3. go to `/service`
4.  install packages with `$ pip install -r requirements.txt`
5. go to `/service/server`
6. start the server with `$ python3 manage.py runserver`
7. sever sould be live at http://127.0.0.1:8000/


## Experiments: `/experiments`
Experiments for measuring execution time of considering if two users are neighours.

## /setupgeohash/main.py:
Experiment with algorithm of our service using Geohashes.

## /setuplonglat/main.py:
Experiment with algorithm calculating the distance between two user longitude-latitude -coordinates and compare it to a predefined threshold for considering if the two users are neighbours.
