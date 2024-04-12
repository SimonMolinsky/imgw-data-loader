from typing import Union

import requests
from src.imgw_data.consts import IMGWUrls, IMGWDataFormats
from src.imgw_data.export.export import export_to_file
from src.imgw_data.utils.parse import parse_response
from src.imgw_data.utils.translate import translate_synoptic
from src.imgw_data.utils.urljoin import urljoin


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
        return urlbase
    elif is_csv:
        return urljoin(urlbase, 'format', IMGWDataFormats.CSV.value)
    elif is_xml:
        return urljoin(urlbase, 'format', IMGWDataFormats.XML.value)
    elif is_html:
        return urljoin(urlbase, 'format', IMGWDataFormats.HTML.value)

    return urlbase


def get_current_weather(
        fname: str = None,
        translate_to_english=True,
        as_json=False,
        as_csv=False,
        as_xml=False,
        as_html=False,
):
    """
    Function gets current weather from IMGW website.

    Parameters
    ----------
    fname : str, optional
        Filename where to store readings. If provided then function saves data instead of returning it.

    translate_to_english : bool, default = true
        Translate weather readings keys to English.

    as_json : bool, default = False
        Save output to json.

    as_csv : bool, default = False
        Save output to csv.

    as_xml : bool, default = False
        Save output as xml file.

    as_html : bool, default = False
        Save output as html.

    Notes
    -----
    If all file type parameters are set to ``False`` then system downloads default JSON.
    """

    base_url = IMGWUrls.SYNOPTIC.value

    url = _build_format_url(
        urlbase=base_url,
        is_json=as_json,
        is_csv=as_csv,
        is_xml=as_xml,
        is_html=as_html
    )

    response = requests.get(url=url)

    # Parse response
    parsed = parse_response(
        response, url
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
            as_json=as_json,
            as_csv=as_csv,
            as_xml=as_xml,
            as_html=as_html
        )
