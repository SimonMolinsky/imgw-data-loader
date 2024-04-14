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


def export_to_file(ds, fname: str, ftype: str):
    """
    Function exports dataset to a specific file.

    Parameters
    ----------
    ds : Union[list[dict], str]

    fname : str

    ftype : str
    """

    if ftype == 'json':
        fname = _check_filesuffix(fname, suffix='json')
        if isinstance(ds, list):
            with open(fname, 'w', encoding='utf8') as fin:
                json.dump(ds, fin, indent=2, ensure_ascii=False)
        elif isinstance(ds, str):
            with open(fname, 'w', encoding='utf8') as fin:
                serialized = json.dumps(ds, ensure_ascii=False).encode('utf-8')
                fin.write(serialized)
    else:
        if ftype == 'csv':
            fname = _check_filesuffix(fname, suffix='csv')
        elif ftype == 'xml':
            fname = _check_filesuffix(fname, suffix='xml')
        elif ftype == 'html':
            fname = _check_filesuffix(fname, suffix='html')
        else:
            raise TypeError('Unknown output file type!')

        with open(fname, 'w', encoding='utf8') as fin:
            fin.write(ds)
