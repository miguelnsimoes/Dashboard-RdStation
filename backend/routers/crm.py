from fastapi import APIRouter
import httpx
from backend.core.config import settings

router = APIRouter(prefix="/crm", tags=["CRM"])
#vendas por periodo
@router.get("/deals/")
async def get_deals_por_periodo(start_date: str, end_date: str):
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
        response = await client.get(url, headers=headers, timeout=30.0)

    if response.status_code == 401:
        return {"error": "invalid_token", "details": "Token inválido."}

    if response.status_code != 200:
        print(f"Erro na API de CRM ({response.status_code}): {response.text}")
        return {"error": "api_error", "details": response.text}

    data_bruta = response.json()
    deals_brutos = data_bruta.get('deals', []) 
    return deals_brutos

#venda especifica
@router.get("/vendas/{venda_id}")
async def get_venda_por_id(venda_id: str):
    [cite_start], url = f"https://api.rd.services/crm/v2/deals/{venda_id}"
    token = settings.RD_ACCESS_TOKEN.strip()
    headers = { "Authorization": f"Bearer {token}", "Content-Type": "application/json" }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, timeout=30.0)

    if response.status_code != 200:
        return {"error": "api_error", "details": "Venda não encontrada ou erro."}
        
    data_bruta = response.json()
    return data_bruta.get("data", {})