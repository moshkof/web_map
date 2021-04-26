import folium

maps = folium.Map(location=[59.803338, 30.377412], zoom_start=17, tiles='https://server.arcgisonline.com/ArcGIS/rest'
																		'/services/World_Imagery/MapServer/tile/{z}/{'
																		'y}/{x}', attr="toner-bcg")
maps.save('map.html')
