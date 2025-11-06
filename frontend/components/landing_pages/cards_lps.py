import dash_bootstrap_components as dbc
from dash import html
import pandas as pd


def card_visitas(dados: pd.DataFrame):
    
    
    total_visitas = dados['qtd_visitas'].sum()

    return dbc.Card(
        dbc.CardBody([
            html.H6("Volume de Visitas", className="card-title"),
            html.H3(f"{total_visitas:,.0f}", className="card-text"),
            html.P("Total de visitas no período", className="text-secondary")
        ]),
        style={
            'backgroundColor': '#0d1b2a',
            'color': 'white',
            'border': '2px solid #08B9FF',
            'borderRadius': '10px',
            'textAlign': 'center',
            'padding': '5px'
        }
    )

def card_leads(dados: pd.DataFrame):
    
    total_leads = dados['qtd_conversoes'].sum()

    return dbc.Card(
        dbc.CardBody([
            html.H6("Total de Leads", className="card-title"),
            html.H3(f"{total_leads:,.0f}", className="card-text"),
            html.P("Total de leads gerados no período", className="text-secondary")
        ]),
        style={
            'backgroundColor': '#0d1b2a',
            'color': 'white',
            'border': '2px solid #08B9FF',
            'borderRadius': '10px',
            'textAlign': 'center',
            'padding': '5px'
        }
    )
