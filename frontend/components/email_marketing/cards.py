from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import datetime

def extraindo_dados(dados: pd.DataFrame):
    dados_filtrados = dados[[
        'nome_campanha',
        'data_envio',
        'taxa_abertura',
        'taxa_clique'
    ]]
    
    dados_ordenados = dados_filtrados.sort_values(by='taxa_abertura', ascending=False)
    return dados_ordenados

import pandas as pd
import datetime
import dash_bootstrap_components as dbc
from dash import html

import pandas as pd
import dash_bootstrap_components as dbc
from dash import html
from datetime import datetime

def card_taxa_abertura(dados: pd.DataFrame):

    dados['data_envio'] = pd.to_datetime(dados['data_envio'], errors='coerce')

    if dados.empty:
        media_inicial = 0
        media_final = 0
        variacao = 0
    else:
        dados_ordenados = dados.sort_values('data_envio')

        metade = len(dados_ordenados) // 2
        dados_inicial = dados_ordenados.iloc[:metade]
        dados_final = dados_ordenados.iloc[metade:]
        media_inicial = dados_inicial['taxa_abertura'].mean() if not dados_inicial.empty else 0
        media_final = dados_final['taxa_abertura'].mean() if not dados_final.empty else 0

        if media_inicial > 0:
            variacao = ((media_final - media_inicial) / media_inicial) * 100
        else:
            variacao = 0

    if variacao > 0:
        cor = '#5cb85c'
        simbolo = '▲'
    elif variacao < 0:
        cor = '#d9534f'
        simbolo = '▼'
    else:
        cor = '#4e5d6c'
        simbolo = '■'

    return dbc.Card(
        dbc.CardBody([
            html.H6("Evolução da Taxa de Abertura", className="card-title"),
            html.H3(f"{media_final:.2f}%", className="card-text"),
            html.P([
                html.Span(simbolo, style={'color': cor, 'marginRight': '5px'}),
                html.Span(f"{variacao:.2f}% vs período anterior", style={'color': cor})
            ])
        ]),
        style={
            'backgroundColor': '#0d1b2a',
            'color': 'white',
            'border': f'2px solid #08B9FF',
            'borderRadius': '10px',
            'textAlign': 'center',
            'padding': '5px',
            'width': '100%',
            'maxWidth': '400px',
            'margin': '0 auto'
        }
    )


def card_taxa_clique(dados: pd.DataFrame):
    dados['data_envio'] = pd.to_datetime(dados['data_envio'], errors='coerce')

    if dados.empty:
        media_inicial = 0
        media_final = 0
        variacao = 0
    else:
        dados_ordenados = dados.sort_values('data_envio')
        metade = len(dados_ordenados) // 2
        dados_inicial = dados_ordenados.iloc[:metade]
        dados_final = dados_ordenados.iloc[metade:]

        media_inicial = dados_inicial['taxa_clique'].mean() if not dados_inicial.empty else 0
        media_final = dados_final['taxa_clique'].mean() if not dados_final.empty else 0

        if media_inicial > 0:
            variacao = ((media_final - media_inicial) / media_inicial) * 100
        else:
            variacao = 0

    if variacao > 0:
        cor = '#5cb85c'
        simbolo = '▲'
    elif variacao < 0:
        cor = '#d9534f'
        simbolo = '▼'
    else:
        cor = '#4e5d6c'
        simbolo = '■'

    return dbc.Card(
        dbc.CardBody([
            html.H6("Evolução da Taxa de Clique", className="card-title"),
            html.H3(f"{media_final:.2f}%", className="card-text"),
            html.P([
                html.Span(simbolo, style={'color': cor, 'marginRight': '5px'}),
                html.Span(f"{variacao:.2f}% vs período anterior", style={'color': cor})
            ])
        ]),
        style={
            'backgroundColor': '#0d1b2a',
            'color': 'white',
            'border': f'2px solid #08B9FF',
            'borderRadius': '10px',
            'textAlign': 'center',
            'padding': '5px',
            'width': '100%',
            'maxWidth': '400px',
            'margin': '0 auto'
        }
    )

def card_horario_melhor_engajamento(dados: pd.DataFrame):
    dados['data_envio'] = pd.to_datetime(dados['data_envio'], errors='coerce')
    dados['hora'] = dados['data_envio'].dt.hour

    medias = (
        dados.groupby('hora')[['taxa_abertura', 'taxa_clique']]
        .mean()
        .reset_index()
        .dropna()
    )

    if medias.empty:
        melhor_hora = "Sem dados"
        engajamento_medio = 0
    else:
        medias['media_engajamento'] = (medias['taxa_abertura'] + medias['taxa_clique']) / 2

        melhor_linha = medias.loc[medias['media_engajamento'].idxmax()]
        melhor_hora = f"{int(melhor_linha['hora'])}h"
        engajamento_medio = melhor_linha['media_engajamento']

    return dbc.Card(
        dbc.CardBody([
            html.H6("Melhor Horário de Engajamento", className="card-title"),
            html.H3(f"{melhor_hora}", className="card-text", style={'color': '#fffff'}),
            html.P(f"Média de engajamento: {engajamento_medio:.2f}%", className="text-secondary", style={'color': '#fffff'})
        ]),
        style={
            'backgroundColor': '#0d1b2a',
            'color': 'white',
            'border': '2px solid #08B9FF',
            'borderRadius': '10px',
            'textAlign': 'center',
            'padding': '5px',
            'width': '100%',
            'maxWidth': '400px',
            'margin': '0 auto',
            'height': '160px'
        }
    )

    
def container_cards(dados: pd.DataFrame):
    return dbc.Row(
        [
            dbc.Col(card_taxa_abertura(dados)),
            dbc.Col(card_taxa_clique(dados)),
            dbc.Col(card_horario_melhor_engajamento(dados))
        ],
        className="g-3 d-flex align-items-stretch",
    )