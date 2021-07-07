import pandas as pd
import folium
import json

testbusanmap = folium.Map(
    location = [35.20310343924181, 129.0570605554762],
    titles = 'Pusan map',
    zoom_start = 11
)

folium.CircleMarker(
    location     = [35.203103,129.057061],
    fill         = True,
    fill_color   = 'red', 
    fill_opacity = 1,
    color        = 'red',
    weight       = 10,
    radius       = 30,
).add_to(testbusanmap)
testbusanmap.save('map.html')
