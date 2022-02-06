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