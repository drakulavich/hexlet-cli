import os
import json
from tests.test_data import resource_path

from app import main


WEATHER_OUTPUT_FILE: str = os.path.join(resource_path('api'), 'weather.json')


def test_formatter():
    with open(WEATHER_OUTPUT_FILE) as json_data:
        d = json.load(json_data)

    assert main.format_output(d) =='Weather in Minsk:\nCurrent: 15.23 °C\nMin: 3.54 °C\nMax: 15.95 °C\nWind speed: 4.2 m/s\nHumidity: 81 %\nAir pressure: 1025.0 mbar'
