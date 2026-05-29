# https://dash.plotly.com/dash-core-components/rangeslider --> main slider template
# https://dash.plotly.com/dash-core-components/slider
# https://dash.plotly.com/minimal-app --> main template
# ChatGPT gave me idea to add limits to the quantiles to filter out outliers and make the scaling better and introduced me to the quantile function

from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import numpy as np

df = pd.read_csv("data/NY-House-Dataset.csv")

app = Dash()

low = df["PRICE"].quantile(0.001)
high = df["PRICE"].quantile(0.96)

# Requires Dash 2.17.0 or later
app.layout = html.Div([
    html.H1(children='Filtered Property Sales Map of NYC by Sale Price', style={'textAlign':'center'}),
    dcc.RangeSlider(min=low, max=high, step=10000, value=[low, high], id='my-range-slider', updatemode="mouseup"),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('my-range-slider', 'value')
)
def update_graph(priceRange):

    minPrice, maxPrice = priceRange

    df2 = df[(df["PRICE"] >= minPrice) & (df['PRICE'] <= maxPrice)]
    fig = px.scatter_mapbox(df2, lat="LATITUDE", lon="LONGITUDE", size="PRICE", color="STATE", size_max=10, zoom=10, height=1000)
    fig.update_layout(mapbox_style="carto-darkmatter")
    return fig

if __name__ == '__main__':
    app.run(debug=True)
