# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## How can we find accidents before they occur?

            What if we could detect problems and fix them before an accident occurs?
             Use this app to see which causal indicators you should be on the lookout for.
              Preventative maintenance is key!

            """
        ),
        dcc.Link(dbc.Button('Lets Detect!', color='primary'), href='/predictions')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.Img(src='assets/earth.jpg', className='earth'),
    ]
)

layout = dbc.Row([column1, column2])