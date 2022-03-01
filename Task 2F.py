from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import *


def run():
    stations = build_station_list()
    # highest = stations_highest_rel_level2(stations, 5)
    highest = stations_highest_rel_level(stations, 5)
    dt = 2
    print(highest)


    #convert list of tuples of station_name, level to list of station objects
    riskiest_stations = []
    for station_tuple in highest:    
        for station in stations:
                if station.name == station_tuple[0]:
                    riskiest_stations.append(station)
                    break
    print(len(riskiest_stations))
    print(riskiest_stations)

    for station in riskiest_stations:
        data = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_fit(station, data[0], data[1], 4)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()