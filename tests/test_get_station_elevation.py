from imgw_data.utils.parse import get_station_elevation


def test_get_stations_elevation():
    elevation = get_station_elevation(200)
    assert isinstance(elevation, int)
    assert elevation == 4
