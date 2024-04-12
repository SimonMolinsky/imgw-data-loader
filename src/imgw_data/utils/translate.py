from typing import Union


MAPPER = {
    'id_stacji': 'station_id',
    'stacja': 'station_name',
    'data_pomiaru': 'observation_date',
    'godzina_pomiaru': 'observation_hour',
    'temperatura': 'temperature',
    'predkosc_wiatru': 'wind_speed',
    'kierunek_wiatru': 'wind_direction',
    'wilgotnosc_wzgledna': 'relative_humidity',
    'suma_opadu': 'precipitation',
    'cisnienie': 'pressure'
}


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
    translated = []
    for obs in synoptic_json:
        ndict = {}
        for _k, _v in obs.items():
            ndict[MAPPER[_k]] = _v
        translated.append(ndict)
    return translated


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
    for _polish, _english in MAPPER.items():
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
