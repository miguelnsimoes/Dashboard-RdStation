from dash import html, dcc, Output, Input, State, callback
import dash_bootstrap_components as dbc
from datetime import date

sidebar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(html.Img(src='../../assets/logo.webp', height='30px')),
                    dbc.Col(dbc.NavbarBrand('Dashboard', style={'color':'#004381'})),
                ],
                className='d-flex justify-content-center align-items-center'
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.DropdownMenu(
                            [
                                dbc.DropdownMenuItem('Hospitalar', id='id-hospitalar')
                            ],
                            label='Clientes',
                            in_navbar=True,
                            nav=True,
                            style={'color': '#004381'}
                        ),
                    ),
                    dbc.Col(
                        [
                            dbc.Button("Filtros", id="open-filter", n_clicks=0, style={'width': '100px'}),
                            dbc.Modal(
                                [
                                    dbc.ModalHeader(dbc.ModalTitle("Filtros")),
                                    dbc.ModalBody(id="modal-filter-body"),
                                    dbc.ModalFooter(
                                        dbc.Button("Fechar", id="close-filter", className="ms-auto", n_clicks=0)
                                    ),
                                ],
                                id="modal-filter",
                                is_open=False,
                                centered=True,
                                backdrop="static"
                            ),
                        ]
                    ),
                ],
                className='d-flex flex-row justify-content-center align-items-center',
                style={'gap': '80px'}
            )
        ]
    ),
    style={'padding': '40px', 'height': '60px'},
    color='white',
    dark=True,
)


@callback(
    Output("modal-filter", "is_open"),
    [Input("open-filter", "n_clicks"), Input("close-filter", "n_clicks")],
    [State("modal-filter", "is_open")],
)
def toggle_modal(open_click, close_click, is_open):
    if open_click or close_click:
        return not is_open
    return is_open


@callback(
    Output("modal-filter-body", "children"),
    Input("tabs", "active_tab")
)
def atualizar_modal_conteudo(tab_ativa):
    if tab_ativa == "email-marketing":
        return html.Div([
            html.P("Selecione o período de análise:", className="fw-bold mb-2"),
            dcc.DatePickerRange(
                id="date-picker-range-email",
                min_date_allowed=date(2020, 1, 1),
                max_date_allowed=date.today(),
                initial_visible_month=date.today(),
                end_date=date.today(),
                display_format="DD/MM/YYYY",
                className="mb-3"
            ),
            html.Div(id="output-date-picker", className="mt-3 fw-bold text-secondary")
        ])

    elif tab_ativa == "lading-page":
        return html.Div([
            html.P("Selecione o período de análise:", className="fw-bold mb-2"),
            dcc.DatePickerRange(
                id="date-picker-range-lp",
                min_date_allowed=date(2020, 1, 1),
                max_date_allowed=date.today(),
                initial_visible_month=date.today(),
                end_date = date.today(),
                display_format="DD/MM/YY",
                className="mb-3"
            ),
            html.P("Filtro de LP Específica:", className="fw-bold mb-2 mt-3"),
            dbc.Input(placeholder="Buscar por nome...", type="text"),
        ])

    return html.P("Selecione uma aba para visualizar os filtros.")
