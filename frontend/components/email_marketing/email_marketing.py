from dash import Input, Output, State, html, dcc, callback
import dash_bootstrap_components as dbc
import pandas as pd
from datetime import date
from services.rd_station_services import get_dados
from .ranking_emails import ranking
from .cards import container_cards
from .grafico_horas import grafico_horario_envio


# ==============================
# CONTAINER PRINCIPAL
# ==============================
def container_email_marketing(dados: pd.DataFrame):
    return dbc.Container(
        [
            # ------------------------------
            # BOTÃO + MODAL DE PERÍODO
            # ------------------------------
            dbc.Row(
                dbc.Col(
                    [
                        dbc.Button(
                            "Selecionar Período",
                            id="open-date-modal",
                            color="primary",
                            style={"backgroundColor": "#df6919", "border": "none"},
                        ),
                        dbc.Modal(
                            [
                                dbc.ModalHeader(
                                    dbc.ModalTitle("Selecionar Período de Análise")
                                ),
                                dbc.ModalBody(
                                    [
                                        dcc.DatePickerRange(
                                            id="date-picker-range",
                                            min_date_allowed=date(2020, 1, 1),
                                            max_date_allowed=date.today(),
                                            initial_visible_month=date.today(),
                                            end_date=date.today(),
                                            display_format="DD/MM/YYYY",
                                        ),
                                        html.Div(
                                            id="output-date-picker",
                                            className="mt-3 fw-bold text-white",
                                        ),
                                    ]
                                ),
                                dbc.ModalFooter(
                                    dbc.Button(
                                        "Fechar", id="close-date-modal", color="secondary"
                                    )
                                ),
                            ],
                            id="modal-date",
                            is_open=False,
                            centered=True,
                            backdrop="static",
                        ),
                    ],
                    width=12,
                    style={"textAlign": "right"},
                ),
                className="mb-4",
            ),

            # ------------------------------
            # CONTEÚDO PRINCIPAL DO DASHBOARD
            # ------------------------------
            html.Div(
                id="dashboard-conteudo",
                children=[gerar_conteudo(dados)],
            ),
        ],
        fluid=True,
        style={
            "padding": "2rem",
            "borderRadius": "10px",
            "boxShadow": "0 4px 12px rgba(0,0,0,0.3)",
            "color": "white",
            "minHeight": "100vh",  # Garante que o container ocupe toda a tela
        },
        className="overflow-auto",  # Ativa scroll se o conteúdo ultrapassar a tela
    )



def gerar_conteudo(dados: pd.DataFrame):
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
                                    className="text-white fw-bold",
                                ),
                                dbc.CardBody(
                                    dcc.Graph(
                                        figure=grafico_horario_envio(dados),
                                        config={"displayModeBar": False},
                                        style={
                                            "height": "35vh",  # reduzido para caber melhor em telas pequenas
                                            "width": "100%",
                                        },
                                    )
                                ),
                            ],
                            style={
                                "backgroundColor": "#0E1117",
                                "color": "white",
                                "border": "none",
                                "borderRadius": "10px",
                                "boxShadow": "0 4px 12px rgba(0,0,0,0.3)",
                            },
                        ),
                        className="mb-4",
                    ),
                ],
                xs=12,
                md=12,
                lg=6,  # Em telas grandes divide, em pequenas empilha
                className="mb-3",
            ),

            # ------------------------------
            # COLUNA 2: RANKING
            # ------------------------------
            dbc.Col(
                ranking(dados),
                xs=12,
                md=12,
                lg=6,
                style={
                    "maxHeight": "85vh",
                    "overflowY": "auto",  # scroll individual
                    "paddingRight": "5px",
                },
                className="mb-3",
            ),
        ],
        className="g-2 flex-wrap",  # Permite quebra de linha em telas pequenas
        style={"margin": "0"},
    )


# ==============================
# CALLBACK DO MODAL
# ==============================
@callback(
    Output("modal-date", "is_open"),
    [Input("open-date-modal", "n_clicks"), Input("close-date-modal", "n_clicks")],
    [State("modal-date", "is_open")],
)
def toggle_modal(open_click, close_click, is_open):
    if open_click or close_click:
        return not is_open
    return is_open


# ==============================
# CALLBACK DE ATUALIZAÇÃO DOS DADOS
# ==============================
@callback(
    Output("dashboard-conteudo", "children"),
    Input("date-picker-range", "start_date"),
    Input("date-picker-range", "end_date"),
)
def atualizar_dados(start_date, end_date):
    if not start_date or not end_date:
        return html.P("Selecione um intervalo de datas.", className="text-warning")

    dados = get_dados(start_date, end_date)

    if "emails" not in dados:
        return html.P("Erro ao carregar dados. Verifique a conexão com o backend.")

    df = pd.DataFrame(dados["emails"])

    df = df.rename(
        columns={
            "send_at": "data_envio",
            "campaign_id": "id_campanha",
            "campaign_name": "nome_campanha",
            "email_dropped_count": "emails_nao_enviados",
            "email_delivered_count": "emails_entregues",
            "email_bounced_count": "emails_rejeitados",
            "email_opened_count": "emails_abertos",
            "email_clicked_count": "emails_clicados",
            "email_unsubscribed_count": "emails_descadastrados",
            "email_spam_reported_count": "emails_spam_reportados",
            "email_delivered_rate": "taxa_entrega",
            "email_opened_rate": "taxa_abertura",
            "email_clicked_rate": "taxa_clique",
            "email_spam_reported_rate": "taxa_spam",
            "contacts_count": "total_contatos",
        }
    )

    return gerar_conteudo(df)
