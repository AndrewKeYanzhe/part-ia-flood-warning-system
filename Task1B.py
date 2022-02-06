from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():
    stations = build_station_list()
    p = (52.2053, 0.1218)
    distances = stations_by_distance(stations, p)
    print("The closest stations are: ", distances[:10])
    print("The furthest stations are: ", distances[-10:])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
