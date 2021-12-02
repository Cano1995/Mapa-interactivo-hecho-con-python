#lIBRERIAS
import folium
from folium import plugins
import pandas as pd
import webbrowser

webbrowser.open('https://www.python.org')

from folium.plugins import MarkerCluster #para agrupar los puntos espaciales o Escuelas
#Puntos Espaciales
escuelas = pd.read_excel('C:/Users/pro1/Documents/pythonmapa/ESCUELAS.xlsx')

#DEPLOY MAP

mapa = folium.Map(location=[-23.442503,-58.443832],
                            zoom_start=5)

#Capa de Escuelas

codigo = list (escuelas["CODIGO"])
latitud = list (escuelas["Latitud"])
longitud = list (escuelas["Longitud"])
fpp = list (escuelas["INSTITUCIONES DEL PAIS"])
color_e = list (escuelas["COLOR_EXTERNO"])
color_i = list (escuelas["COLOR_INTERNO"])
icons = list (escuelas["ICONO"])
prefx = list (escuelas["PREFIX"])

mc_fp = MarkerCluster()

for cod,lat,lon,fp,c_e,c_i,ico,pref in zip(codigo,latitud,longitud,fpp,color_e,color_i,icons,prefx):
    mc_fp.add_child(folium.Marker(location=[lat,lon],
    popup="<b> Codigo: </b>"+str(cod)+"<br> <b> Institucion: <b>"+fp+"</br>",max_width=4000, min_width=4000,
    icon=folium.Icon(color=c_e,
    icon_color=c_i,
    icon=ico,
    prefix=pref)))

Capa_fp = folium.FeatureGroup(name='Institucion')
mc_fp.add_to(Capa_fp)

mapa.add_child(Capa_fp)

#capas del Mapa Base
folium.TileLayer('Stamen Terrain').add_to(mapa)
folium.TileLayer('Cartodb Positron').add_to(mapa)
folium.TileLayer('Cartodb dark_matter').add_to(mapa)
folium.TileLayer('Stamentoner').add_to(mapa)

folium.LayerControl(position='topleft').add_to(mapa)

mapa.save('mapa_interactivo.html')
webbrowser.open('mapa_interactivo.html')
