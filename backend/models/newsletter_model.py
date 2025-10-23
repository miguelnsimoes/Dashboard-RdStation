from datetime import datetime
from pydantic import BaseModel, Field

class Newsletter(BaseModel):
    id: int = Field(alias="campaign_id")
    name: str = Field(alias="campaign_name")
    data_envio: datetime = Field(alias="send_at")
    qtd_contatos: int = Field(alias="contacts_count")
    qtd_emails_abertos: int = Field(alias="email_opened_count")
    taxa_emails_abertos: float = Field(alias="email_opened_rate")
    qtd_emails_clicados: int = Field(alias="email_clicked_count")
    taxa_emails_clicados: float = Field(alias="email_clicked_rate")
    qtd_emails_rejeitados: int = Field(alias="email_bounced_count")
    qtd_emails_spam: int = Field(alias="email_spam_reported_count")
    qtd_emails_descartados: int = Field(alias="email_dropped_count")

    class Config:
        populate_by_name = True
