from imgw_data import get_current_weather, get_current_hydro


def test_load_hydro():
    hydro = get_current_hydro()
    assert bool(hydro)


def test_load_weather():
    weather = get_current_weather()
    assert bool(weather)


