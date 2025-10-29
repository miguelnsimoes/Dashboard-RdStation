import dash_bootstrap_components as dbc
from dash import Dash, dcc, Input, Output, html


def cards(dados):
    return  dbc.Row([
    dbc.Col([
        dbc.Card([
            dbc.CardHeader('Evolução da taxa de abertura'),
            dbc.CardBody(html.H3('25%')),
        ])
    ], className='mb-4'),

    dbc.Col([
        dbc.Card([
            dbc.CardHeader('Evolução da taxa de abertura'),
            dbc.CardBody(html.H3('25%')),
        ])
    ], className='mb-4'),

    dbc.Col([
        dbc.Card([
            dbc.CardHeader('Evolução da taxa de abertura'),
            dbc.CardBody(html.H3('25%')),
        ])
    ], className='mb-4'),

    dbc.Col([
        dbc.Card([
            dbc.CardHeader('Evolução da taxa de abertura'),
            dbc.CardBody(html.H3('25%')),
        ])
    ], className='mb-4')  
    ], className='d-flex flex-column justify-content-center align-items-center', style={'gap' : '60px'})