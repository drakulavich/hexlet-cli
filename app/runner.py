import argparse

from app import main


def run():
    parser = argparse.ArgumentParser(description='Get current weather from CLI',
                                     prog='weather', usage='%(prog)s [city_name]')
    parser.add_argument('city')
    args = parser.parse_args()

    city_info = main.get_city_info(args.city)
    if city_info:
        stdout = main.format_output(main.get_weather_by_city_id(city_info['woeid']))
        print(stdout)
