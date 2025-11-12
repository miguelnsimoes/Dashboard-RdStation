from dash import html
import dash_bootstrap_components as dbc
import pandas as pd

def ranking_lps(dados: pd.DataFrame):
    dados_ranking = dados.copy()
    dados_ranking['conversion_rate'] = pd.to_numeric(dados_ranking['conversion_rate'])
    dados_ranking['visits_count'] = pd.to_numeric(dados_ranking['visits_count'])
    dados_ranking['conversion_count'] = pd.to_numeric(dados_ranking['conversion_count'])

    dados_ordenados  = dados_ranking.sort_values(by='conversion_rate', ascending=False)
    
    linhas_ranking = []
    for i, lp in (dados_ordenados.iterrows()):
        header = dbc.Row(
            [
                dbc.Col(html.H2(f'{index + 1}'))
            ]
        )