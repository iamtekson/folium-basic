import folium

m = folium.Map(location=[28.2380,83.9956], zoom_start=12)

tooltip = 'Click for more info'
logo = folium.features.CustomIcon('1.jpg', icon_size=(50,50))

folium.Marker([28.2380,83.9956],
				popup='this is first location',
				tooltip=tooltip).add_to(m),
folium.Marker([28.2350,83.9566],
				popup='this is second location',
				tooltip=tooltip,
				icon= folium.Icon(color='red')).add_to(m),
folium.Marker([28.2450,83.9566],
				popup='this is second location',
				tooltip=tooltip,
				icon= logo).add_to(m)

folium.CircleMarker(
	location=[28.2250,83.9666],
	radius = 50,
	popup='something here',
	color='#428bca',
	fill=True,
	fill_color='#428bca'
	).add_to(m)

m.save('map.html')
				
