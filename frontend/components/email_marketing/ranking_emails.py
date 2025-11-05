from dash import html
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
    dados_extraidos = extraindo_dados(dados)
    num_cards = len(dados_extraidos)

    rows_ranking = []

    for index, (i, dado) in enumerate(dados_extraidos.iterrows()):

        header = dbc.Row(
            [
                dbc.Col(html.H2(f'{index + 1}°', className='fw-bold text-white'), width=1),
                dbc.Col(html.H6(f'{dado["nome_campanha"]}', className='text-wrap text-white fw-semibold'), width=8),
                dbc.Col(html.H4(f'{round(dado["taxa_abertura"], 2)}%', style={'color': '#df6919'}), width=3),
            ],
            className='d-flex align-items-center',
            style={'marginBottom': '0.5rem'}
        )

        accordion_content = dbc.AccordionItem(
            [
                dbc.Row(
                    [
                        dbc.Col(html.P(f'Taxa de abertura: {round(dado["taxa_abertura"], 2)}%', className='text-light'), width=4),
                        dbc.Col(html.P(f'Taxa de clique: {round(dado["taxa_clique"], 2)}%', className='text-light'), width=4),
                        dbc.Col(html.P(f'Data de envio: {pd.to_datetime(dado["data_envio"]).strftime("%d/%m/%y %H:%M")}', className='text-light'), width=4),
                    ],
                    style={'fontSize': '0.9rem'}
                )
            ],
            title="Ver detalhes",
            style={'backgroundColor': '#1b263b', 'color': 'white'}
        )

        card = dbc.Card(
            dbc.CardBody(
                [
                    header,
                    dbc.Accordion(
                        [accordion_content],
                        flush=True,
                        start_collapsed=True,
                        always_open=False,
                    )
                ]
            ),
            style={
                'border': '1px solid rgba(255,255,255,0.2)',
                'borderRadius': '10px',
                'backgroundColor': '#0d1b2a',
                'padding': '8px'
            },
        )

        rows_ranking.append(card)

    return dbc.Col(
        rows_ranking,
        className='d-flex flex-column',
        style={
            'gap': '10px',
            'height': '90%',    
            'paddingRight': '8px',
            'backgroundColor': 'none'
        }
    )
