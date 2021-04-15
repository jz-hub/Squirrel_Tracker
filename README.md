# Squirrel_Tracker(WIP)

Final Project for Tools for Analytics.

Created by: Jackie Zhang, Guanchao Qi

## Description
This website is aiming to track all the known squirrels, starting with Central Park in New York City. We firstly imported [2018 Central Park Squirrel Census](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw).
The website also allows users to add, update and view squirrel data. 


## Group Info

Group Name: Group 48

## UNI Info
UNIS: [wz2519, gq2146]

## Commands
### Import Data
```bash
$ python3 manage.py import_squirrel_data /path/to/file.csv
```
### Export Data
```bash
$ python3 manage.py import_squirrel_data /path/to/file.csv
```
## Explaination of Pages
`/map/base`: Home page of our website

`/map`: Map view of sightings of 80 squirrels (Could be all 3000+ squirrels, but it would be too crowded)

`/sightings/all`: All identified squirrels with their unique attribuets

`/sightings/add`: To add a new squirrel if necessary

`/sightings/stats`: Some fun statistics about squirrels
