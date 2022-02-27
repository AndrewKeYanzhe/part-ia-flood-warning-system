from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list


def run():
    stations = build_station_list()
    result_stations = stations_level_over_threshold(stations, 0.8)
    for station in result_stations:
        print(station)

    # print(stations)


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
