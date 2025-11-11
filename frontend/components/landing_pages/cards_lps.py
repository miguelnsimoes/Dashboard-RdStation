import dash_bootstrap_components as dbc
from dash import html
import pandas as pd


def card_visitas(dados: pd.DataFrame):
    try:
        total_visitas = pd.to_numeric(dados['visits_count']).sum()
    except Exception as e:
        print(f"Erro em card_visitas: {e}")
        total_visitas = 0
    
    return dbc.Card(
        dbc.CardBody([
            html.H6("Volume de Visitas", className="card-title"),
            html.H3(f"{total_visitas:,.0f}", className="card-text"), 
            html.P("Total de visitas no período", className="text-secondary")
        ]),
        style={
            'backgroundColor': '#0d1b2a', 'color': 'white',
            'border': '2px solid #08B9FF', 'borderRadius': '10px',
            'textAlign': 'center', 'padding': '5px'
        }
    )   


def card_leads(dados: pd.DataFrame):
    try:
        total_leads = pd.to_numeric(dados['conversion_count']).sum()
    except Exception as e:
        print(f"Erro em card_leads: {e}")
        total_leads = 0

    return dbc.Card(
        dbc.CardBody([
            html.H6("Total de Leads", className="card-title"),
            html.H3(f"{total_leads:,.0f}", className="card-text"), 
            html.P("Total de leads gerados no período", className="text-secondary")
        ]),
        style={
            'backgroundColor': '#0d1b2a', 'color': 'white',
            'border': '2px solid #08B9FF', 'borderRadius': '10px',
            'textAlign': 'center', 'padding': '5px'
        }
    )

def card_taxa_conversao(dados: pd.DataFrame):
    try:
        total_visitas = pd.to_numeric(dados['visits_count']).sum()
        total_leads = pd.to_numeric(dados['conversion_count']).sum()
        
        if total_visitas > 0:
            taxa_media = (total_leads / total_visitas) * 100
        else:
            taxa_media = 0
    except Exception as e:
        print(f"Erro em card_taxa_conversao: {e}")
        taxa_media = 0

    return dbc.Card(
        dbc.CardBody([
            html.H6("Taxa de Conversão Média", className="card-title"),
            html.H3(f"{taxa_media:.2f}%", className="card-text"), 
            html.P("Média (Leads / Visitas) no período", className="text-secondary")
        ]),
        style={
            'backgroundColor': '#0d1b2a', 'color': 'white',
            'border': '2px solid #08B9FF', 'borderRadius': '10px',
            'textAlign': 'center', 'padding': '5px'
        }
    )


def container_cards_lps(dados: pd.DataFrame):
    
    if dados.empty:
        return None 

    return dbc.Row(
        [
            dbc.Col(card_visitas(dados), md=4),
            dbc.Col(card_leads(dados), md=4),
            dbc.Col(card_taxa_conversao(dados), md=4),
        ],
        className="g-3 d-flex align-items-stretch",
    )