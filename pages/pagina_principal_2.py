import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go


import pandas as pd
from datetime import datetime 
import sys
sys.path.insert(0, '../')
from pages.paginas_1.paginas_1_side_bar import sidebar

#imports de modulo del dashboard
from charts.componentes import make_dropdown, make_card

from charts.charts import *
dash.register_page(__name__)


#---- DATA ---------------------------
DATA_PATH = "../data/"

# tipo de cambio
tipo_cambio = pd.read_excel(DATA_PATH+"precio_dolar.xlsx")
tipo_cambio_compra = tipo_cambio[tipo_cambio['Tipo de Precio']=='Compra'][["Fecha", "Precio"]]

# Inversiones
distribucion_cartera = pd.read_excel(DATA_PATH + "tablas_informe_trimestral_inversiones.xlsx", 
                                     sheet_name="distribución inversiones")

# vencimientos
distribucion_vencimiento = pd.read_excel(DATA_PATH+"tablas_informe_trimestral_inversiones.xlsx", 
                                         sheet_name="distribución vencimiento")[["Vencimiento", "Monto"]]

distribucion_vencimiento = distribucion_vencimiento.sort_values("Monto", ascending = False)
distribucion_vencimiento["Vencimiento"] = [str(value.year) for value in distribucion_vencimiento.Vencimiento]

# meses
meses = distribucion_cartera.columns[1:]

#---- PLOTS --------------------------
bar_plot = dcc.Graph(id = "id-bar")
line_plot = dcc.Graph(id = "id-scatter")
pie_plot = dcc.Graph(id = "id-pie")

month_dropdown = make_dropdown(id = "mes-dropdown", value = meses[0],options = meses )

def layout():
    return html.Div([
    

    dbc.Row(
        [
            dbc.Col(
                [       sidebar(),
                        month_dropdown
                 

               ], 
                width={"size": 3, "order": 1}),

            dbc.Col(
                [
                dcc.Markdown("## Gráfico pie", className="text-body-secondary my-sm-5 text-center"),
                pie_plot,
                dcc.Markdown("## Gráfico de barras", className="text-body-secondary my-sm-5 text-center"),
                bar_plot,
                dcc.Markdown("## Gráfico de linea", className="text-body-secondary my-sm-5 text-center"),
                line_plot,

                            ],
                width={ "size":9,"order": 2}),

                                
                ]
    )



])

@callback(
          Output("id-bar", "figure"),
          Output("id-scatter", "figure"),
          Output("id-pie", "figure"),
          Input("mes-dropdown", "value"))
def update_plots(mes):
    
    bar = bar_chart(dff = distribucion_vencimiento, 
                    x = "Vencimiento", y = "Monto", 
                    name = "Vencimientos")
    
    pie = pie_chart(distribucion_cartera.iloc[:4,:], 
                    "Instrumento", 
                    mes, 
                    formato = ",.4%",
                    name = "Instrumento", 
                    texttemplate="%{label}:(%{percent})")
    
    scatter = scatter_chart(tipo_cambio_compra.iloc[-30:], "Fecha", "Precio", "Compra", tickfont = 10)

    return bar, scatter, pie
