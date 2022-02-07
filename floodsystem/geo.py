# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from haversine import haversine, Unit

from floodsystem.utils import sorted_by_key  # noqa

def stations_by_distance(stations, p):
    distances = []
    for station in stations:
        distances.append((station.name, station.town, haversine(station.coord, p)))
    return sorted_by_key(distances, 2)

def rivers_with_station(stations):                  
    river_stations = set()
    unique_rivers = []
    for j in stations:
        if j.name != None:
            river_stations.add(j.river)
    for x in river_stations:
        unique_rivers.append(x)
    
    return unique_rivers

#return dictionary that maps river names (‘key’) to a list of station objects on a given river
def stations_by_river(stations):                  
    station_locations = {}
    stations_of_all_rivers = {}
    for k in stations:
        station_locations[k.name] = k.river
    for q in rivers_with_station(stations):
        stations_of_a_river = []
        for s, r in station_locations.items():
            if r == q:
                stations_of_a_river.append(s)
        stations_of_a_river.sort()
        stations_of_all_rivers[q] = stations_of_a_river
    return stations_of_all_rivers

def stations_within_radius(stations, centre, r):
    stations_centre = stations_by_distance(stations, centre)
    stations_satisfied = []
    if r < 0:
        raise ValueError("ValueError")

    for i in stations_centre:
        if i[2] <= r:
            stations_satisfied.append(i[0])
        else:
            break
    return stations_satisfied

#1E
def rivers_by_station_number(stations, N):
    tuples_rivers_stationCount = []
    stations_of_each_river = stations_by_river(stations)
    for river in stations_of_each_river:
        tuples_rivers_stationCount.append((river, len(stations_of_each_river[river])))

    sorted_tuples = sorted_by_key(tuples_rivers_stationCount, 1)
    tuples_rivers_stationCount = sorted_tuples
    i = 0
    m = N
    rivers_with_most_stations = []
    for j in range(len(tuples_rivers_stationCount)):
       rivers_with_most_stations.append(tuples_rivers_stationCount[-(j+1)]) 
    while i < 1:
        if rivers_with_most_stations[m-1][1] == rivers_with_most_stations[m][1]:
            m = m + 1
        else:
            break
        if m >= len(rivers_with_most_stations):
            break
    return rivers_with_most_stations[:m]
