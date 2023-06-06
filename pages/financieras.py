import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc



import pandas as pd
import sys
sys.path.insert(0, '../')


#imports de modulo del dashboard
from charts.componentes import make_dropdown, make_card
from utils.functions import *

from charts.charts import *
dash.register_page(__name__)


#---- DATA ---------------------------

PATH_DATA = "https://raw.githubusercontent.com/davidlescoto/data_sets/main/vitesse_dataset.csv"

#----------------CLEAN DATA----------------------------------------
df = pd.read_csv(PATH_DATA)
dff = clean_data(df)


#----------------ID´S----------------------------------------

id_euribor = "id-euroibor-graph"
id_index_price = "id-index-price-graph"
id_confidence = "id-emp-ratio-graph"

#----------------CHARTS----------------------------------------
## 1. EUROIBOR
graph = dcc.Graph()
euro = cohorte_numericas(dff, "euribor3m")
euro_graph = bar_group_cohor(euro, x = "euribor3m", y = "y", values = "Total")
euro_graph = dcc.Graph(id = id_euribor,figure =  euro_graph)

## 2. PRICE INDEX
price_index = cohorte_numericas(dff, "cons.price.idx")
price_index_graph = bar_group_cohor(price_index, x = "cons.price.idx", y = "y", values = "Total")
price_index_graph = dcc.Graph(id = id_index_price, figure=price_index_graph)

## 2. CONFIDENCE
confidence = cohorte_numericas(dff, "cons.conf.idx")
confidence_graph = bar_group_cohor(confidence, x = "cons.conf.idx", y = "y", values = "Total")
confidence_graph = dcc.Graph(id = id_confidence, figure=confidence_graph)

#----------JUMBOTRON------------------------------------------------
jumbotron = html.Div(
    dbc.Container(
        [
            html.H1("Oberve", className="display-3"),
            html.Ul(
            children=[
                html.Li("Según los datos analizados, se observa una aparente relación negativa entre la contratación de certificados y las tasas de interés Euribor. Esta relación puede resultar poco intuitiva a primera vista, ya que se esperaría que a medida que las tasas de interés aumenten, aumente la contratación de certificados debido a su atractivo como opción de inversión segura."),
                html.Li("Al examinar la relación entre el índice de precios y la contratación de certificados, no se identifica una correlación clara. Se observa que en los extremos de los cohortes de índice de precios, se contratan certificados, lo cual puede indicar que otros factores o variables influyen en la decisión de contratar un certificado, independientemente del nivel de precios."),
            ]
        )
            ,
            html.Hr(className="my-2 bg-dark")
        ],
        fluid=True,
        className="py-3 ",
    ),
    className="p-3 bg-dark rounded-3",
)

#------------FOOTER--------------
footer =  html.Div(
    dbc.Container(
        [
            html.Footer(
            children=[
                html.P("Realizado por Jóse López,  2023.")
            ]
        )
        ],
        fluid=True,
        className="py-100 ",
    ),
    className="p-3 bg-dark mt-5",
)

second_row =     dbc.Row(
        [
            dbc.Col(
                [       
            dcc.Markdown("## Confidence rate", className="text-body-secondary my-sm-5 text-center"),
                 confidence_graph

               ], 
                width={"size": 10, "order": 1, "offset":1}),

                                
                ]
    )

def layout():
    return html.Div([
    
        # first row
    jumbotron,
    dbc.Row(
        [
            dbc.Col(
                [       
            dcc.Markdown("## EuroIbor", className="text-body-secondary my-sm-5 text-center"),
                 euro_graph

               ], 
                width={"size": 5, "order": 1, "offset":1}),

            dbc.Col(
                [
            dcc.Markdown("## Price index", className="text-body-secondary my-sm-5 text-center"),
            price_index_graph
                            ],
                width={ "size":5,"order": 2}),

                                
                ]
    ),
    footer
# Second row
    #second_row



])