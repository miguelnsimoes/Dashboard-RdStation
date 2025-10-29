import dash_bootstrap_components as dbc
from dash import Dash, dcc, Input, Output, html
import requests
from components.sidebar.sidebar import sidebar
from components.email_marketing.components.email_marketing import container_email_marketing
from services.rd_station_services import get_dados

app = Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])

opcoes = dbc.Tabs([
        dbc.Tab(label='E-mail Marketing', id='email-marketing'),
        dbc.Tab(label='Landing Page', id='lading-page')
    ],
    id='tabs',
    active_tab='email-marketing',
    style={'margin-bottom':'30px'}
)

app.layout = dbc.Container([
   sidebar,
   opcoes,
   container_email_marketing(get_dados('2025-09-29', '2025-10-29'))
],
    fluid=True,
    style={'margin' : 0, 'padding' : 0}
)

if __name__ == '__main__':
    app.run(debug=True)