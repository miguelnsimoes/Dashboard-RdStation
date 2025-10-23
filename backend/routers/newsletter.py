from fastapi import APIRouter
import httpx
from backend.core.config import settings
from backend.models.newsletter_model import Newsletter

router = APIRouter(prefix='/newsletter', tags=["Newsletter"])

@router.get("/")
async def get_newsletter(start_date:str,end_date:str):
    url = f'https://api.rd.services/platform/analytics/emails?start_date={start_date}&end_date={end_date}'
    headers = {
        "Authorization" : f"Bearer {settings.RD_ACCESS_TOKEN}"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

    
    if response.status_code != 200:
        print(f"Erro na requisição: {response.text}")

    return response.json()