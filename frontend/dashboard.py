import streamlit as st
import requests
import pandas as pd

def sidebar():
    st.sidebar.title('Cliente')
    cliente = st.sidebar.selectbox('Vizualizar qual cliente?', ('Hospitalar'))
    
    email_marketing = st.sidebar.checkbox("E-mail Marketing")

    start_date = None
    end_date = None
    if email_marketing:
        start_date = st.sidebar.date_input('Digite um início: ')
        end_date = st.sidebar.date_input('Digite um final: ')

    return {
        'cliente' : cliente,
        'email_marketing' : email_marketing,
        'start_date' : start_date,
        'end_date' : end_date
    }

def bloco_email_marketing(start_date, end_date):
    st.markdown('### E-mail Marketing')
        
    url = "http://127.0.0.1:8000/newsletter/"
    queryparams = {
        "start_date" : start_date,
        "end_date" : end_date
    }

    response = requests.get(url, queryparams)

    if response.status_code != 200:
        st.warning("Erro ao pegar os dados!!")
    else:
        response = response.json()['emails']
        df = pd.DataFrame(response)

        df = df[[
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

        

    

def main():
    st.set_page_config(layout='wide')

    cliente_escolhido = sidebar()
    st.title(f'Dashboard - {cliente_escolhido['cliente']}')
    if cliente_escolhido['email_marketing']:
        bloco_email_marketing(cliente_escolhido['start_date'], cliente_escolhido['end_date'])


main()