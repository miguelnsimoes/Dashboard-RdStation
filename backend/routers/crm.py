from fastapi import APIRouter
import httpx
from backend.core.config import settings
from typing import List

from backend.models.vendas import VendaCRM


router = APIRouter(prefix="/crm", tags=["CRM"])

# rota que o dashboard vai usar para pegar todas as vendas
@router.get("/vendas/")
async def get_vendas_por_periodo(start_date: str, end_date: str):
    
    url = (
        f"https://api.rd.services/crm/v2/deals"
        f"?start_date={start_date}&end_date={end_date}"
    )

    token = settings.RD_ACCESS_TOKEN.strip() 
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

    if response.status_code == 401:
        return {
            "error": "invalid_token",
            "error_description": "O token de acesso expirou ou é inválido."
        }

    if response.status_code != 200:
        print(f"Erro na requisição ({response.status_code}): {response.text}")
        return {"error": "api_error", "details": response.text}

    data_bruta = response.json()

    vendas_brutas = data_bruta.get('deals', []) 

    try:
        vendas_validadas = [VendaCRM.model_validate(item) for item in vendas_brutas]  
        return vendas_validadas 
    
    except Exception as e:
        print(f"Erro ao validar lista de vendas do Pydantic: {e}")
        return {"error": "validation_error", "details": str(e)}



@router.get("/vendas/{venda_id}")
async def get_venda_por_id(venda_id: str):
    
    url = f"https://api.rd.services/crm/v2/deals/{venda_id}"

    token = settings.RD_ACCESS_TOKEN.strip()

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

    if response.status_code == 401:
        return {
            "error": "invalid_token",
            "error_description": "O token de acesso expirou ou é inválido."
        }
    
    if response.status_code == 404:
        return {"error": "not_found", "details": f"Venda com ID {venda_id} não encontrada."}

    if response.status_code != 200:
        print(f"Erro na requisição ({response.status_code}): {response.text}")
        return {"error": "api_error", "details": response.text}

    data_bruta = response.json()
    
   
    try:
        # usa o molde VendaCRM para traduzir a resposta
        venda_validada = VendaCRM.model_validate(data_bruta['data'])
        return venda_validada
    
    except Exception as e:
        print(f"Erro ao validar dados do Pydantic: {e}")
        return {"error": "validation_error", "details": str(e)}