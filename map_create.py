import folium
import pandas

mappings = pandas.read_excel('vol_locations.xlsx')
lat = list(mappings['Latitude'])
lon = list(mappings['Longitude'])
elev = list(mappings['Elevation (m)'])
name = list(mappings['Name'])
vol_type = list(mappings['Type'])

def color_producer(elevation):
    if elevation < 0:
        return 'darkblue'
    else:
        return 'red'

map_obj = folium.Map(location=[41.034069, -112.234989],zoom_start=5)

fg = folium.FeatureGroup(name='Volcano Map')

for lt, lg, el, na, tp in zip(lat,lon,elev,name,vol_type):
    fg.add_child(folium.CircleMarker(location=[lt,lg], radius= 7, popup=folium.Popup(str(na) + '\n' + str(el) + ' m  Type: ' + str(tp),parse_html=True),
    fill_color= color_producer(el), color = 'grey', fill= True, fill_opacity=0.9))

map_obj.add_child(fg)

map_obj.save('map1.html')