import folium
import pandas

# create map object
mapObj = folium.Map(location=[-41.2935209, 174.7760023], zoom_start=12)

# extract coordinate data from a CVS file with pandas
data = pandas.read_csv("Volcanoes.txt")
names_list = list(data["NAME"])
lon_list = list(data["LON"])
lat_list = list(data["LAT"])

# create feature group
feature_group = folium.FeatureGroup(name="my feature group")

# load file into feature group
for name, lat, lon in zip(names_list, lat_list, lon_list):
    feature_group.add_child(folium.Marker(location=[lat, lon],
                                          popup=name,
                                          icon=folium.Icon(color="blue")))

# add feature group and save a file
mapObj.add_child(feature_group)
mapObj.save("map1.html")

