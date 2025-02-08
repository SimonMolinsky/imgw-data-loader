from typing import Union


HYDRO_MAPPER = {
    'id_stacji': 'station_id',
    'stacja': 'station_name',
    'rzeka': 'river',
    'województwo': 'voivodeship',
    'stan_wody': 'water_level_cm',
    'stan_wody_data_pomiaru': 'water_level_measurement_datetime',
    'temperatura_wody': 'water_temperature_C',
    'temperatura_wody_data_pomiaru': 'water_temperature_measurement_datetime',
    'zjawisko_lodowe': 'ice_phenomena_code',
    'zjawisko_lodowe_data_pomiaru': 'ice_phenomena_measurement_datetime',
    'zjawisko_zarastania': 'vegetation_growth_code',
    'zjawisko_zarastania_data_pomiaru': 'vegetation_growth_measurement_datetime',
    'lon': 'lon',
    'lat': 'lat'
}


SYNOPTIC_MAPPER = {
    'id_stacji': 'station_id',
    'stacja': 'station_name',
    'data_pomiaru': 'observation_date',
    'godzina_pomiaru': 'observation_hour',
    'temperatura': 'temperature',
    'predkosc_wiatru': 'wind_speed',
    'kierunek_wiatru': 'wind_direction',
    'wilgotnosc_wzgledna': 'relative_humidity',
    'suma_opadu': 'precipitation',
    'cisnienie': 'pressure',
    'lon': 'lon',
    'lat': 'lat',
    'mnpm': 'elevation'
}


def translate_json(json_list, mapper):
    """
    Function translates given list of json-s.

    Parameters
    ----------
    json_list : list[dict]

    mapper : dict

    Returns
    -------
    translated : list[dict]
    """
    translated = []
    for obs in json_list:
        ndict = {}
        for _k, _v in obs.items():
            ndict[mapper[_k]] = _v
        translated.append(ndict)
    return translated


def translate_hydro_json(hydro_json: list[dict]):
    """
    Function translates hydrological observations from Polish to English.

    Parameters
    ----------
    hydro_json : list[dict]

    Returns
    -------
    translated : list[dict]
    """
    return translate_json(json_list=hydro_json, mapper=HYDRO_MAPPER)


def translate_synoptic_json(synoptic_json: list[dict]):
    """
    Function translates synoptic data keys from string.

    Parameters
    ----------
    synoptic_json : list[dict]

    Returns
    -------
    translated : list[dict]
    """
    return translate_json(json_list=synoptic_json, mapper=SYNOPTIC_MAPPER)


def translate_synoptic_text(synoptic_text: str):
    """
    Function translates synoptic data keys from string.

    Parameters
    ----------
    synoptic_text : str

    Returns
    -------
    : str
    """
    for _polish, _english in SYNOPTIC_MAPPER.items():
        synoptic_text = synoptic_text.replace(_polish, _english)
    return synoptic_text


def translate_synoptic(ds: Union[str, list[dict]]):
    """
    Function translates synoptic data keys from string.

    Parameters
    ----------
    ds : Union[str, list[dict]]
        CSV, XML, HTML text or JSON list with IMGW readings.

    Returns
    -------
    translated : Union[str, list[dict]]
    """
    if isinstance(ds, str):
        return translate_synoptic_text(ds)
    elif isinstance(ds, list):
        return translate_synoptic_json(ds)
    else:
        raise TypeError('Not recognized input data type!')
