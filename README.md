# imgw-data-loader

Python API for IMGW (Polish: Instytut Meteorologii i Gospodarki Wodnej) public data access.

## Setup

```shell
pip install imgw-data
```

## Usage

### `get_current_weather()`

Function gets current weather from IMGW website. Monitored variables (polish: english):

- 'id_stacji': 'station_id'
- 'stacja': 'station_name'
- 'data_pomiaru': 'observation_date'
- 'godzina_pomiaru': 'observation_hour'
- 'temperatura': 'temperature'
- 'predkosc_wiatru': 'wind_speed'
- 'kierunek_wiatru': 'wind_direction'
- 'wilgotnosc_wzgledna': 'relative_humidity'
- 'suma_opadu': 'precipitation'
- 'cisnienie': 'pressure'

### Download as a Python object

```python
from imgw_data import get_current_weather


current_weather_json = get_current_weather()  # downloads data as JSON
current_weather_csv = get_current_weather(as_csv=True)  # downloads data as string csv
current_weather_xml = get_current_weather(as_xml=True)  # downloads data as string xml
current_weather_html = get_current_weather(as_html=True)  # downloads data as string html

current_weather_pl = get_current_weather(translate_to_english=False)  # downloads original data with Polish sentences

print(current_weather_json)

```

```shell
[
  {'station_id': '12295',
   'station_name': 'Białystok',
   'observation_date': '2024-04-12',
   'observation_hour': '7',
   'temperature': '12.2',
   'wind_speed': '2',
   'wind_direction': '250',
   'relative_humidity': '68.8',
   'precipitation': '0',
   'pressure': '1028.6'}, 
   {...},
]

```

### Download and export to file

```python
from imgw_data import get_current_weather


current_weather_json = get_current_weather(fname='data.json')  # stores data as JSON
current_weather_csv = get_current_weather(fname='data.csv', as_csv=True)  # stores data as string csv
current_weather_xml = get_current_weather(fname='data.xml', as_xml=True)  # stores data as string xml
current_weather_html = get_current_weather(fname='data.html', as_html=True)  # stores data as string html

```

## Dependencies

- Python >= 3.8
- `requests`