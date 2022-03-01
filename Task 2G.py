from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

stations = build_station_list()

def risk(stations):
    update_water_levels(stations)
    severe = set()
    high = set()
    moderate = set()
    low = set()
    for station in stations:
        h = station.relative_water_level()
        if h is None:
            pass
        elif h > 2.0 and station.town is not None:
            severe.add(station.town)
        elif h > 1.5 and h < 2.0 and station.town is not None:
            high.add(station.town)
        elif h > 1.0 and h < 1.5 and station.town is not None:
            moderate.add(station.town)
        elif h < 1.0 and station.town is not None:
            low.add(station.town)
    return severe, high, moderate, low


severe, high, moderate, low = risk(stations)

print("Severe risk of flooding \n", severe)
print("High risk of flooding \n", high)
print("Moderate risk of flooding \n", moderate)
print("Low risk of flooding \n", low)
