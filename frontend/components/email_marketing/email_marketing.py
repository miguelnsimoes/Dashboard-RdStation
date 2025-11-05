from dash import Input, Output, html, dcc, callback
import dash_bootstrap_components as dbc
import pandas as pd
from .ranking_emails import ranking
from .cards import container_cards
from .grafico_horas import grafico_horario_envio


def container_email_marketing(dados: pd.DataFrame):
    """
    Container principal da aba de E-mail Marketing.
    Exibe os cards de métricas, o gráfico de engajamento e o ranking.
    """
    return dbc.Container(
        [
            html.Div(
                id="dashboard-conteudo",
                children=[gerar_conteudo(dados)],
                className="p-3",
            ),
        ],
        fluid=True,
        style={
            "color": "white",
            "minHeight": "100vh",
            "overflowX": "hidden",
            "padding": "1.5rem",
        },
    )


def gerar_conteudo(dados: pd.DataFrame):
    """
    Gera o layout principal do dashboard de E-mail Marketing.
    Contém os cards de métricas, gráfico e tabela de ranking.
    """
    return dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Row(
                        container_cards(dados),
                        className="mb-4",
                        style={"margin": "0"},
                    ),

                    dbc.Row(
                        dbc.Card(
                            [
                                dbc.CardHeader(
                                    "📈 Horário de Melhor Engajamento",
                                    className="fw-bold",
                                    style={
                                        "color": "white",
                                        "border": "none",
                                        "fontSize": "1rem",
                                    },
                                ),
                                dbc.CardBody(
                                    dcc.Graph(
                                        figure=grafico_horario_envio(dados),
                                        config={"displayModeBar": False},
                                        style={
                                            "height": "38vh",
                                            "width": "100%",
                                        },
                                    ),
                                    style={"padding": "1rem"},
                                ),
                            ],
                            style={
                                "border": "none",
                                "borderRadius": "12px",
                                "background-color": "transparent"
                            },
                        ),
                        className="mb-4",
                    ),
                ],
                xs=12,  
                md=12,
                lg=6, 
                className="d-flex flex-column",
            ),
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(
                            "🏆 Ranking de Campanhas",
                            className="fw-bold",
                            style={
                                "color": "white",
                                "border": "none",
                                "fontSize": "1rem",
                            },
                        ),
                        dbc.CardBody(
                            ranking(dados),
                            style={
                                "maxHeight": "70vh",
                                "overflowY": "auto",
                                "padding": "0.5rem",
                            },
                        ),
                    ],
                    style={
                        "border": "none",
                        "borderRadius": "12px",
                        "boxShadow": "0 4px 16px rgba(0,0,0,0.4)",
                        "height": "100%",
                        "background-color": "transparent",

                    },
                ),
                xs=12,
                md=12,
                lg=6,
                className="mt-3 mt-lg-0",
                style={
                    "background-color": "transparent",
                    'height': '40%'
                }
            ),
        ],
        className="g-3 align-items-stretch",
        style={"margin": "0"},
    )
