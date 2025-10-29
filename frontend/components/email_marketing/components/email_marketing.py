import dash_bootstrap_components as dbc
from dash import Dash, dcc, Input, Output, html
from .cards.cards_email_marketing import cards
from .tabela_emails_marketing.tabelas_emails_marketing import tabela

def container_email_marketing(dados):
    return dbc.Container(
    [  
        dbc.Col(
            cards(dados), width=20
        ),
        dbc.Col(
            [   
                dbc.Row(
                    [
                        html.H2('Tabela Resultados Gerais'),
                        tabela(dados),
                        html.H6(str(dados))

                    ],
                ), 
            ],
            className='d-flex align-items-start'
        ),
    ],
    className='d-flex justify-content-center', style={'gap':'60px', 'margin':'30px', 'justify-content':'center', 'align-items':'center'}
)