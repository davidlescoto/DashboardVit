import dash
#from dash import Dash, html
import dash_bootstrap_components as dbc
from dash import html
#import sys
#sys.path.insert(0, '../')

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, pages_folder = "../pages",use_pages=True)
#server = app.server
app._favicon = ("favicon.ico")
header = dbc.Navbar(
    dbc.Container(
        [
	
            dbc.Row([
                dbc.NavbarToggler(id="navbar-toggler"),
                    dbc.Nav([
                        dbc.NavLink(page["name"], href=page["path"])
                        for page in dash.page_registry.values()
                        # Paginas que no van en el nav principal
                        if not page["path"].startswith("/paginas-")
			            #if not page["path"].startswith("/paginas_")
                        #if not page["path"].startswith("/paginas-estrategico")
                        #if not page["path"].startswith("/paginas-inversiones")
                    ])
            ]),
	    	    dbc.Row(
                    [
                        
                        dbc.Col(dbc.NavbarBrand("Dashboard|Vitesse", className="ms-2", style = {'font-size':'10px'})),
                    ])
        ],
        fluid=True,
    ),
    dark=True,
    color='primary',
    className = "navbar navbar-xpand-lg bg-dark mb-2"
)


app.layout = dbc.Container([header, dash.page_container], fluid=True)

if __name__ == '__main__':
	app.run_server(debug = True, port = "8040")