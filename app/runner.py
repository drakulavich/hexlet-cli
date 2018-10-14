import argparse

from app import weather_lib


def run():
    parser = argparse.ArgumentParser(description='Get current weather from CLI',
                                     prog='weather', usage='%(prog)s [city_name]')
    parser.add_argument('city')
    args = parser.parse_args()

    try:
        print(weather_lib.get_forecast(args.city))
    except (LookupError, AssertionError) as e:
        print(e)
        exit(1)
