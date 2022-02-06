from floodsystem.geo import *
from floodsystem.stationdata import build_station_list


def run():
    stations = build_station_list()

    river_stations = rivers_with_station(stations)
    river_stations.sort()

    print(len(river_stations), river_stations[:10])
    stations_of_rivers = stations_by_river(stations)

    print("River Aire \n ", stations_of_rivers["River Aire"])
    print("River Cam \n ", stations_of_rivers["River Cam"])
    print("River Thames \n ", stations_of_rivers["River Thames"])


if __name__ == "__main__":
    run()
