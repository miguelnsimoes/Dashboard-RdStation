import streamlit as st

def sidebar():
    st.sidebar.title('Cliente')
    cliente = st.sidebar.selectbox('Vizualizar qual cliente?', ('Hospitalar'))
    
    email_marketing = st.sidebar.checkbox("E-mail Marketing")

    return {
        'cliente' : cliente,
        'email_marketing' : email_marketing,
    }

def main():
    st.set_page_config(layout='wide')

    cliente_escolhido = sidebar()
    st.title(f'Dashboard - {cliente_escolhido['cliente']}')


main()