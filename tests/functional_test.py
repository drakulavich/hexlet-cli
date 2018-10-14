import httpretty

from app import weather_lib
from tests.test_data import data_path, read_file

WEATHER_OUTPUT_FILE: str = data_path('api', 'weather.json')
CITY_OUTPUT_FILE: str = data_path('api', 'city.json')


@httpretty.activate
def test_get_weather():

    httpretty.register_uri(
        httpretty.GET,
        weather_lib.API_CITY_ID_URL.format('minsk'),
        body=read_file(CITY_OUTPUT_FILE)
    )

    httpretty.register_uri(
        httpretty.GET,
        weather_lib.API_CITY_WEATHER_URL.format('834463'),
        body=read_file(WEATHER_OUTPUT_FILE)
    )

    expected_result = (
        'Current: 15.23 °C\n'
        'Min: 3.54 °C\n'
        'Max: 15.95 °C\n'
        'Wind speed: 4.2 m/s\n'
        'Humidity: 81 %\n'
        'Air pressure: 1025.0 mbar'
    )
    assert str(weather_lib.get_forecast('minsk')) == expected_result
