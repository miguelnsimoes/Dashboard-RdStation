import dash_bootstrap_components as dbc
from dash import Dash, html, Input, Output
import pandas as pd
from components.sidebar.sidebar import sidebar
from datetime import date, timedelta

from services.rd_station_services import get_dados
from components.email_marketing.email_marketing import container_email_marketing
from services.rd_station_services import get_landing_page_data
from components.landing_pages.landing_page import container_landing_pages
from services.rd_station_services import get_deals_data


app = Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO], suppress_callback_exceptions=True)

def get_comparison_dates():
    end_date_atual = date.today()
    start_date_atual = end_date_atual - timedelta(days=90)
    end_date_anterior = start_date_atual - timedelta(days=1)
    start_date_anterior = end_date_anterior - timedelta(days=90)

    return (
        start_date_atual.isoformat(), 
        end_date_atual.isoformat(), 
        start_date_anterior.isoformat(), 
        end_date_anterior.isoformat()
    )

def get_datas_filtro():
    end_date = date.today()
    start_date = end_date - timedelta(days = 90)
    return start_date.isoformat(), end_date.isoformat()


def dados_rdstation():
    dados = get_dados('2025-09-29', '2025-10-29')

    if not isinstance(dados, dict):
        print("⚠️ Resposta inesperada:", dados)
        return pd.DataFrame()

    if 'emails' not in dados:
        print("⚠️ Chave 'emails' não encontrada:", dados)
        return pd.DataFrame()

    df = pd.DataFrame(dados['emails'])

    rename_map = {
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
    }

    df = df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns})

    if 'data_envio' not in df.columns:
        print("⚠️ Coluna 'data_envio' ausente. Colunas disponíveis:", df.columns.tolist())
        return pd.DataFrame()

    df['data_envio'] = pd.to_datetime(df['data_envio'], errors='coerce')
    return df

def dados_landing_pages():
    start_date, end_date = get_datas_filtro()
    df = get_landing_page_data(start_date, end_date)
    return df


def dados_vendas():
    start_date, end_date = get_datas_filtro()
    df = get_deals_data(start_date, end_date)
    return df


tabs = dbc.Tabs(
    [
        dbc.Tab(label='E-mail Marketing', tab_id='email-marketing'),
        dbc.Tab(label='Landing Page', tab_id='lading-page'),
    ],
    id='tabs',
    active_tab='email-marketing',
    style={'margin-bottom': '20px'}
)


app.layout = dbc.Container(
    [
        sidebar,
        tabs,
        html.Div(id='conteudo-dashboard')
    ],
    fluid=True,
    style={
        'margin': 0,
        'padding': 0,
        'overflowX': 'hidden',
        'width': '100vw',
        'height': '100vh',
        'display': 'flex',
        'flexDirection': 'column',
        'background-color':'#091023'
    }
)


@app.callback(
    Output('conteudo-dashboard', 'children'),
    Input('tabs', 'active_tab')
)


def switch_tab(at):
    if at == 'email-marketing':
        df_email = dados_rdstation()
        if df_email.empty:
            return dbc.Alert(
                "Nenhum dado disponível no momento. Verifique a conexão com o RD Station ou o token de acesso.",
                color="warning",
                className="m-3",
            )
        return container_email_marketing(df_email)
    
    elif at == 'lading-page':
        df_lp = dados_landing_pages()
        df_vendas = dados_vendas()
        return container_landing_pages(df_lp, df_vendas)

    else:
        return dbc.Alert("Pagina nao encontrada", color="danger", className="m-3")

   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8051, debug=True)