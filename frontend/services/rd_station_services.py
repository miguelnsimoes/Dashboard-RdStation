import requests
import pandas as pd  

def get_dados(start_date=None, end_date=None):
    url = 'http://127.0.0.1:8000/newsletter'
    queryparams = {
        "start_date": start_date,
        "end_date": end_date
    }
    try:
        response = requests.get(url, params=queryparams)
        response.raise_for_status() 
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados de Newsletter: {e}")
        return {} 
    
    

def get_landing_page_data(start_date: str, end_date: str) -> pd.DataFrame:
    url = 'http://127.0.0.1:8000/landing-pages/' 
    queryparams = {
        "start_date": start_date,
        "end_date": end_date
    }

    try:
        response = requests.get(url, params=queryparams, timeout=30.0)
        response.raise_for_status() 
        dados_json = response.json()
        df = pd.DataFrame(dados_json)
        return df

    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar na API de Landing Pages: {e}")
        return pd.DataFrame()
    
    except Exception as e:
        print(f"Erro ao processar dados das Landing Pages: {e}")
        return pd.DataFrame()
    


def get_deals_data(start_date: str, end_date: str) -> pd.DataFrame:
    url = 'http://127.0.0.1:8000/crm/deals/'

    queryparams = {
        "start_date": start_date,
        "end_date": end_date    
    }

    try:
        response = requests.get(url, params=queryparams, timeout=30.0)
        response.raise_for_status()
        dados_json = response.json()
        df = pd.DataFrame(dados_json)
        return df
    except requests.exceptions.RequestException as e:
        print(f"Erro ao processar dados das Landing Pages: {e}")
    
    except Exception as e:
        print(f"Erro ao processar dados das Landing Pages: {e}")
        return pd.DataFrame() 