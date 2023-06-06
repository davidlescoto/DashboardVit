import dash_bootstrap_components as dbc
from dash import html
import dash

dash.register_page(__name__)

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
        className="py-5",
    ),
    className="p-3 bg-dark mt-5",
)


jumbotron = html.Div(
    dbc.Container(
        [
            html.H1("Dashboard de prueba Vitesse", className="display-3"),
            html.P(
                "Este dashboard presenta un resumen visual de los datos recopilados durante la campaña de marketing realizada mediante llamadas telefónicas para una institución bancaria portuguesa. Aquí encontrarás información clave y métricas relevantes que te permitirán comprender el rendimiento y los resultados de la campaña de manera rápida y concisa. Explora los gráficos interactivos y desgloses detallados para obtener una visión clara de la efectividad de la campaña y descubrir posibles oportunidades de mejora.",

                className="lead",
            ),
            html.Hr(className="my-2 bg-dark")
        ],
        fluid=True,
        className="py-3 ",
    ),
    className="p-3 bg-dark rounded-3",
)

def layout():
    return html.Div([
        jumbotron,
        footer
                     
                     ])