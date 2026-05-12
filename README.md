# RD Station Insights Dashboard

Uma dashboard analítica para RD Station que integra relatórios de e-mail marketing, desempenho de landing pages e análises de CRM/vendas. O projeto une uma API backend em FastAPI com uma interface frontend em Dash, consumindo dados via endpoints internos que repassam chamadas para as APIs da RD Station.

## Descrição

Dashboard de insights para RD Station que centraliza monitoramento de campanhas de e-mail, conversões de landing pages e negócios CRM. Permite comparar períodos, visualizar métricas de desempenho e consultar contatos enriquecidos via integrações com as APIs da RD Station.

## Principais recursos

- Painel de e-mail marketing com métricas de envio, abertura, cliques e taxas de conversão.
- Relatórios de landing pages para analisar desempenho de conversões ao longo do tempo.
- Integração com CRM para consultar negócios (`deals`) e contatos enriquecidos.
- Backend FastAPI que expõe endpoints próprios e faz proxy seguro para as APIs da RD Station.
- Frontend Dash com navegação por abas e visualização interativa.

## Arquitetura

- `backend/` - API FastAPI para newsletter, landing pages e CRM.
- `frontend/` - Aplicação Dash que consome as APIs internas e renderiza o dashboard.
- `requirements.txt` - dependências Python do projeto.
- `backend/core/config.py` - configuração de ambiente e tokens RD Station.
- `frontend/services/rd_station_services.py` - cliente HTTP para consumir endpoints locais do backend.

## Pré-requisitos

- Python 3.11+ (recomendado)
- RD Station API tokens:
  - `RD_ACCESS_TOKEN`
  - `RD_CRM_TOKEN`
- Rede local/localhost disponível para o backend e frontend se comunicarem.

## Instalação

1. Clone o repositório:

```bash
git clone <REPO_URL>
cd Dashboard-RdStation
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz do projeto com as variáveis de ambiente:

```env
RD_ACCESS_TOKEN=seu_token_rd_station_analytics
RD_CRM_TOKEN=seu_token_rd_station_crm
```

## Como executar

### Backend

Execute o backend FastAPI a partir da raiz do projeto:

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

Abra outro terminal, ative o mesmo ambiente virtual e execute o dashboard Dash:

```bash
cd frontend
python dashboard.py
```

Depois, acesse o dashboard em:

```text
http://127.0.0.1:8051
```

## Endpoints principais

- `GET /newsletter?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD`
- `GET /landing-pages/?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD`
- `GET /crm/deals/?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD`
- `GET /crm/contacts?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD`
- `GET /crm/contacts/email/{email}`
- `GET /crm/contacts/enriched/?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD`

## Observações

- O frontend depende do backend local em `http://127.0.0.1:8000`.
- A rota `crm/contacts/enriched/` busca até 20 e-mails para enriquecer detalhes de contato.
- Para testar dados reais, valide a validade dos tokens RD Station.

## Estrutura de pastas

- `backend/`
  - `main.py` - servidor FastAPI principal.
  - `routers/` - endpoints de newsletter, landing pages e CRM.
  - `core/config.py` - carregamento de variáveis de ambiente.
- `frontend/`
  - `dashboard.py` - aplicação Dash e callbacks.
  - `components/` - componentes visuais de e-mail marketing, landing pages e sidebar.
  - `services/` - client HTTP para consumir o backend.

## Contato

Use este repositório como base para ampliar dashboards de RD Station com novos relatórios, filtros e integrações de CRM.
