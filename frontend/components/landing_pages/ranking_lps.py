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
                dbc.Col(html.H2(f'{i + 1}º', className='fw-bold text-white'), width=1),
                dbc.Col(html.H6(f'{lp["asset_identifier"]}', className='text-wrap text-white fw-semibold'), width=8),
                dbc.Col(html.H4(f'{round(lp["conversion_rate"], 2)}%', style={'color':'#df6919'}), width=3),
            ],
            class_name='d-flex align-items-center',
            style={'marginBottom': '0.5rem'}
        )

    
        accordion_content = dbc.AccordionItem(
            [
                dbc.Row(
                    [
                        dbc.Col(html.P(f'Visitas: {lp["visits_count"]}', className='text-light'), width=4),
                        dbc.Col(html.P(f'Leads: {lp["conversion_count"]}', className='text-light'), width=4),  
                    ],
                    style = {'fontSize':'0.9rem'}
                )
            ],
            title = "Ver detalhers",
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
                'backgroundColor':  '#0d1b2a',
                'padding': '8px'
            },
        )

        linhas_ranking.append(card)
    

    return dbc.Col(
        [
            dbc.CardHeader("Ranking de LPs por Conversão", 
                           className="fw-bold", 
                           style={
                               'color': 'white', 
                               'border': 'none', 
                               'fontSize': '1.2rem', 
                               'paddingLeft': '0'
                           }
            ),
            html.Div(
                linhas_ranking, 
                style={
                    'maxHeight': '70vh', 
                    'overflowY': 'auto', 
                    'padding': '0.5rem'
                }
            )
        ],
        className='d-flex flex-column',
        style={'gap': '10px', 'height': '100%'}
    )