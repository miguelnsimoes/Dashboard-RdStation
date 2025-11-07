from fastapi import APIRouter
import httpx
from backend.core.config import settings
from typing import List

from backend.models.landing_page_conversion import LandingPageConversion

router = APIRouter(prefix="/landing-pages", tags=["Landing Pages"])

@router.get("/")
async def get_landing_pages_performance(start_date: str, end_date: str):
    
    url = (
        f"https://api.rd.services/platform/analytics/conversions"
        f"?start_date={start_date}&end_date={end_date}&assets_type[]=LandingPage"
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
            "error_description": "O token de acesso expirou ou é inválido. "
                                 "Renove o RD_ACCESS_TOKEN e reinicie o backend."
        }

    if response.status_code != 200:
        print(f"Erro na requisição ({response.status_code}): {response.text}")
        return {"error": "api_error", "details": response.text}

    data_bruta = response.json()

    conversions_brutas = data_bruta.get('conversions', [])

    try:
        conversoes_validadas = [LandingPageConversion.model_validate(item) for item in conversions_brutas]
        
        return conversoes_validadas
    
    except Exception as e:
        print(f"Erro ao validar dados do Pydantic (LandingPage): {e}")
        return {"error": "validation_error", "details": str(e)}