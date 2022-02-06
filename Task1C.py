from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    stations = build_station_list()
    p = (52.2053, 0.1218)
    r = 10
    radius = stations_within_radius(stations, p, r)
    radius.sort()
    print(radius)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()