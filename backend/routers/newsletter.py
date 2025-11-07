from fastapi import APIRouter
import httpx
from backend.core.config import settings

router = APIRouter(prefix="/newsletter", tags=["Newsletter"])

@router.get("/")
async def get_newsletter(start_date: str, end_date: str):
    url = (
        f"https://api.rd.services/platform/analytics/emails"
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
            "error_description": "O token de acesso expirou ou é inválido. "
                                 "Renove o RD_ACCESS_TOKEN e reinicie o backend."
        }

    if response.status_code != 200:
        print(f"❌ Erro na requisição ({response.status_code}): {response.text}")
        return {"error": "api_error", "details": response.text}

    data = response.json()
    print(f"✅ Dados recebidos da RD Station: {list(data.keys())}")
    return data
