import pandas as pd
import matplotlib.pyplot as plt
from weather_analysis import log, readCsv


DATASET_PATH = r"C:\Users\behar\Desktop\Github\Python\Weather Analysis\weather_data.csv"

if __name__ == '__main__':
    weatherData = readCsv(DATASET_PATH)
    log(
        f'🌹  Unique Values of a Column:\n{weatherData["Weather"].unique()}')
    plt.hist(weatherData['Weather'])
    plt.show()
