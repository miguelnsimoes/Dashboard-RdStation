import dash_bootstrap_components as dbc
from dash import Dash, dcc, Input, Output, html
from components.sidebar.sidebar import sidebar
from services.rd_station_services import get_dados
from components.email_marketing.email_marketing import container_email_marketing
import pandas as pd


app = Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])

def dados_rdstation():
    dados = get_dados('2025-09-29', '2025-10-29')
    print("🔎 Retorno do get_dados:", dados)  # <-- debug

    if not isinstance(dados, dict) or 'emails' not in dados:
        print("⚠️ Erro: resposta inválida do backend. Esperado {'emails': [...]}")
        return pd.DataFrame()
    
    df = pd.DataFrame(dados['emails'])

    df = df.rename(columns={
        'send_at': 'data_envio',
        'campaign_id': 'id_campanha',
        'campaign_name': 'nome_campanha',
        'email_dropped_count': 'emails_nao_enviados',
        'email_delivered_count': 'emails_entregues',
        'email_bounced_count': 'emails_rejeitados',
        'email_opened_count': 'emails_abertos',
        'email_clicked_count': 'emails_clicados',
        'email_unsubscribed_count': 'emails_descadastrados',
        'email_spam_reported_count': 'emails_spam_reportados',
        'email_delivered_rate': 'taxa_entrega',
        'email_opened_rate': 'taxa_abertura',
        'email_clicked_rate': 'taxa_clique',
        'email_spam_reported_rate': 'taxa_spam',
        'contacts_count': 'total_contatos'
    })
    
    return df



opcoes = dbc.Tabs([
        dbc.Tab(label='E-mail Marketing', id='email-marketing'),
        dbc.Tab(label='Landing Page', id='lading-page')
    ],
    id='tabs',
    active_tab='email-marketing',
    style={'margin-bottom':'20px'}
)

app.layout = dbc.Container(
    [
        sidebar,
        opcoes,
        container_email_marketing(dados_rdstation())
    ],
    fluid=True,
    style={
        'margin': 0,
        'padding': 0,
        'overflow': 'hidden',
        'width': '100vw',
        'height': '100vh',
        'display': 'flex',
        'flexDirection': 'column'
    }
)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port='8050',
        debug=True)