import folium

maps = folium.Map(location=[59.807602, 30.379634], zoom_start=17, tiles='https://server.arcgisonline.com/ArcGIS/rest'
																		'/services/World_Imagery/MapServer/tile/{z}/{'
																		'y}/{x}', attr="toner-bcg")
fg = folium.FeatureGroup(name="My map")
fg.add_child(folium.Marker(location=[59.807602, 30.379634], popup="Привет!Здесь живу я!", icon=folium.Icon(color="green")))
maps.add_child(fg)
maps.add_child(folium.LatLngPopup())

maps.save('map.html')
