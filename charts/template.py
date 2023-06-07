
import plotly.io as pio
import plotly.graph_objects as go
import plotly.express as px

def chart_template(dark = False):
    
    plot_bgcolor="#ffffff"
    paper_bgcolor="#ffffff"
    font_color = '#000000'
    template = 'plotly_white'

    if dark:
        plot_bgcolor="#30363d"
        paper_bgcolor="#30363d"
        font_color = '#ffffff'
        template = 'plotly_dark'


    layout = go.Layout(
            font=dict(color = font_color, family="Arial", size=12),
            plot_bgcolor=plot_bgcolor,
            paper_bgcolor=paper_bgcolor,
            xaxis = dict(griddash='dot', showline=True, linecolor = font_color),
            yaxis = dict(griddash='dot', showline=True, linecolor = font_color),
            colorway=px.colors.qualitative.Prism,
            )




    pio.templates["update_layout"] = dict(
        layout = layout,
        )

    pio.templates.default = f"{template}+update_layout"