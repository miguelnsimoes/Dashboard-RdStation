import dash_bootstrap_components as dbc
from dash import Dash, dcc, Input, Output, html
import pandas as pd


def tabela(dados):
    df = pd.DataFrame(dados['emails'])
    return dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)

