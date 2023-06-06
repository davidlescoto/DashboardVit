import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go


import pandas as pd
from datetime import datetime 
from pages.paginas_1.paginas_1_side_bar import sidebar

#imports de modulo del dashboard
from charts.componentes import make_dropdown, make_card

from charts.charts import *
dash.register_page(__name__)


def layout():
    return html.Div([
    

    dbc.Row(
        [
            dbc.Col(
                [       sidebar()

               ], 
                width={"size": 3, "order": 1}),

            dbc.Col(
                [
                dcc.Markdown("# Pagina Principal", className="text-secondary my-sm-5 text-center"),
                            ],
                width={ "size":9,"order": 2}),

                                
                ]
    )


])
