import matplotlib
import numpy as np

def polyfit (dates, levels, p):

    dates = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(dates,levels,p)
    poly = np.poly1d(p_coeff)

    return poly, dates[0]
