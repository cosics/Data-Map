import folium
import os
import json

#Create map object
m = folium.Map(location=[45.6580, 25.6012], zoom_start = 12)

#Global tooltip
tooltip = 'Click For more Info'

#Create custom marker icon
logoIcon = folium.features.CustomIcon('merge.png', icon_size=(25, 50))

#Vega data
vis = os.path.join('data', 'vis.json')

#Geojson data
overlay = os.path.join('data', 'overlay.json')

#Create markers
folium.Marker([45.6595, 25.6123],
            popup='<strong>Location One</strong>',
            tooltip=tooltip).add_to(m),
folium.Marker([45.6459, 25.5923],
            popup='<strong>Location Two</strong>',
            tooltip=tooltip,
            icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([45.6578, 25.6208],
            popup='<strong>Location Three</strong>',
            tooltip=tooltip,
            icon=folium.Icon(color='purple')).add_to(m),
folium.Marker([45.6759, 25.6123],
            popup='<strong>Location Four</strong>',
            tooltip=tooltip,
            icon=folium.Icon(icon='leaf', color='green')).add_to(m),
#folium.Marker([45.6759, 25.6223],
            #popup='<strong>Location Five</strong>',
            #tooltip=tooltip,
            #icon=folium.Icon(icon=logoIcon)).add_to(m) 
folium.Marker([45.6512, 25.6298],
            popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)), width=450, height=250))).add_to(m),   

#Circle marker
folium.CircleMarker(
    location=[45.641985, 25.590805],
    redius=100,
    popup="TipoTipoTipo",
    color='#428bca',
    fill=True,
    fill_color='#428bca'
).add_to(m)        

#Geojson overlay
folium.Geojson(overlay, name='brasov').add_to(m)

#Generate map
m.save('map.html')