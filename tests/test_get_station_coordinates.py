from imgw_data.stations import get_active_stations_coordinates


def test_get_stations_coordinates():
    ids_and_coordinates = get_active_stations_coordinates()
    assert isinstance(ids_and_coordinates, list)
    assert isinstance(ids_and_coordinates[0], list)
