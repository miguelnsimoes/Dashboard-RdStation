from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc

sidebar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
            [
                dbc.Col(html.Img(src='../../assets/logo.webp', height='30px'), style={'background': 'white', 'border-radius' : '10px', 'padding': '5px'}),
                dbc.Col(dbc.NavbarBrand('Dashboard', style={'color':'white'})),
            ],
            className='d-flex justify-content-center align-items-center'
        ),
            dbc.DropdownMenu(
                [
                    dbc.DropdownMenuItem('Hospitalar', id='id-hospitalar')
                ],
                label='Clientes',
                in_navbar=True,
                nav=True,
                style={'color':'white'}
            ),
        ],
    ),
    style={'padding':'40px', 'height': '60px'},
    color='secondary',
    dark=True,
)