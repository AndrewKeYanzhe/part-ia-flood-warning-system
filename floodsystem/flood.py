from floodsystem.station import MonitoringStation
from floodsystem.stationdata import update_water_levels
from floodsystem.utils import sorted_by_key



def stations_level_over_threshold(stations, tol):
    "Returns a list of stations with relative water level higher than tolerance"
    update_water_levels(stations)
    water_level_list = []  
    for station in stations:
        if not station.relative_water_level():
            pass
        elif station.relative_water_level() > tol:
            water_level_list.append((station.name, station.relative_water_level()))
            # if station.name == "Letcombe Bassett":
            #     print(station)
            #     print(station.latest_level)
    return sorted_by_key(water_level_list, 1, reverse=True)

def stations_highest_rel_level(stations, N):
    N_stations_list = []
    update_water_levels(stations)
    for station in stations:
        if station.relative_water_level() is not None:
            N_stations_list.append((station.name, station.relative_water_level()))
    N_stations_list = sorted_by_key(N_stations_list, 1, reverse = True)
    return N_stations_list[:N]


def stations_highest_rel_level2(stations, N):
    stations_list = []
    update_water_levels(stations)
    for station in stations:
        if station.relative_water_level() is not None:
            stations_list.append((station.name, station.relative_water_level()))
    stations_list = sorted_by_key(stations_list, 1, reverse = True)
    listID = []
    for datas in stations_list:
        listID.append(datas[0])
    return list[:N]