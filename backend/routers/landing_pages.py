from fastapi import APIRouter
import httpx
from backend.core.config import settings

router = APIRouter(prefix='/landing-pages', tags=['Landing Pages'])

@router.get('/')
async def get_dados():
    pass