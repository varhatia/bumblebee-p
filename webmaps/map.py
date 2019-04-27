import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
print(data)
print(data.columns)

lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
el = list(data["ELEV"])

def color_producer(elevation):
    if(elevation < 1000):
        return 'green'
    elif (1000<= elevation < 3000):
        return 'orange'
    else:
        return 'yellow'

map = folium.Map(location=[38.58, -99], zoom_start=8, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name = "Volcanoes")

for lt,ln, nm, el in zip(lat,lon, name, el):
    fgv.add_child(folium.Marker(location=[lt, ln], tooltip=nm, icon=folium.Icon(color=color_producer(el))))

fgp = folium.FeatureGroup(name = "Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor' : 'green' if x['properties']['POP2005'] < 20000000
else 'orange' if 20000000 <= x['properties']['POP2005'] < 50000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map1.html")
