# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town



from floodsystem.station import inconsistent_typical_range_stations

s_id2 = "test-s-id2"
m_id2 = "test-m-id2"
label2 = "station2"
coord2 = (-2.0, 4.0)
trange2 = (-2.3, 3.4445)
river2 = "River2"
town2 = "Town2"
s2 = MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)

s_id3 = "test-s-id3"
m_id3 = "test-m-id3"
label3 = "station3"
coord3 = (2.0, 4.0)
trange3 = (5.3, 3.4445)
river3 = "River3"
town3 = "Town3"
s3 = MonitoringStation(s_id3, m_id3, label3, coord3, trange3, river3, town3)

s_id4 = "test-s-id4"
m_id4 = "test-m-id4"
label4 = "station4"
coord4 = (2.0, 0.0)
trange4 = (5, 5)
river4 = "River4"
town4 = "Town4"
s4 = MonitoringStation(s_id4, m_id4, label4, coord4, trange4, river4, town4)


def test_typical_range_consistent():
    condition1 = MonitoringStation.typical_range_consistent(s2)
    condition2 = MonitoringStation.typical_range_consistent(s3)
    condition3 = MonitoringStation.typical_range_consistent(s4)
    assert condition1 == False
    assert condition2 == True
    assert condition3 == False


def test_inconsistent_typical_range_stations():
    conditions = [MonitoringStation.typical_range_consistent(s2),
                 MonitoringStation.typical_range_consistent(s3),
                 MonitoringStation.typical_range_consistent(s4)]
    test = inconsistent_typical_range_stations(conditions)
    assert test == ['station2', 'station4']

