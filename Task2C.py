from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list


def run():
    stations = build_station_list()
    riskiest_stations = stations_highest_rel_level(stations, 10)
    for station in riskiest_stations:
        print(station)


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
