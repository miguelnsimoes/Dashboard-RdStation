import dash_bootstrap_components as dbc
from dash import html
import pandas as pd

from .cards_lps import container_cards_lps 
from .ranking_lps import ranking_lps 
from .grafico_origem import grafico_origem_visual

def container_landing_pages(dados_lp: pd.DataFrame, dados_lp_anterior: pd.DataFrame, dados_vendas: pd.DataFrame):
    
    if dados_lp.empty:
        return dbc.Alert(
            "nenhum dado da lp encontrado",
            color="warning",
            className="m-3"
        )
    
    if dados_vendas.empty:
        print("nenhum dado de vendas CRM foi encontrado")

    return dbc.Container(
            [
                dbc.Row(
                    html.H1("Performance de Landing Pages", style={'color': 'white'}),
                    className="mb-4",
                ),
                dbc.Row(
                    container_cards_lps(dados_lp, dados_lp_anterior, dados_vendas),
                    className="mb-4 g-0",
                ),
                
                dbc.Row(
                    [      
                        dbc.Col(grafico_origem_visual(dados_vendas), md=6, style={'height': '100%'}), 
                        dbc.Col(ranking_lps(dados_lp), md=6, style={'height': '100%'}),
                        
                    ],
                    className="mb-4 g-0",
                    style={'height': '58vh'}
                )
            ],
            fluid=True,
            style={'height': '100vh', 'overflow': 'hidden', 'display': 'flex', 'flexDirection': 'column', 'padding': '10px'}
        )