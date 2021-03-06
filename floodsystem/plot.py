import matplotlib.pyplot as plt
import matplotlib
from floodsystem.analysis import polyfit

#need to install matplotlib in a vanilla python environment

def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)
    plt.xlabel('Date')
    plt.ylabel('Water Level/m')
    plt.title(station.name)
    typical_low = []
    typical_high = []
    for i in range(0, len(dates)):
        typical_low.append(station.typical_range[0])
        typical_high.append(station.typical_range[1])
    plt.plot(dates, typical_low, label = "Typical Low")
    plt.plot(dates, typical_high, label = "Typical High")
    plt.xticks(rotation = 45)
    plt.tight_layout()

    plt.show()



def plot_water_level_with_fit(station, dates, levels, p):

   if len(dates) != 0 and len(levels) != 0:
       dates = matplotlib.dates.date2num(dates)
       dates = dates - dates[0]
       poly, d0 = polyfit(dates, levels, p)
       

       plt.plot(dates, levels, label="water level")
       plt.plot(dates, poly(dates), label="best-fit polynomial")
       plt.xlabel('Date')
       plt.ylabel('Water Level(m)')
       plt.title(station.name)
       typical_low = []
       typical_high = []
       for i in range(0, len(dates)):
           typical_low.append(station.typical_range[0])
           typical_high.append(station.typical_range[1])
       plt.plot(dates, typical_low, label="Typical Low")
       plt.plot(dates, typical_high, label="Typical High")
       plt.legend()
       plt.xticks(rotation=45)
       plt.tight_layout()

       plt.show()

   else:
       # if the list is empty (the data of a station is incorrect), plot an empty chart
       plt.plot(dates, levels)
       plt.xlabel('Date')
       plt.ylabel('Water Level/m')
       plt.title(station.name)
       typical_low = []
       typical_high = []
       for i in range(0, len(dates)):
           typical_low.append(station.typical_range[0])
           typical_high.append(station.typical_range[1])
       plt.plot(dates, typical_low, label="Typical Low")
       plt.plot(dates, typical_high, label="Typical High")
       plt.xticks(rotation=45)
       plt.tight_layout()

       plt.show()

