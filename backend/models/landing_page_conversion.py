from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class LandingPageConversion(BaseModel):
    id_asset: int = Field(alias="asset_id")
    nome_identificador: Optional[str] = Field(alias="asset_identifier", default=None)
    tipo_asset: Optional[str] = Field(alias="asset_type", default=None)
    qtd_conversoes: int = Field(alias="conversion_count", default=0)
    qtd_visitas: int = Field(alias="visit_count", default=0)
    taxa_conversao: float = Field(alias="conversion_rate", default=0.0)
    data_criacao: Optional[datetime] = Field(alias="asset_created_at", default=None)
    data_atualizacao: Optional[datetime] = Field(alias="asset_updated_at", default=None)

    class Config:
        populate_by_name = True