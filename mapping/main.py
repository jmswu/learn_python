import folium
import pandas

# create map object
mapObj = folium.Map(location=[37.2093588, -113.8991741], zoom_start=5)

# extract coordinate data from a CVS file with pandas
data = pandas.read_csv("Volcanoes.txt")
names_list = list(data["NAME"])
lon_list = list(data["LON"])
lat_list = list(data["LAT"])
elev_list = list(data["ELEV"])


def color_maker(elevation):
    if elevation < 1500:
        return "green"
    elif 1500 <= elevation < 2500:
        return "orange"
    else:
        return "red"


# create feature group
feature_group = folium.FeatureGroup(name="my feature group")

# load file into feature group
for name, lat, lon, elev in zip(names_list, lat_list, lon_list, elev_list):
    feature_group.add_child(folium.Marker(location=[lat, lon],
                                          popup=elev,
                                          icon=folium.Icon(color=color_maker(elev))))

# lambda style function is too long
# just break it down to here
lambda_style_function = lambda x: {"fillColor": "green" if x["properties"]["POP2005"] < 10000000
else "orange" if 15000000 <= x["properties"]["POP2005"] < 50000000
else "red"}

# add world layer
word_data = open("world.json", "r", encoding="utf-8-sig").read()
feature_group.add_child(folium.GeoJson(data=word_data, style_function=lambda_style_function))

# add feature group and save a file
mapObj.add_child(feature_group)
mapObj.save("map1.html")
