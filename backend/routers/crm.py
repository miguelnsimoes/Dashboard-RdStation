from fastapi import APIRouter
import httpx
from backend.core.config import settings
import requests 
router = APIRouter(prefix="/crm", tags=["CRM"])



@router.get("/deals/")
async def get_deals_por_periodo(start_date: str, end_date: str):
    url = (
        f"https://api.rd.services/crm/v2/deals"
        f"?start_date={start_date}&end_date={end_date}"
    )

    token = settings.RD_CRM_TOKEN.strip()

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, timeout=30.0)

    if response.status_code == 401:
        return {"error": "invalid_token", "details": "Token inválido."} 

    if response.status_code != 200:
        print(f"Erro na API de CRM ({response.status_code}): {response.text}")
        return {"error": "api_error", "details": response.text}

    data_bruta = response.json()

    if isinstance(data_bruta, list) and len(data_bruta) > 0:
        data_bruta = data_bruta[0] 

    deals_brutos = data_bruta.get('data', [])
        
    return deals_brutos



@router.get("/contacts")
async def get_todos_contatos_email(start_date: str, end_date: str):
    base_url = "https://api.rd.services/platform/contacts"

    token = settings.RD_CRM_TOKEN.strip()
    headers = { "Authorization": f"Bearer {token}", "Content-Type": "application/json" }

    todos_emails = []
    page_number = 1

    async with httpx.AsyncClient() as client:
        while True:
            query_params = {
                "start_date": start_date,
                "end_date": end_date,
                "page[number]": page_number,
                "page[size]": 100
            }

            response = await client.get(base_url, params=query_params, headers=headers, timeout=30.0)

            if response.status_code != 200:
                print(f"erro na paginacao dos dados ({response.status_code}) : {response.text}")
                break

            data_bruta = response.json()

            contatos = data_bruta.get('data', [])

            if not contatos:
                break

            for contato in contatos:
                emails_do_contato = contato.get('emails', [])
                if emails_do_contato and emails_do_contato[0].get('email'):
                    todos_emails.append(emails_do_contato[0]['email'])

            links = data_bruta.get('links', {})
            if 'next' not in links:
                break

            page_number += 1
            
    return todos_emails  



@router.get("/contacts/email/{email}")
async def get_detalhes_contatos(email: str):
    url = f"https://api.rd.services/platform/contacts/email:{email}"
    
    token = settings.RD_CRM_TOKEN.strip()
    headers = { "Authorization": f"Bearer {token}", "Content-Type": "application/json" }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, timeout=30.0)

    if response.status_code == 404:
        return {"error": "contact_not_found", "details": f"Contato com email {email} não encontrado."}
    
    if response.status_code != 200:
        print(f"Erro na API de Contatos ({response.status_code}): {response.text}")
        return {"error": "api_error", "details": response.text}

    return response.json()



@router.get("/contacts/enriched/")
async def get_enriched_contacts(start_date: str, end_date: str):
    emails_list_url = f"http://127.0.0.1:8000/crm/contacts?start_date={start_date}&end_date={end_date}"
    
    try:
        response_emails = requests.get(emails_list_url, timeout=60) 
        emails = response_emails.json()
    except Exception as e:
        print(f"ERRO: Falha ao buscar lista de emails (Paginação): {e}")
        return {"error": "failed_pagination"}


    if isinstance(emails, dict) and 'error' in emails:
        return emails
        
    if not emails:
        return [] 
    
    contatos_enriquecidos = []

    for email in emails[:20]: 
        contact_url = f"http://127.0.0.1:8000/crm/contacts/email/{email}"
        
        try:
            response_contact = requests.get(contact_url, timeout=10) 
            
            if response_contact.status_code == 200:
                contatos_enriquecidos.append(response_contact.json())
        except Exception as e:
            print(f"Aviso: Contato {email} falhou na busca de detalhe: {e}")
            continue

    return contatos_enriquecidos