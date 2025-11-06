from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class VendaCRM(BaseModel):
    
    id_venda: str = Field(alias="id")
    nome: str = Field(alias="name")
    valor_recorrente: float = Field(alias="recurrence_price")
    valor_unico: float = Field(alias="one_time_price")
    valor_total: float = Field(alias="total_price")
    status: str = Field(alias="status")
    data_fechamento_esperada: Optional[date] = Field(alias="expected_close_date")
    data_fechamento_real: Optional[datetime] = Field(alias="closed_at")
    data_criacao: datetime = Field(alias="created_at")
    data_atualizacao: datetime = Field(alias="updated_at")
    id_pipeline: str = Field(alias="pipeline_id")
    id_etapa: str = Field(alias="stage_id")
    id_vendedor: str = Field(alias="owner_id") 
    id_motivo_perda: Optional[str] = Field(alias="lost_reason_id") 
    id_origem: Optional[str] = Field(alias="source_id") 
    id_campanha: Optional[str] = Field(alias="campaign_id")
    id_organizacao: Optional[str] = Field(alias="organization_id")
    ids_contatos: List[str] = Field(alias="contact_ids")
    campos_personalizados: Dict[str, Any] = Field(alias="custom_fields")

    class Config:
        populate_by_name = True