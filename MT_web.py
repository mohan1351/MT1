from dash import Dash, dcc, State, Input, Output, callback_context, html, callback
import dash_bootstrap_components as dbc
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
from MT1 import *
#from app import app, server
app.title = "Machine Translation"
header = html.H1("Machine Translation App", style={'font-size':'40px', 'color':'blue', 'text-align':'center', 'background':'#D6EAF8'})
user_text_l = dcc.Textarea(
        id='textarea-example',
        placeholder= 'Enter Text',
        style={'width': '50%', 'height': 100},
    )
div_l = html.Div(id='textarea-example-output', style={'width': '50%', 'height': 100},)
app.layout = html.Div([header,user_text_l, div_l])

@callback(
    Output('textarea-example-output', 'children'),
    Input('textarea-example', 'value')
)
def update_output(web_input):
    translated_text =  translator(web_input)
    return 'Translation: \n{}'.format(translated_text)

if __name__ == '__main__':
    app.run_server(port = 8089)