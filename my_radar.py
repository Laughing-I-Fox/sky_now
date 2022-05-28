import requests
import webbrowser
import folium
import pandas as pd

# Area coordinates
lon_min, lat_min = 15.74,  42.55
lon_max, lat_max = 19.62,  45.28
# Username and password for Open Sky
user_name = 'token.rey'
password = '2Jqt3NvWK93oundBuDNO'
# Request
url_data = f'https://token.rey:2Jqt3NvWK93oundBuDNO@opensky-network.org/api/states/all?lamin=' \
           f'{lat_min}&lomin={lon_min}&lamax={lat_max}&lomax={lon_max}'
# Response
response = requests.get(url_data).json()
# rename columns
col_name = ['icao24', 'callsign', 'origin_country', 'time_position', 'last_contact', 'long', 'lat', 'baro_altitude',
            'on_ground', 'velocity', 'true_track', 'vertical_rate', 'sensors', 'geo_altitude', 'squawk', 'spi',
            'position_source']
# Create dataframe from response
flight_df = pd.DataFrame(response['states'])
# Format table dataframe
flight_df = flight_df.loc[:, 0:16]
flight_df.columns = col_name
# Change None to Unavailable
flight_df = flight_df.fillna('Unavailable')

# Fix display table problem pycharm
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.width', 500)

# Create instance folium map
world_map = folium.Map(zoom_start=12, control_scale=True, tiles='Stamen Terrain')
world_map.fit_bounds([[90, -180], [-90, 180]])

# Add markers from dataframe to map
for i in range(0, len(flight_df)):
    folium.Marker(
        location=[flight_df.iloc[i]['lat'], flight_df.iloc[i]['long']], popup=flight_df.iloc[i]['callsign'],
        icon=folium.Icon(color='blue', icon='glyphicon-plane')). \
        add_to(world_map)

# Auto open map in browser just for test
world_map.save('map_1.html')


def auto_open(path):
    html_page = f'{path}'
    world_map.save(html_page)
    new = 2
    webbrowser.open(html_page, new=new)


auto_open('map_1.html')
