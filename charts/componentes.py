import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc

import sys
# adding charts to the system path

from charts.colors import graphics_colors as gc




def make_dropdown(id, value, options = []):
    dropdown = dcc.Dropdown(
    options,
    id = id,
    value = value,
    className="custom-dropdown text-body-secondary",
    style = {
        'border': '.1 px solid black',
        "fontSize":12
},
    clearable=False)
    return dropdown


def make_card (header:str, id:str, className = "card text-white bg-primary mb-3"):
    card = dbc.Card(
        [
            dbc.CardHeader(header),
            dbc.CardBody(
                [
                    dcc.Markdown(id = id)
                    
                ]
            )
        ],
        className = className
    )
    
    return card