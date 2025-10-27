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
            melhor_email_taxa_abertura = dados_card.loc[dados_card['email_opened_rate'].idxmax()]
            melhor_email_taxa_cliques = dados_card.loc[dados_card['email_clicked_rate'].idxmax()]

            horario_taxa_abertura =  pd.to_datetime(melhor_email_taxa_abertura['send_at']).strftime('%H:%M')
            horario_taxa_clique  = pd.to_datetime(melhor_email_taxa_cliques['send_at']).strftime('%H:%M')

            col_card3.metric(label=f'Horário de melhor engajamento', value=f'{horario_taxa_abertura} - {horario_taxa_clique}' if horario_taxa_abertura != horario_taxa_clique else f'{horario_taxa_abertura}', border=True, help='Horário Taxa de Abertura - Horário Taxa de Clique',height="stretch")    


def bloco_picos_horario(dados):
    dados['send_at'] = pd.to_datetime(dados['send_at'])

    dados['hora_envio'] = dados['send_at'].dt.strftime('%H:%M')

    picos = (
        dados.groupby('hora_envio')
        .size()
        .reset_index(name='quantidade')
        .sort_values('hora_envio')
    )

    st.markdown("### ⏰ Picos de horário de envio")
    st.line_chart(picos, x='hora_envio', y='quantidade')




def bloco_melhor_email(dados):
    dados['media_ponderada'] = (dados['email_opened_rate'] * 0.4) + (dados['email_clicked_rate'] * 0.6)
    melhor_email = (dados.loc[dados['media_ponderada'].idxmax()]) 

    melhor_email_df = pd.DataFrame({
        "Assunto do e-mail": [melhor_email['campaign_name']],
        "Data e hora do envio": [melhor_email['send_at']],
        "Taxa de abertura (%)": [melhor_email['email_opened_rate']],
        "Taxa de clique (%)": [melhor_email['email_clicked_rate']],
        "Quantidade total de cliques": [melhor_email['email_clicked_count']]
    })

    melhor_email_df["Data e hora do envio"] = pd.to_datetime(melhor_email_df["Data e hora do envio"]).dt.strftime('%d/%m/%Y %H:%M')

    st.markdown("### 📊 E-mail com melhor desempenho")
    st.dataframe(melhor_email_df)

def bloco_tabela(dados):
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

    st.markdown('### E-mail Marketing')
    bloco_cards(dados)
    bloco_picos_horario(dados)
    bloco_melhor_email(dados)
    bloco_tabela(dados)
  