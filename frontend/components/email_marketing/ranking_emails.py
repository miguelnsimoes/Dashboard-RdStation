from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd


def extraindo_dados(dados: pd.DataFrame):
    dados_filtrados = dados[[
        'nome_campanha',
        'data_envio',
        'taxa_abertura',
        'taxa_clique'
    ]]
    
    dados_ordenados = dados_filtrados.sort_values(by='taxa_abertura', ascending=False)
    return dados_ordenados

def ranking(dados: pd.DataFrame):
    dados_extraidos = extraindo_dados(dados).head()
    num_cards = len(dados_extraidos)

    rows_ranking = []

    for index, (i, dado) in enumerate(dados_extraidos.iterrows()):
        rows_ranking.append(
            dbc.Card(
                dbc.CardBody([
                    dbc.Row(
                        [
                            dbc.Col(html.H2(f'{index + 1}°', className='fw-bold'), width=1),
                            dbc.Col(html.H6(f'{dado["nome_campanha"]}', className='text-wrap'), width=9),
                            dbc.Col(html.H4(f'{round(dado["taxa_abertura"], 2)}%', style={'color':'#df6919'}))
                        ],
                        className='d-flex align-items-center mb-2'
                    ),
                    dbc.Row(
                        [
                            dbc.Col(html.P(f'Taxa de abertura: {round(dado["taxa_abertura"], 2)}%'), width=3),
                            dbc.Col(html.P(f'Taxa de clique: {round(dado["taxa_clique"], 2)}%'), width=3),
                            dbc.Col(html.P(f'Data de envio: {pd.to_datetime(dado["data_envio"]).strftime("%d/%m/%y %H:%M")}'), width=4)
                        ],
                        className='text-secondary',
                        style={'fontSize':'0.9rem'}
                    ),
                ]),
                style={
                    'border': '1px solid rgba(255,255,255,0.2)',
                    'borderRadius': '10px',
                    'backgroundColor': '#0d1b2a',
                    'flex': f'1 1 {100/num_cards}%' 
                }
            )
        )

    return dbc.Col(
        rows_ranking,
        className='d-flex flex-column',
        style={
            'gap': '10px',
            'height': '100%',    
            'paddingRight': '8px',
        }
    )
