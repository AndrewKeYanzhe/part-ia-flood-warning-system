import matplotlib.pyplot as plt

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

