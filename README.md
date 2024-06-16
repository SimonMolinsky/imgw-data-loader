# imgw-data-loader

Python API for IMGW (Polish: Instytut Meteorologii i Gospodarki Wodnej) public data access.

## Setup

```shell
pip install imgw-data
```

## Usage

### `get_current_weather()`

Function gets current weather from IMGW website. Monitored variables (*polish*: *english*):

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

#### Download as a Python object

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

#### Download and export to file

```python
from imgw_data import get_current_weather


current_weather_json = get_current_weather(fname='data.json')  # stores data as JSON
current_weather_csv = get_current_weather(fname='data.csv', as_csv=True)  # stores data as string csv
current_weather_xml = get_current_weather(fname='data.xml', as_xml=True)  # stores data as string xml
current_weather_html = get_current_weather(fname='data.html', as_html=True)  # stores data as string html

```

### `get_current_hydro()`

Function gets current hydrological observations from IMGW website. Monitored variables (*polish*: *english*):

- 'id_stacji': 'station_id'
- 'stacja': 'station_name'
- 'rzeka': 'river',
- 'województwo': 'voivodeship',
- 'stan_wody': 'water_level_cm',
- 'stan_wody_data_pomiaru': 'water_level_measurement_datetime',
- 'temperatura_wody': 'water_temperature_C',
- 'temperatura_wody_data_pomiaru': 'water_temperature_measurement_datetime',
- 'zjawisko_lodowe': 'ice_phenomena_code',
- 'zjawisko_lodowe_data_pomiaru': 'ice_phenomena_measurement_datetime',
- 'zjawisko_zarastania': 'vegetation_growth_code',
- 'zjawisko_zarastania_data_pomiaru': 'vegetation_growth_measurement_datetime',

#### Download as a Python object

```python
from imgw_data import get_current_hydro


current_hydro_json = get_current_hydro()  # downloads data as JSON
current_hydro_pl = get_current_hydro(translate_to_english=False)  # downloads original data with Polish sentences

print(current_hydro_json)

```

```shell
[
  {'station_id': '151140030',
   'station_name': 'Przewoźniki',
   'river': 'Skroda',
   'voivodeship': 'lubuskie',
   'water_level_cm': '243',
   'water_level_measurement_datetime': '2024-06-16 09:10:00',
   'water_temperature_C': None,
   'water_temperature_measurement_datetime': None,
   'ice_phenomena_code': '0',
   'ice_phenomena_measurement_datetime': '2024-01-09 11:00:00',
   'vegetation_growth_code': '0',
   'vegetation_growth_measurement_datetime':
   '2023-09-11 10:00:00'},
   ...
]
```

#### Download and export to file

```python
from imgw_data import get_current_hydro


current_weather_json = get_current_hydro(fname='data.json')  # stores data as JSON

```

### `get_active_stations_coordinates()`

Returns list with station id, station longitude, station latitude among the current active stations.

```python
from imgw_data.stations import get_active_stations_coordinates


active_stations = get_active_stations_coordinates()
print(active_stations[0])

```

```shell
['12295', 23.162281307080264, 53.10725901708551]
```

## Dependencies

- Python >= 3.8
- `requests`