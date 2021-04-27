import folium

maps = folium.Map(location=[59.807602, 30.379634], zoom_start=17, tiles='https://server.arcgisonline.com/ArcGIS/rest'
                                                                        '/services/World_Imagery/MapServer/tile/{z}/{'
                                                                        'y}/{x}', attr="toner-bcg")
fg = folium.FeatureGroup(name="My map")
for coordinates in [[59.807602, 30.379634], [59.807602, 30.38]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Привет!Здесь живу я!",
                               icon=folium.Icon(color='red', icon="home", prefix='fa')))
assert isinstance(fg, object)
maps.add_child(fg)
maps.add_child(folium.LatLngPopup())

maps.save('map.html')
