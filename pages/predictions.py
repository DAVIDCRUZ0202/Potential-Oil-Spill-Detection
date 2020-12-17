# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

from joblib import load
pickle = load('pickle.joblib')
# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            Customize the pipeline type and the longitude location below


            """
        ),
        dcc.Dropdown(
            id='Pipeline Type',
            className='Pipeline Type',
            options=[
                {'label': 'ABOVEGROUND', 'value': 'ABOVEGROUND'},
                {'label': 'UNDERGROUND', 'value': 'UNDERGROUND'},
                {'label': 'TANK', 'value': 'TANK'},
                {'label': 'TRANSITION AREA', 'value': 'TRANSITION AREA'}
            ],
            placeholder='Choose a Pipeline Type'),
    ],
)
column2 = dbc.Col(
    [           
           dcc.Markdown(
            """
                          Longitude Location
            """
        ),
        dcc.Slider(
            id='Accident Longitude',
            className='Longitude Location',
            min = -158,
            max = 104,
            step = 10,
            value = -95,
            marks = {n: str(n) for n in range(-140,100,20)},
        )
    ],
)
column3 = dbc.Col(
    [
        html.H4('Accident Type', className='mb-3'), 
        html.Div(id='prediction-content', className='lead')
    ]
)

import pandas as pd

@app.callback(
    Output('prediction-content', 'children'),
    [Input('Pipeline Type', 'value'), Input('Accident Longitude', 'value')],
)
def prediction(Pipeline_type, Accident_longitude):
    df9 = pd.DataFrame(
        columns=['Pipeline Type', 'Accident Longitude'], 
        data=[[Pipeline_type, Accident_longitude]]
    )
    y_pred9 = pickle.predict(df9)[0]
    return y_pred9

layout = dbc.Row(column1), dbc.Row(column2), dbc.Row(column3)