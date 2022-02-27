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