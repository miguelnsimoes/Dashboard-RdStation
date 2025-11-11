import dash_bootstrap_components as dbc
from dash import html
import pandas as pd

from .cards_lps import container_cards_lps

def container_landing_pages(dados: pd.DataFrame):
    if dados.empty:
        return dbc.Alert(
            "nenhum dado da lp encontrado",
            color="warning",
            className="m-3"
        )

    return dbc.Container(
        [
            dbc.Row(
                html.H1("Performance de Landing Pages", style={'color': 'white'}),
                className="mb-4",
            ),
            dbc.Row(
                container_cards_lps(dados),
                className="mb-4",
            ),
            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody("card"),
                        style={'backgroundColor': '#0d1b2a', 'color': 'white'}
                    ),
                    md=6
                )
            )
        ],
        fluid=True,
    )