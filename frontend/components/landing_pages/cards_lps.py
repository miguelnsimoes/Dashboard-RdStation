import dash_bootstrap_components as dbc
from dash import html
import pandas as pd

def card_visitas(dados: pd.DataFrame):
    total_visitas = dados['qtd_visitas'].sum()

    return dbc.Card(
        dbc.CardBody([
            html.H6("Volume de Visitas", className="card-title")
            html.H3(f"{total_visitas:,.0f}", className="card-text")
            html.P("Total de visitas no período", className="text-secondary")
        ]),
    )