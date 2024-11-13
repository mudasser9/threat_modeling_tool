import dash
from dash import dcc, html
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from db_config import get_db_connection

# Create Dash app
def create_dfd_app(flask_app):
    dash_app = dash.Dash(__name__, server=flask_app, url_base_pathname='/dash/')

    # Sample data fetch function
    def fetch_data():
        conn = get_db_connection()
        query = "SELECT category, value FROM sample_data_table"  # Replace with your actual query
        df = pd.read_sql(query, conn)
        conn.close()
        return df

    # Fetch initial data
    df = fetch_data()

    # Create sample plots
    bar_fig = px.bar(df, x='category', y='value', title="Sample Bar Graph")
    line_fig = px.line(df, x='category', y='value', title="Sample Line Graph")

    # Layout for the dashboard
    dash_app.layout = html.Div(children=[
        html.H1(children='Dashboard'),

        html.Div(children='''
            This dashboard shows sample data visualizations.
        '''),

        dcc.Graph(
            id='bar-graph',
            figure=bar_fig
        ),

        dcc.Graph(
            id='line-graph',
            figure=line_fig
        )
    ])

    return dash_app
