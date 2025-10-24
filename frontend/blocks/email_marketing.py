import streamlit as st
import  requests
import pandas as pd
from streamlit_extras.metric_cards import style_metric_cards
import datetime

def get_dados(start_date, end_date):
    url = "http://127.0.0.1:8000/newsletter/"
    queryparams = {
        "start_date" : start_date,  
        "end_date" : end_date
    }

    response = requests.get(url, queryparams)

    if response.status_code != 200:
        st.warning("Erro ao pegar os dados!!")
    
    return response.json()['emails']

def bloco_cards(dados: pd.DataFrame):
    col1, col2, col3 = st.columns(3)
    col_card1, col_card2, col_card3, col_card4 = st.columns(4)

    dados_card = dados[['email_opened_rate', 'send_at', 'email_clicked_rate']]

    with st.container():
        mes_atual = datetime.datetime.now().month
        mes_passado = datetime.datetime.now().month - 1
        dados_mes_atual = dados_card[pd.to_datetime(dados_card['send_at']).dt.month == mes_atual]
        dados_mes_passado = dados_card[pd.to_datetime(dados_card['send_at']).dt.month == mes_passado]

        with col1:
            porcent_abertura_atual = round(dados_mes_atual['email_opened_rate'].sum(axis=0) / len(dados_mes_atual),2)
            porcent_abertura_passado = round(dados_mes_passado['email_opened_rate'].sum(axis=0) / len(dados_mes_passado),2)

            col_card1.metric(label='Evolução da taxa de abertura', value=f'{porcent_abertura_atual}%', delta=round(porcent_abertura_atual-porcent_abertura_passado,2), border=True)

        with col2:
            porcent_cliques_atual = round(dados_mes_atual['email_clicked_rate'].sum(axis=0) / len(dados_mes_atual), 2)
            porcent_cliques_passado = round(dados_mes_passado['email_clicked_rate'].sum(axis=0) / len(dados_mes_passado), 2)

            col_card2.metric(label="Evolução da taxa de clique", value=f'{porcent_cliques_atual}%', delta=round(porcent_cliques_atual-porcent_cliques_passado,2), border=True)

        with col3:
            pass


def bloco_tabela(dados):
    st.markdown('### E-mail Marketing')

    df = dados[[
        "campaign_name",
        "send_at",
        "contacts_count",
        "email_opened_rate",
        "email_opened_count",
        "email_clicked_rate",
        "email_clicked_count",
        "email_bounced_count",
        "email_spam_reported_count",
        "email_unsubscribed_count"
    ]]

    df = df.rename(columns={
        "campaign_name": "Assunto do e-mail",
        "send_at": "Data e hora do envio",
        "contacts_count": "Leads selecionados",
        "email_opened_rate": "Taxa de abertura (%)",
        "email_opened_count": "Quantidade de aberturas",
        "email_clicked_rate": "Taxa de cliques (%)",
        "email_clicked_count": "Quantidade de cliques",
        "email_bounced_count": "Bounces (número absoluto)",
        "email_spam_reported_count": "Spam (número absoluto)",
        "email_unsubscribed_count": "Descadastrados (número absoluto)"
    })

    if not df.empty:
        df["Data e hora do envio"] = pd.to_datetime(df["Data e hora do envio"]).dt.strftime("%d/%m/%Y %H:%M")
        df["Taxa de abertura (%)"] = df["Taxa de abertura (%)"].apply(lambda x: round(x, 2))
        df["Taxa de cliques (%)"] = df["Taxa de cliques (%)"].apply(lambda x: round(x, 2))

    st.dataframe(df, use_container_width=True)           
    

def bloco_principal(start_date, end_date):
    dados = pd.DataFrame(get_dados(start_date, end_date))
    bloco_cards(dados)
    bloco_tabela(dados)
  