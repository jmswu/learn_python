import folium

mapObj = folium.Map(location=[-41.2935209, 174.7760023], zoom_start=12)

feature_group = folium.FeatureGroup(name="my feature group")

for location in [[-41.2935209, 174.776002], [-41.2925209, 174.775002], [-41.2905209, 174.779002]]:
    feature_group.add_child(folium.Marker(location=location,
                                          popup="I am a marker",
                                          icon=folium.Icon(color="blue")))

mapObj.add_child(feature_group)
mapObj.save("map1.html")

