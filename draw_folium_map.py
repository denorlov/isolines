import json

import folium
from rdp import rdp

m = folium.Map()

with open('data\contours.json') as json_data:
    data = json.load(json_data)
    json_data.close()

for contour in data["contours"]:
    print(f"processing contour z:{contour['z']}")
    for i, curve in enumerate(contour['sets']):
        print(f"processing line #{i}")
        folium.PolyLine(curve, tooltip=f"z #{contour['z']}_{i}", color='red').add_to(m)
        folium.PolyLine(rdp(curve, epsilon=0.1), tooltip=f"z compacted #{contour['z']}_{i}", color='blue').add_to(m)

m.save("data\map_folium.html")
