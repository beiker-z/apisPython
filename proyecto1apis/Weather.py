import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from requests.exceptions import HTTPError

"""
@author: Keneth Sical
"""


class Weather:

    def __init__(self):
        self.json = dict()

    def get_temperature(self, latitude: float, longitude: float):
        url = "https://api.open-meteo.com/v1/forecast?latitude={0}&longitude={1}&hourly=temperature_2m&current_weather=true&temperature_unit=fahrenheit&timezone=auto&past_days=7".format(
            latitude, longitude)
        response = requests.get(url=url)
        response.raise_for_status()
        self.json = response.json()
        return self.json["current_weather"]

    def get_graphic(self):
        hourly = self.json["hourly"]
        time = hourly["time"]
        time_np = np.array(time, dtype='datetime64')
        temperature = hourly["temperature_2m"]
        fig, ax = plt.subplots()
        ax.plot(time_np, temperature)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))
        return fig


weather = Weather()
try:
    current_weather = weather.get_temperature(39.76, -98.50)
    print("Zona Horaria:", weather.json["timezone"])
    print("Temperatura:", current_weather["temperature"])
    fig = weather.get_graphic()
    fig.show()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
