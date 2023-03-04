import json

import plotly.graph_objects as go
import pandas as pd

from rdp import rdp

scl = ['rgb(213,62,79)', 'rgb(244,109,67)', 'rgb(253,174,97)', \
       'rgb(254,224,139)', 'rgb(255,255,191)', 'rgb(230,245,152)', \
       'rgb(171,221,164)', 'rgb(102,194,165)', 'rgb(50,136,189)'
       ]
n_colors = len(scl)

with open('contours.json') as json_data:
    data = json.load(json_data)
    json_data.close()

fig = go.Figure()

for contour in data["contours"]:
    print(f"processing contour z:{contour['z']}")
    for i, curve in enumerate(contour['sets']):
        print(f"processing line #{i}")
        df = pd.DataFrame(curve, columns=['x', 'y'])
        rdp_df = pd.DataFrame(rdp(curve, epsilon=0.1), columns=['x', 'y'])

        fig.add_trace(go.Scattergeo(
            lat=df["x"],
            lon=df["y"],
            mode='lines+markers',
            marker={'size': 10},
            line=dict(width=1, color=scl[i % n_colors])
        ))

        fig.add_trace(go.Scattergeo(
            lat=rdp_df["x"],
            lon=rdp_df["y"],
            marker={'size': 5},
            mode='lines+markers',
            line=dict(width=1, color=scl[(i + 5) % n_colors])
        ))

fig.update_geos(projection_type="equirectangular")
fig.update_layout(
    width=1300,
    margin={"r": 0, "t": 0, "l": 0, "b": 0}
)
fig.write_html('data/map_plotly.html', auto_open=True)
