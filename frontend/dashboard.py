import streamlit as st
import requests
import pandas as pd
from blocks.email_marketing import bloco_principal

def sidebar():
    st.logo('./logo.webp', size='large')
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
 
def main():
    st.set_page_config(layout='wide')

    cliente_escolhido = sidebar()
    st.title(f'Dashboard - {cliente_escolhido['cliente']}')
    if cliente_escolhido['email_marketing']:
        bloco_principal(cliente_escolhido['start_date'], cliente_escolhido['end_date'])


main()