import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.figure_factory as ff

import pandas as pd

import sys
sys.path.insert(0, '../')

#imports de modulo del dashboard

from utils.functions import *

from charts.charts import *
dash.register_page(__name__)

PATH_DATA = "https://raw.githubusercontent.com/davidlescoto/data_sets/main/vitesse_dataset.csv"

#----------------CLEAN DATA----------------------------------------
df = pd.read_csv(PATH_DATA)
dff = clean_data(df)

#----------------ID´S----------------------------------------
#demográficas
id_age = "id-age-graph"
id_campaing = "id-campaing-graph"
id_marital = "id-marital-graph"
id_education = "id-education-graph"
id_poutcome = "id-poutcome-graph"
id_month = "id-month-graph"
id_job = "id-job-graph"
id_contact = "id-contact"
#----------------CHARTS----------------------------------------
## 1. AGE
age = dff.age.to_list()
age_graph = ff.create_distplot([age], ["age"],
                         bin_size=.2, show_rug=False)

age_graph = dcc.Graph(id = id_age, figure=age_graph)
graph = dcc.Graph()

## 2. CAMPAING
campaign = dff.campaign.to_list()
campaign_graph = ff.create_distplot([campaign], ["Campaing"],
                         bin_size=.2, show_rug=False)
campaign_graph = dcc.Graph(id = id_campaing,figure = campaign_graph)

## 3. MARITAL
marital_graph = bar_group(dff, x="marital", y="y")
marital_graph = dcc.Graph(id = id_marital, figure = marital_graph)

## 4. EDUCATION
education_graph = bar_group(dff, x="education", y="y")
education_graph = dcc.Graph(id = id_education, figure = education_graph)

## 5. POUTCOME
poutcome_graph = bar_group(dff, x="poutcome", y="y")
poutcome_graph = dcc.Graph(id = id_poutcome, figure = poutcome_graph)

## 6. MONTH
month_graph = bar_group(dff, x="month", y="y")
month_graph = dcc.Graph(id = id_month, figure = month_graph)

## 7. JOB
job_graph = bar_group(dff, x="job", y="y")
job_graph = dcc.Graph(id = id_job, figure = job_graph)

## 8. CONTACT
contact_graph = bar_group(dff, x="contact", y="y")
contact_graph = dcc.Graph(id = id_contact, figure = contact_graph)

#----------JUMBOTRON------------------------------------------------
jumbotron = html.Div(
    dbc.Container(
        [
            html.H1("Oberve", className="display-3"),
            html.Ul(
            children=[
                html.Li("La mayoría de los encuestados tienen edades comprendidas entre los 20 y 40 años, lo que indica que esta franja de edad es la más representativa en el estudio."),
                html.Li("Las primeras campañas han tenido un impacto significativo y han generado resultados positivos en comparación con las campañas posteriores."),
                html.Li("Entre los encuestados, la profesión más común es la 'administrativa'. Curiosamente, los encuestados con esta profesión son los que más han contratado certificados."),
                html.Li("Se observa un mejor desempeño en las llamadas realizadas a números de teléfono móvil en comparación con las llamadas a teléfonos fijos."),
                html.Li("La mayoría de los encuestados que han aceptado la oferta de certificados están casados, seguidos por los solteros."),
                html.Li("Las personas con educación universitaria muestran una mayor tendencia a contratar certificados en comparación con los encuestados con otros niveles de educación."),
                html.Li("Mayo es el mes en el que se registra la mayor cantidad de llamadas realizadas por parte del banco durante la campaña.")
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
    className="p-3 bg-darks mt-5",
)

def layout():
    return html.Div([

        # first row
    jumbotron, 
    dbc.Row(
        [
            dbc.Col(
                [       
            dcc.Markdown("## Distribución de edad", className="text-body-secondary my-sm-5 text-center"),
            age_graph

               ], 
                width={"size": 5, "order": 1, "offset":1}),

            dbc.Col(
                [
            dcc.Markdown("## Distribución de Campaing", className="text-body-secondary my-sm-5 text-center"),
            campaign_graph
                            ],
                width={ "size":5,"order": 2}),

                                
                ]
    ),
 # CERO row
    dbc.Row(
        [
            dbc.Col(
                [       
            dcc.Markdown("## JOB según respuesta", className="text-body-secondary my-sm-5 text-center"),
                 job_graph

               ], 
                width={"size": 5, "order": 1, "offset":1}),

            dbc.Col(
                [
            dcc.Markdown("## Distribución de Contact", className="text-body-secondary my-sm-5 text-center"),
            contact_graph
                            ],
                width={ "size":5,"order": 2})

                                
                ]
    ),

# Second row
    dbc.Row(
        [
            dbc.Col(
                [       
            dcc.Markdown("## Marital según respuesta", className="text-body-secondary my-sm-5 text-center"),
                 marital_graph

               ], 
                width={"size": 5, "order": 1, "offset":1}),

            dbc.Col(
                [
                dcc.Markdown("## Education según respuesta", className="text-body-secondary my-sm-5 text-center"),
                education_graph
                            ],
                width={ "size":5,"order": 2}),

                                
                ]
    ),
# third row
    dbc.Row(
        [
            dbc.Col(
                [       
            dcc.Markdown("## Outcome según respuesta", className="text-body-secondary my-sm-5 text-center"),
                 poutcome_graph

               ], 
                width={"size": 5, "order": 1, "offset":1}),

            dbc.Col(
                [
            dcc.Markdown("## Month según respuesta", className="text-body-secondary my-sm-5 text-center"),
            month_graph
                            ],
                width={ "size":5,"order": 2}),

                                
                ]
    ),
    footer    

])
