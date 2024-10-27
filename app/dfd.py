# app/dfd.py
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

def create_dfd_app(flask_app):
    app = dash.Dash(__name__, server=flask_app, url_base_pathname='/dash/')

    app.layout = html.Div([
        dcc.Input(id='component-name', type='text', placeholder='Enter Component Name'),
        dcc.Dropdown(
            id='component-type',
            options=[
                {'label': 'Data Store', 'value': 'Data Store'},
                {'label': 'Process', 'value': 'Process'},
                {'label': 'External Entity', 'value': 'External Entity'}
            ],
            placeholder='Select Component Type'
        ),
        html.Button('Add Component', id='add-button'),
        html.Div(id='canvas', style={'border': '1px solid black', 'width': '300px', 'height': '500px', 'overflow': 'auto'})
    ])

    @app.callback(
        Output('canvas', 'children'),
        [Input('add-button', 'n_clicks')],
        [Input('component-type', 'value'), Input('component-name', 'value')]
    )
    def update_canvas(n_clicks, component_type, component_name):
        if n_clicks is None or not component_type or not component_name:
            return []
        return [html.Div(f'{component_name} ({component_type})', style={'padding': '5px'})]

    return app
