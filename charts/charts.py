

import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from charts.template import chart_template



chart_template(dark = True)

def spinner(graph):
    graph_spinner = dbc.Spinner([ graph],size="lg", color="primary", type="border")
    return graph_spinner


#------------ SCATTER CHART------------------------------------------------------------
def scatter_chart(df, x, y, name = "x", dtick="M1", tickformat="%m-%Y", tickfont = 7, annotation_font_size = 10):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df[x],
        y=df[y],
        mode="lines+text",
        name=name,
    ))

    fig.update_layout(annotations=[
                go.layout.Annotation(
                x=df[x].iloc[i],
                y = df[y].iloc[i],
                xref="x",
                yref="y",
                text= df[y].iloc[i],
                align='center',
                showarrow=False,
                yanchor='bottom',
                textangle=90,
                font=dict(size = annotation_font_size)) for i in range(len(df[y])) ])
    fig.update_xaxes(
        dtick=dtick,
        tickformat=tickformat,
        tickfont   = dict(size = 7))

    fig.update_layout(
            margin={'t': 30},
            )
    return fig


#------------ PIE CHART------------------------------------------------------------
def pie_chart(df, x, y, formato, name = "x", texttemplate = "%{label}: %{value:,.2f} <br>(%{percent})"):
    fig = go.Figure(
        data=[
            go.Pie(
                values=df[y], 
                labels=df[x], 
                #text = dff[y],
                texttemplate = texttemplate,
                hole=.5, 
                name = name,
                hovertemplate = '%{text:' + f'{formato}' + '}',
                hovertext = df[y],
                scalegroup='one'

            )

        ])
    fig.update_traces(textposition='outside', textinfo='percent+value+label')
    return fig



#------------ BAR CHART------------------------------------------------------------
def bar_chart(dff, x,y, formato = ",.2f", unidades = "L", name = "y"):
    #dff = dff.sort_values(y, ascending = False)
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
                x=dff[x],
                y=dff[y],
                name = name,
                text = dff[y],
                texttemplate = f'{unidades}'+'%{text:' + f'{formato}' + '}',
                hovertemplate = '%{text:' + f'{formato}' + '}',
               ))

    #fig.update_layout(barmode='stack')


    fig.update_xaxes(
        tickangle = -45,
        tickfont   = dict(size = 8),
        title_font = dict(size = 20),
        title_standoff = 25,
        showline = False)

    fig.update_yaxes(
        zeroline=False,
        showline=False,
        showticklabels=True,
        tickformat = formato,
        tickfont   = dict(size = 8))
    fig.update_traces( textposition="auto", textfont_size=10)
    fig.update_layout( uniformtext_minsize=12)
    return fig


def bar_group(dff, x, y):
    y_values = dff[y].unique()
    data = []
    for value in y_values:
        dfff = dff[dff[y]==value]
        dfff = dfff.groupby([x]).count().reset_index()
        xx = dfff[x].to_list()
        yy = dfff[y].to_list()
        data.append(go.Bar(name = value, x = xx ,y = yy ))


    fig = go.Figure(data=data)
    # Change the bar mode
    fig.update_layout(barmode='group')
    return fig

def bar_group_cohor(dff, x, y, values):

    y_values = dff[y].unique()
    data = []
    
    for value in y_values:
        dfff = dff[dff[y]==value]
        
        xx = [str(index) for index in dfff[x].to_list()]
        yy = dfff[values].to_list()
        data.append(go.Bar(name = value, x = xx ,y = yy ))


    fig = go.Figure(data=data)
    # Change the bar mode
    fig.update_layout(barmode='group')
    return fig