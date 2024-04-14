from typing import Union

import requests


def add_coordinates(readings: list[dict],
                    coordinates: list[list],
                    raise_error_if_missing=False):
    """
    Function adds coordinates to downloaded stations.

    Parameters
    ----------
    readings : list[dict]
        Current weather readings.

    coordinates : list[list]
        ``[[id, longitude, latitude], ...]``

    raise_error_if_missing : bool, default = False
        If any coordinates are missing then raise error.

    Returns
    -------
    : list[dict]
        Readings woth additional keys: ``lon`` | ``lat``.
    """

    transformed = []
    transformed_ids = set()
    all_ids = set()

    for reading in readings:
        rid = reading['station_id'][2:]
        all_ids.add(rid)
        # Get coordinates
        for coo in coordinates:
            if str(coo[0]) == rid:
                new_reading = reading.copy()
                new_reading['lon'] = coo[1]
                new_reading['lat'] = coo[2]
                transformed.append(new_reading)
                transformed_ids.add(str(coo[0]))
                break

    if raise_error_if_missing:
        if len(transformed) != len(readings):
            missing_ids = all_ids.difference(transformed_ids)
            missing_stations = ['12'+str(x) for x in missing_ids]
            raise ValueError(f'Missing coordinates for those stations: {missing_stations}')

    return transformed


def parse_response(response: requests.Response, ftype: str) -> Union[list[dict], str]:
    """
    Function parses response data to appropriate format.

    Parameters
    ----------
    response : requests.Response

    ftype : str

    Returns
    -------
    : Union[list[dict], str]
    """
    if ftype == 'csv':
        return response.text
    elif ftype == 'xml':
        return response.text
    elif ftype == 'html':
        return response.text

    return response.json()
