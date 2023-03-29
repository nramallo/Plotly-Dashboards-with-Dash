import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import base64

def encode_image(image):
    encoded=base64.b64encode(open(image, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

##Multiple Inputs
''' df=pd.read_csv('~/Plotly-Dashboards-with-Dash/Data/mpg.csv')

app = dash.Dash()

features = df.columns

app.layout = html.Div([
    html.Div([dcc.Dropdown(
        id='xaxis',
        options=[{'label': i, 'value': i} for i in features],
        value='displacement')],
        style={'width': '48%', 'display': 'inline-block'}),

    html.Div([dcc.Dropdown(
        id='yaxis',
        options=[{'label': i, 'value': i} for i in features],
        value='mpg'
        )],
        style={'width': '48%', 'display': 'inline-block'}),

    dcc.Graph(id='features-graph')

], style={'padding': '10px'})

@app.callback(
    Output('features-graph', 'figure'),
    [Input('xaxis', 'value'),
     Input('yaxis', 'value')])

def update_graph(xaxis_value, yaxis_value):

    return {'data':go.Scatter(x=df[xaxis_value],
                              y=df[yaxis_value],
                              text=df['name'],
                              mode='markers',
                              marker=dict(size=15,
                                          opacity= 0.8,
                                          line= dict(width=0.5,color='white')
                                          )),

            'layout':go.Layout(title='My Dashboard',
                               xaxis=dict(title=xaxis_value),
                               yaxis=dict(title=yaxis_value),
                               hovermode='closest')}

if __name__ == '__main__':
    app.run_server(debug=True) '''

##Multiple Outputs
df2=pd.read_csv('~/Plotly-Dashboards-with-Dash/Data/wheels.csv')

app2 = dash.Dash()

app2.layout = html.Div([
    dcc.RadioItems(id='wheels',
                   options=[{'label':i, 'value':i} for i in df2['wheels'].unique()],
                   value=1
                   ),
    html.Div(id='wheels-output'),
    html.Hr(),
    dcc.RadioItems(id='color',
                   options=[{'label':i, 'value':i} for i in df2['color'].unique()],
                   value='blue'
                   ),
    html.Div(id='color-output'),
    html.Img(id='display-image',src='children',height=300)
],style={'fontFamiliy':'helvetica',
         'fontSize':18})

@app2.callback(
    Output('wheels-output', 'children'),
    [Input('wheels', 'value')])

@app2.callback(
    Output('color-output', 'children'),
    [Input('color', 'value')])

@app2.callback(
    Output('display-image','src'),
    [Input('wheels', 'value'),
     Input('color', 'value')])

def callback_a(wheels_value):
    return 'You selected: {}'.format(wheels_value)

def callback_b(color_value):
    return 'You selected: {}'.format(color_value)

def callback_image(wheel,color):
    path='~/Plotly-Dashboards-with-Dash/Data/Images/'
    return encode_image(path+df[(df['wheels']==wheel) & (df['color']==color)]['image'].values[0])

if __name__ == '__main__':
    app2.run_server(debug=True)
