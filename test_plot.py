from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import *
import datetime


def test_plot_water_levels():

    stations = build_station_list()
    dt = 10
    tuples_riskiest_stations = stations_highest_rel_level(stations, 5)

    names_riskiest_stations = [item[0] for item in tuples_riskiest_stations]
    print(names_riskiest_stations)

    riskiest_stations = []
    for station in stations:
        if station.name in names_riskiest_stations:
            riskiest_stations.append(station)
        
        if len(riskiest_stations) == 5:
            break
    
    for station in riskiest_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)
# test_plot_water_levels()