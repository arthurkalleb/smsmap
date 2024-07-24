import folium
from folium.plugins import LocateControl

map = folium.Map(
    location=[-5.664558763806402, -36.60399399589964],
    tiles="OpenStreetMap",  # Corrigido para 'tiles'
    zoom_start=5
)

# Adiciona o LocateControl ao mapa
LocateControl(
    auto_start=True,
    drawMarker=True,  # Adiciona o marcador no mapa
    markerStyle=dict(
        className="leaflet-control-locate-marker",
        color="green",
        fillColor="black",
        fillOpacity=1
    )
).add_to(map)
