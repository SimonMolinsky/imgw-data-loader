from typing import List

from imgw_data.get import get_current_weather


def get_active_stations_coordinates() -> List:
    """
    Function returns ID, longitude, latitude of each active meteorological station.

    Returns
    -------
    : List
        ``[[station_id, lon, lat]]``
    """

    current_stations = get_current_weather(
        translate_to_english=True, add_station_coordinates=True
    )

    results = []

    for station in current_stations:

        results.append(
            [station['station_id'], station['lon'], station['lat']]
        )

    return results
