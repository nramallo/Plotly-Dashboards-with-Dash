import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

df=pd.read_csv('~/Plotly-Dashboards-with-Dash/Data/gapminderDataFiveYear.csv')

''' app4=dash.Dash()

app4.layout = html.Div([
    dcc.Input(id='my-id',value='Initial Value' ,type='text'),
    html.Div(id='my-div')
])

if __name__=='__main__':
    app4.run_server()

@app4.callback(Output('my-div',component_property='children'),
               [Input(component_id='my-id',component_property='value')])

def update_output_div(input_val):
    return 'You entered "{}"'.format(input_val) '''

app = dash.Dash()

year_options=[]
for year in df['year'].unique():
    year_options.append({'label':str(year),'value':year})

app.layout = html.Div([
    dcc.Graph(id='my-graph'),
    dcc.Dropdown(id='year-picker',options=year_options,
                 value=df['year'].min())
])

@app.callback(Output('my-graph', 'figure'),
              [Input('year-picker', 'value')])

def update_graph(year):
    fitlered_df=df[df['year']==year]

    traces=[]

    for cont_name in fitlered_df['continent'].unique():
        df_by_cont=fitlered_df[fitlered_df['continent']==cont_name]
        traces.append(go.Scatter(
            y=df_by_cont['lifeExp'],
            x=df_by_cont['gdpPercap'],
            name=cont_name,
            mode='markers',
            opacity=0.7,
            marker = {'size': 15}
            ))

    return {'data':traces,'layout':go.Layout(title='My Graph',
                                             xaxis={'title':'GDP per Capita','type':'log'},
                                             yaxis={'title':'Life Expectancy'}
                                             )}

if __name__ == '__main__':
    app.run_server(debug=True)
