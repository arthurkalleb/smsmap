import folium
from folium.plugins import LocateControl

map = folium.Map([-5.6645401109365805, -36.60398193330714],
                 tiles="cartodbpositron", zoom_start=10)

folium.plugins.LocateControl().add_to(map)

folium.plugins.LocateControl(auto_start=True).add_to(map)

map
