import sys
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs  as go
from dash.dependencies import Input, Output
from importlib import import_module
predictions=__import__('predictions')
import_module('predictions')
#from .predictions import resul

os.system("C:/Users/LENOVO/flaskedacy/flasktuto/")

tables=predictions.resul
df1 = pd.DataFrame(tables)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', dbc.themes.BOOTSTRAP]

df = pd.read_csv('D:/talent.csv', sep=';')
#print(df.head())
colors = ['red', 'blue', 'black', 'green']

features = df.groupby('genre').agg('parti').count()
background = df.groupby('background').agg('parti').count()
corh = df.groupby('cohorte').agg('parti').count()
#print(background)

retards = df.groupby('cohorte').agg('retards').count()
absences = df.groupby('cohorte').agg('absences').count()

trace1 = go.Bar(x=df['genre'], y=features, name='Oui', marker={'color':'#FFD700'})
trace2 = go.Bar(x=df['genre'], y=features, name='Non', marker={'color':'#9EA0A1'})

data1=[trace1, trace2]

ret1 = go.Scatter(x=df['cohorte'], y=retards, mode='markers', name='cohorte 7', marker=dict(size=[40, 60, 80],
                color=[0, 1, 2]))
ret2 = go.Scatter(x=df['cohorte'], y=retards, mode='markers', name='cohorte 6', marker=dict(size=[40, 60, 80],
                color=[0, 1, 2]))
ret3 = go.Scatter(x=df['cohorte'], y=retards, mode='markers', name='cohorte 5', marker=dict(size=[40, 60, 80],
                color=[0, 1, 2]))

abs1 = go.Scatter(x=df['cohorte'], y=absences, mode='markers', name='cohorte 7', marker=dict(size=[40, 60, 80, 100],
                color=[0, 1, 2]))
abs2 = go.Scatter(x=df['cohorte'], y=absences, mode='markers', name='cohorte 6', marker=dict(size=[40, 60, 80, 100],
                color=[0, 1, 2]))
abs3 = go.Scatter(x=df['cohorte'], y=absences, mode='markers', name='cohorte 5', marker=dict(size=[40, 60, 80, 100],
                color=[0, 1, 2]))

back1 = go.Bar(x=df['background'], y=background, name='Oui', marker={'color':'#FFD700'})
back2 = go.Bar(x=df['background'], y=background, name='Non', marker={'color':'#9EA0A1'})

cohorte = [go.Pie(labels=df['cohorte'], values=corh, name='Oui')]


data2=[ret1, ret2, ret3]
data3=[abs1, abs2, abs3]
data4=[back1, back2]

data =[go.Histogram(x=df['age'], xbins=dict(start=18, end=30, size=1))]

import flask

app = dash.Dash(external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dcc.Location(id="url"),
        #html.Div(id='page-content'),
        dbc.NavbarSimple(
            children=[
                dbc.NavLink("Visualisation", href="/visualisation", id="page-1-link", style={'font-size': '15px'}),
                dbc.NavLink("Prédictions", href="/predictions", id="page-2-link", style={'font-size': '15px'}),
                dbc.NavLink("A propos", href="/page-3", id="page-3-link", style={'font-size': '15px'}),
               # dbc.NavLink("A propos", href="/page-4", id="page-4-link"),
            ],
            brand="EDACY",
            color="black",
            dark=True,
            brand_style={'color':'yellow', 'font-size': '30px'},
            style={
            'width': '100%',
            'height': '60px',},
        ),

        dbc.Container(id="page-content", className="pt-12"),

        html.Div([
            html.Div([
                dcc.Graph(id='bar',
                     figure={'data':data1,
                         'layout':go.Layout(title='Genre', barmode='stack', yaxis={'tickformat': ',d'})}
                )
            ], className="six row"),
            html.Div([
                dcc.Graph(id='scatterplot2',
                     figure={'data':data,
                         'layout':go.Layout(title='Age')}
                )
            ], className="six row"),
            html.Div([
                dcc.Graph(id='scatterplot3',
                          figure={'data': data2,
                                  'layout': go.Layout(title='Cohorte Retards', xaxis={'title': 'cohorte'},
                                yaxis={'title':'Nbre retards'})}
                          )
            ], className="six row"),
            html.Div([
                dcc.Graph(id='scatterplot4',
                          figure={'data': data3,
                                  'layout': go.Layout(title='Cohorte Absences', xaxis={'title': 'cohorte'},
                                yaxis={'title':'Nbre Absences'})}
                          )
            ], className="six row"),
            html.Div([
                dcc.Graph(id='scatterplot5',
                          figure={'data': data4,
                                  'layout': go.Layout(title='Background', barmode='group', yaxis={'tickformat': ',d'})}
                          )
            ], className="six row"),
            html.Div([
                dcc.Graph(id='scatterplot6',
                          figure={'data': cohorte,
                                  'layout': go.Layout(title='Taux De Départ')}
                          )
            ], className="six row"),
        ], className="row"),


    ])

@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]

# page_2_layout = html.Div([
#     html.H1('Page 2'),
#
#         table = dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True)
# ])



@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/visualisation"]:
        return True
    elif pathname == "/predictions":
        return dbc.Table.from_dataframe(df1, striped=True, bordered=True, hover=True)
    elif pathname == "/page-3S":
        return html.P("Oh cool, this is page 4!")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == '__main__':
    app.debug = True
    app.run_server()