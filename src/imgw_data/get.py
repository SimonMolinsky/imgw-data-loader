from typing import Optional

import requests
from imgw_data.consts import IMGWUrls, IMGWDataFormats, IMGWStationsCoordinates
from imgw_data.export.export import export_to_file
from imgw_data.utils.parse import parse_response, add_coordinates, add_elevation
from imgw_data.utils.translate import translate_synoptic, translate_hydro_json
from imgw_data.utils.urljoin import urljoin


def _build_format_url(urlbase: str,
                      is_json=True,
                      is_csv=False,
                      is_xml=False,
                      is_html=False) -> str:
    """
    Function creates downloading url.

    Parameters
    ----------
    urlbase : str

    is_json : bool, default = False

    is_csv : bool, default = False

    is_xml : bool, default = False

    is_html : bool, default = False

    Returns
    -------
    url : str
    """

    if is_json:
        return urlbase, 'json'
    elif is_csv:
        return urljoin(urlbase, 'format', IMGWDataFormats.CSV.value), 'csv'
    elif is_xml:
        return urljoin(urlbase, 'format', IMGWDataFormats.XML.value), 'xml'
    elif is_html:
        return urljoin(urlbase, 'format', IMGWDataFormats.HTML.value), 'html'

    return urlbase, 'json'


# TODO: add station coordinates
def get_current_hydro(
        fname: str = None,
        translate_to_english=True
) -> Optional[list[dict]]:
    """
    Function gets current hydrological status from Poland (IMGW public data).

    Parameters
    ----------
    fname : str, optional
        Filename where to store readings. If provided then function saves data instead of returning it.

    translate_to_english : bool, default = true
        Translate weather readings keys to English.

    Returns
    -------
    readings : list[dict]
        Hydrological observations.
    """

    base_url = IMGWUrls.HYDROLOGICAL.value

    response = requests.get(url=base_url)

    # Parse response
    parsed = parse_response(
        response, 'json'
    )

    # translate
    if translate_to_english:
        parsed = translate_hydro_json(parsed)

    if fname is None:
        return parsed
    else:
        # Save data
        export_to_file(
            ds=parsed,
            fname=fname,
            ftype='json'
        )


def get_current_weather(
        fname: str = None,
        translate_to_english=True,
        add_station_coordinates=True,
        add_station_elevation=True,
        as_json=False,
        as_csv=False,
        as_xml=False,
        as_html=False,
        raise_error_on_missing_coordinates=False
):
    """
    Function gets current weather from IMGW website.

    Parameters
    ----------
    fname : str, optional
        Filename where to store readings. If provided then function saves data instead of returning it.

    translate_to_english : bool, default = true
        Translate weather readings keys to English.

    add_station_coordinates : bool, default = True
        Add station coordinates. Works only with json output.

    add_station_elevation : bool, default = True
        Add station elevation. Works only with json output.

    as_json : bool, default = False
        Save output to json.

    as_csv : bool, default = False
        Save output to csv.

    as_xml : bool, default = False
        Save output as xml file.

    as_html : bool, default = False
        Save output as html.

    raise_error_on_missing_coordinates : bool, default = False
        Raise ``ValueError`` if coordinates are missing.

    Notes
    -----
    If all file type parameters are set to ``False`` then system downloads default JSON.
    """

    base_url = IMGWUrls.SYNOPTIC.value

    url, ftype = _build_format_url(
        urlbase=base_url,
        is_json=as_json,
        is_csv=as_csv,
        is_xml=as_xml,
        is_html=as_html
    )

    response = requests.get(url=url)

    # Parse response
    parsed = parse_response(
        response, ftype
    )

    if add_station_coordinates and ftype == 'json':
        parsed = add_coordinates(
            readings=parsed,
            coordinates=IMGWStationsCoordinates.stations['data'],
            raise_error_if_missing=raise_error_on_missing_coordinates
        )

    if add_station_elevation and ftype == 'json':
        parsed = add_elevation(
            readings=parsed
        )

    if translate_to_english:
        parsed = translate_synoptic(parsed)

    if fname is None:
        return parsed
    else:
        # Save data
        export_to_file(
            ds=parsed,
            fname=fname,
            ftype=ftype
        )


if __name__ == '__main__':
    print(get_current_weather())
