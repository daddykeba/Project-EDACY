import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs  as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', dbc.themes.BOOTSTRAP]

df = pd.read_csv('D:/Jeu de données/talents.csv', sep=';')
#print(df.head())
colors = ['red', 'blue', 'black', 'green']

features = df.groupby('genre').agg('parti').count()

retards = df.groupby('cohorte').agg('retards').count()
absences = df.groupby('cohorte').agg('absences').count()

trace1 = go.Bar(x=df['genre'], y=features, name='Oui', marker={'color':'#FFD700'})
trace2 = go.Bar(x=df['genre'], y=features, name='Non', marker={'color':'#9EA0A1'})

data1=[trace1, trace2]

ret1 = go.Scatter(x=df['cohorte'], y=retards, mode='markers', name='cohorte 1', marker=dict(size=[40, 60, 80, 100],
                color=[0, 1, 2, 3]))
ret2 = go.Scatter(x=df['cohorte'], y=retards, mode='markers', name='cohorte 2', marker=dict(size=[40, 60, 80, 100],
                color=[0, 1, 2, 3]))
ret3 = go.Scatter(x=df['cohorte'], y=retards, mode='markers', name='cohorte 3', marker=dict(size=[40, 60, 80, 100],
                color=[0, 1, 2, 3]))
ret4 = go.Scatter(x=df['cohorte'], y=retards, mode='markers', name='cohorte 4', marker=dict(size=[40, 60, 80, 100],
                color=[0, 1, 2, 3]))

abs1 = go.Scatter(x=df['cohorte'], y=absences, mode='markers', name='cohorte 1', marker=dict(size=[40, 60, 80, 100],
                color=[0, 1, 2, 3]))
abs2 = go.Scatter(x=df['cohorte'], y=absences, mode='markers', name='cohorte 2', marker=dict(size=[40, 60, 80, 100],
                color=[0, 1, 2, 3]))
abs3 = go.Scatter(x=df['cohorte'], y=absences, mode='markers', name='cohorte 3', marker=dict(size=[40, 60, 80, 100],
                color=[0, 1, 2, 3]))
abs4 = go.Scatter(x=df['cohorte'], y=absences, mode='markers', name='cohorte 4', marker=dict(size=[40, 60, 80, 100],
                color=[0, 1, 2, 3]))

data2=[ret1, ret2, ret3, ret4]
data3=[abs1, abs2, abs3, abs4]

data =[go.Histogram(x=df['age'], xbins=dict(start=18, end=30, size=1))]

import flask

app = dash.Dash(external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dcc.Location(id="url"),
        #html.Div(id='page-content'),
        dbc.NavbarSimple(
            children=[
                dbc.NavLink("Visualisation", href="/visualisation", id="page-1-link"),
                dbc.NavLink("Corrélation", href="/page-2", id="page-2-link"),
                dbc.NavLink("Prédictions", href="/page-3", id="page-3-link"),
                dbc.NavLink("A propos", href="/page-4", id="page-4-link"),
            ],
            brand="EDACY",
            color="black",
            dark=True,
            style={'text-color':'yellow'},
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
                          figure={'data': data2,
                                  'layout': go.Layout(title='Cohorte Retards', xaxis={'title': 'cohorte'},
                                yaxis={'title':'Nbre retards'})}
                          )
            ], className="six row"),
            html.Div([
                dcc.Graph(id='scatterplot6',
                          figure={'data': data3,
                                  'layout': go.Layout(title='Cohorte Absences', xaxis={'title': 'cohorte'},
                                yaxis={'title':'Nbre Absences'})}
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

page_2_layout = html.Div([
    html.H1('Page 2'),
    dcc.RadioItems(
        id='page-2-radios',
        options=[{'label': i, 'value': i} for i in ['Orange', 'Blue', 'Red']],
        value='Orange'
    ),
    html.Div(id='page-2-content'),
    html.Br(),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go back to home', href='/')
])



@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/visualisation"]:
        return True
    elif pathname == "/page-2":
        return page_2_layout
    elif pathname == "/page-3":
        return html.P("Oh cool, this is page 3!")
    elif pathname == "/page-4":
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