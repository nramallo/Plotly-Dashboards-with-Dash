import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df=pd.read_csv('~/Plotly-Dashboards-with-Dash/Data/mpg.csv')

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
    app.run_server(debug=True)
