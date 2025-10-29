import requests

def get_dados(start_date=None, end_date=None):
    url = 'http://127.0.0.1:8000/newsletter'
    queryparams = {
        "start_date": start_date,
        "end_date": end_date
    }

    response = requests.get(url, params=queryparams)  
    return response.json()