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

# add feature group and save a file
mapObj.add_child(feature_group)
mapObj.save("map1.html")
