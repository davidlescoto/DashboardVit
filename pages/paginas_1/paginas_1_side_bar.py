import dash
from dash import html
import dash_bootstrap_components as dbc

def sidebar():
    nav_links = []
    for page in dash.page_registry.values():

        if page["path"]=="/pagina-principal-1":
            nav_links.append(
                dbc.NavLink(
                    [
                        html.Div("Ejemplo plotly", className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
            )
        elif page["path"].startswith("/paginas-1/pagina-2"):
            nav_links.append(
                dbc.NavLink(
                    [
                        html.Div("Gráficos prueba", className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
            )


    return dbc.Nav(children=nav_links,
                   vertical=True,
                   pills=True,
                   className="mb-2")