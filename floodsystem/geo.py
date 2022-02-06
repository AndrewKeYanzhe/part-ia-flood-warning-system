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

