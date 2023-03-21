import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

app4=dash.Dash()

app4.layout = html.Div([
    dcc.Input(id='my-id',value='Initial Value' ,type='text'),
    html.Div(id='my-div')
])

if __name__=='__main__':
    app4.run_server()

@app4.callback(Output('my-div',component_property='children'),
               [Input(component_id='my-id',component_property='value')])

def update_output_div(input_val):
    return 'You entered "{}"'.format(input_val)
