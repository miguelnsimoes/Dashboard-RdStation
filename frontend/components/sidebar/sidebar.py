from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc

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
                dbc.DropdownMenu(
                    [
                        dbc.DropdownMenuItem('Hospitalar', id='id-hospitalar')
                    ],
                    label='Clientes',
                    in_navbar=True,
                    nav=True,
                    style={'color':'#004381'}
                ),
            )
            
        ],
    ),
    style={'padding':'40px', 'height': '60px'},
    color='white',
    dark=True,
)