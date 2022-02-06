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