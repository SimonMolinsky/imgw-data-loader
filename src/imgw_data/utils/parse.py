from typing import Union

import requests


def parse_response(response: requests.Response, baseurl: str) -> Union[list[dict], str]:
    """
    Function parses response data to appropriate format.

    Parameters
    ----------
    response : requests.Response

    baseurl : str

    Returns
    -------
    : Union[list[dict], str]
    """
    if baseurl.endswith('csv'):
        return response.text
    elif baseurl.endswith('xml'):
        return response.text
    elif baseurl.endswith('html'):
        return response.text

    return response.json()
