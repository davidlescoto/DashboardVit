import dash
from dash import html
import dash_bootstrap_components as dbc

def sidebar():
    nav_links = []
    for page in dash.page_registry.values():

        if page["path"]=="pages/pagina-principal-2":
            nav_links.append(
                dbc.NavLink(
                    [
                        html.Div("Pagina principal 2", className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
            )
        elif page["path"].startswith("/paginas-2/pagina-2"):
            nav_links.append(
                dbc.NavLink(
                    [
                        html.Div("Pagina 2", className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
            )


    return dbc.Nav(children=nav_links,
                   vertical=True,
                   pills=True,
                   className="mb-2")