import dash_bootstrap_components as dbc
from dash import html
import pandas as pd

from .cards_lps import container_cards_lps 
from .ranking_lps import ranking_lps 

def container_landing_pages(dados_lp: pd.DataFrame, dados_vendas: pd.DataFrame):
    
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
                    container_cards_lps(dados_lp, dados_vendas),
                    className="mb-4",
                ),
                
                dbc.Row(
                    [       
                        dbc.Col(ranking_lps(dados_lp), md=6),
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody("Aqui vai o Gráfico de Origem"),
                                style={'backgroundColor': '#0d1b2a', 'color': 'white', 'height': '100%'}
                            ),
                            md=6
                        ),
                    ],
                    className="mb-4" 
                )
            ],
            fluid=True,
        )