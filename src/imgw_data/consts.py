from enum import Enum


class IMGWUrls(Enum):
    """Groups IMGW links"""
    SYNOPTIC = 'https://danepubliczne.imgw.pl/api/data/synop/'
    HYDROLOGICAL = 'http://danepubliczne.imgw.pl/api/data/hydro/'


class IMGWDataFormats(Enum):
    XML = 'xml'
    JSON = 'json'
    HTML = 'html'
    CSV = 'csv'


class IMGWStations:
    pass
