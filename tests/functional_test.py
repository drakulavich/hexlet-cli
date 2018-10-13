from app import main


def test_get_city_info_by_name():
    payload = main.get_city_info('minsk')
    assert payload['title'] == 'Minsk'
    assert payload['location_type'] == 'City'
    assert payload['woeid'] == 834463


def test_get_city_info_by_name_not_existed():
    payload = main.get_city_info('hexlet')
    assert payload is None


def test_get_weather_by_city_id():
    payload = main.get_weather_by_city_id(834463)

    assert len(payload['consolidated_weather']) > 1
    assert payload['parent']['title'] == 'Belarus'

    summary_key_set = (
        'sun_rise',
        'sun_set',
        'timezone_name',
        'timezone'
    )
    assert all(k in payload for k in summary_key_set)

    current_day_weather = payload['consolidated_weather'][0]
    daily_weather_key_set = (
        'weather_state_name',
        'applicable_date',
        'created',
        'min_temp',
        'max_temp',
        'the_temp',
        'wind_speed',
        'wind_direction',
        'air_pressure',
        'humidity',
        'visibility',
        'predictability'
    )
    assert all(k in current_day_weather for k in daily_weather_key_set)
