import json


def _check_filesuffix(fname: str, suffix: str):
    """
    Function checks suffix of a file and returns file with a valid suffix.

    Parameters
    ----------
    fname : str

    suffix : str

    Returns
    -------
    checked : str
    """
    if fname.endswith(suffix):
        return fname
    return fname + '.' + suffix


def export_to_file(ds, fname: str, as_json=False, as_csv=False, as_xml=False, as_html=False):
    """
    Function exports dataset to a specific file.

    Parameters
    ----------
    ds : Union[list[dict], str]

    fname : str

    as_json : bool, default=False

    as_csv : bool, default=False

    as_xml : bool, default=False

    as_html : bool, default=False
    """

    if as_json:
        fname = _check_filesuffix(fname, suffix='json')
        if isinstance(ds, list):
            with open(fname, 'w', encoding='utf8') as fin:
                json.dump(ds, fin, indent=2, ensure_ascii=False)
        elif isinstance(ds, str):
            with open(fname, 'w', encoding='utf8') as fin:
                serialized = json.dumps(ds, ensure_ascii=False).encode('utf-8')
                fin.write(serialized)
    else:
        if as_csv:
            fname = _check_filesuffix(fname, suffix='csv')
        elif as_xml:
            fname = _check_filesuffix(fname, suffix='xml')
        elif as_html:
            fname = _check_filesuffix(fname, suffix='html')
        else:
            raise TypeError('Output file format must be set!')

        with open(fname, 'w', encoding='utf8') as fin:
            fin.write(ds)
