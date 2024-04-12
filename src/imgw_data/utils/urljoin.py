def urljoin(base: str, *args) -> str:
    """
    Save join of url path.

    Parameters
    ----------
    base : str
        url base

    args : list
        other parts of url

    Returns
    -------
    : str
        Full URL path.
    """

    # Strip base from the last / if exists
    base = base.rstrip('/')

    # Strip all other parts from /
    url_parts = []
    for url_part in args:
        url_part: str
        url_part = url_part.strip('/')
        url_parts.append(url_part)

    # Join all parts
    pts = [base]
    pts.extend(url_parts)

    url = '/'.join(pts)
    return url
