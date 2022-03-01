from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stationsId_highest_rel_level


def run():
    stations = build_station_list()
    highest = stationsId_highest_rel_level(stations, 5)
    dt = 2
    for station in highest:
        data = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_fit(station, data[0], data[1], 4)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()