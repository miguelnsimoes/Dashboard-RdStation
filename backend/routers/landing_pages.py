from fastapi import APIRouter
import httpx
from backend.core.config import settings

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
        response = await client.get(url, headers=headers, timeout=30.0)

    if response.status_code != 200:
        print(f"Erro na requisição ({response.status_code}): {response.text}")
        return {"error": "api_error", "details": response.text}

    data_bruta = response.json()
    conversions_brutas = data_bruta.get('conversions', [])

    return conversions_brutas