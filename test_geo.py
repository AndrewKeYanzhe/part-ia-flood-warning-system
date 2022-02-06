from haversine import haversine

from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_distance



s_id1 = "test_s_id1"
m_id1 = "test_m_id1"
label1 = "station1"
coord1 = (0.0, 1.0)
trange1 = (3.4, 1.2)
river1 = "x1"
town1 = "a1"

s_id2 = "test_s_id2"
m_id2 = "test_m_id2"
label2 = "station2"
coord2 = (0.0, 0.0)
trange2 = (0.4, 1.2)
river2 = "x2"
town2 = "a2"

s_id3 = "test_s_id3"
m_id3 = "test_m_id3"
label3 = "station3"
coord3 = (2.0, 0.0)
trange3 = (10, 2.4)
river3 = "x3"
town3 = "a3"

a = MonitoringStation(s_id1, m_id1, label1, coord1, trange1, river1, town1)
b = MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)
c = MonitoringStation(s_id3, m_id3, label3, coord3, trange3, river3, town3)

test_stations = [a, b, c]


def test_stations_by_distance():
    distance = stations_by_distance(test_stations, (0.0, 0.0))
    assert distance == [('station2', 'a2', 0.0),
                        ('station1', 'a1', haversine((0.0, 0.0), (0.0, 1.0))),
                        ('station3', 'a3', haversine((2.0, 0.0), (0.0, 0.0)))]

# test_stations_by_distance()

def test_rivers_with_station():
    rivers_with_stations = rivers_with_station(test_stations)
    assert rivers_with_stations == ["x1", "x2", "x3"]


def test_stations_by_river():
    stations_of_rivers = stations_by_river(test_stations)
    assert stations_of_rivers == {"x3": ["station3"], "x2": ["station2"], "x1": ["station1"]}