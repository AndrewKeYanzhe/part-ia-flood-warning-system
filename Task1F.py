from floodsystem.stationdata import build_station_list
from floodsystem.station import *

def run():
    stations = build_station_list()
    print(inconsistent_typical_range_stations(stations))


if __name__ == "__main__":
    print("*** Task 1: CUED Part IF Flood Warning System ***")
    run()