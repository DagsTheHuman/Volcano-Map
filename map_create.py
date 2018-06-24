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

fgp = folium.FeatureGroup(name='Population')

fgp.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read()), style_function=lambda x: {'fillColor':'green' 
if x['properties']['POP2005']<10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red',
'color':'grey', 'weight':0.5}, smooth_factor=0.5))

fgv = folium.FeatureGroup(name='Volcano Map')

for lt, lg, el, na, tp in zip(lat,lon,elev,name,vol_type):
    fgv.add_child(folium.CircleMarker(location=[lt,lg], radius= 7, popup=folium.Popup(str(na) + '\n' + str(el) + ' m  Type: ' + str(tp),parse_html=True),
    fill_color= color_producer(el), color = 'grey', fill= True, fill_opacity=0.9))

map_obj.add_child(fgp)
map_obj.add_child(fgv)

map_obj.add_child(folium.LayerControl())

map_obj.save('map1.html')
