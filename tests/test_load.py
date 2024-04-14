from imgw_data import get_current_weather


def test_load_data():
    weather = get_current_weather()
    assert bool(weather)
