import streamlit as st
import folium
from streamlit_folium import st_folium

map = folium.Map([-5.6645401109365805, -36.60398193330714],
                 tiles="cartodbpositron", zoom_start=10)
folium.plugins.LocateControl().add_to(map)
folium.plugins.LocateControl(auto_start=True).add_to(map)

# Configura o Streamlit
st.title("Mapa com Localização Atual")

# Exibe o mapa no Streamlit
st_data = st_folium(map, width=700, height=500)
