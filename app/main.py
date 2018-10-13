import requests


API_CITY_ID_URL = 'https://www.metaweather.com/api/location/search/?query={}'
API_CITY_WEATHER_URL = 'https://www.metaweather.com/api/location/{}'

OUTPUT = """Weather in {city}:
Current: {current_temp:.2f} °C
Min: {min_temp:.2f} °C
Max: {max_temp:.2f} °C
Wind speed: {wind_speed:.1f} m/s
Humidity: {humidity} %
Air pressure: {air_pressure:.1f} mbar"""


def get_city_info(city):
    r = requests.get(API_CITY_ID_URL.format(city))

    data = r.json()
    if data:
        # return first result found
        return r.json()[0]
    else:
        return None


def get_weather_by_city_id(city_id):
    r = requests.get(API_CITY_WEATHER_URL.format(city_id))

    return r.json()


def format_output(weather_payload):
    d = weather_payload['consolidated_weather'][0]

    return (OUTPUT.format(
        city=weather_payload['title'],
        current_temp=d['the_temp'],
        min_temp=d['min_temp'],
        max_temp=d['max_temp'],
        wind_speed=d['wind_speed'],
        humidity=d['humidity'],
        air_pressure=d['air_pressure']
    ))
