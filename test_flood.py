from floodsystem.station import MonitoringStation
from floodsystem.stationdata import update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list

from floodsystem.flood import *

def test_stations_level_over_threshold():
    stations = build_station_list()
    result_stations = stations_level_over_threshold(stations, 0.8)

    # originally intended to assert values, but then realised that this is not possible. this function calls update_water_levels in "stationdata.py" which resets latest_level to "none" if realtime dataset does not contain data for that station

    #hence the function is simply called to see if it runs
test_stations_level_over_threshold()