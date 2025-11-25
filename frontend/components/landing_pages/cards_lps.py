import dash_bootstrap_components as dbc
from dash import html
import pandas as pd


def gerar_indicador_variacao(valor_atual, valor_anterior, sufixo=""):
    if valor_anterior > 0:
        variacao = ((valor_atual - valor_anterior) / valor_anterior) * 100
    else:
        variacao = 0

    if variacao > 0:
        cor = "#5cb85c"
        simbolo = "▲"
    elif variacao < 0:
        cor = "#d9534f" 
        simbolo = "▼"
    else:
        cor = "white"
        simbolo = "="        

    return html.P(
        [
            html.Span(f"{simbolo} {variacao:.1f}% ", style={'color': cor, 'fontWeight': 'bold'}),
            html.Span(f"vs período anterior{sufixo}", style={'color': 'gray', 'fontSize': '0.8rem'})
        ],
        className="mb-0"
    )


def card_visitas(dados_atual, dados_anterior):
    try:
        total_atual = pd.to_numeric(dados_atual['visits_count']).sum()
        
        if isinstance(dados_anterior, pd.DataFrame) and not dados_anterior.empty:
             total_anterior = pd.to_numeric(dados_anterior['visits_count']).sum()
        else:
             total_anterior = 0
             
        elemento_variacao = gerar_indicador_variacao(total_atual, total_anterior)

    except Exception as e:
        print(f"Erro Card Visitas: {e}")
        total_atual = 0
        elemento_variacao = html.P("-")

    return dbc.Card(
        dbc.CardBody([
            html.H6("Volume de Visitas", className="card-title"),
            html.H3(f"{total_atual:,.0f}", className="card-text"), 
            html.P("Total de visitas no período", className="text-secondary"),
            elemento_variacao
        ]),
        style={
            'backgroundColor': '#0d1b2a',
            'color': 'white',
            'border': '2px solid #08B9FF',
            'borderRadius': '10px',
            'textAlign': 'center',
            'padding': '5px',
            'height': '100%'
        }
    )   


def card_leads(dados_atual, dados_anterior):
    try:
        total_atual = pd.to_numeric(dados_atual['conversion_count']).sum()
        
        if isinstance(dados_anterior, pd.DataFrame) and not dados_anterior.empty:
            total_anterior = pd.to_numeric(dados_anterior['conversion_count']).sum()
        else:
            total_anterior = 0
            
        elemento_variacao = gerar_indicador_variacao(total_atual, total_anterior)

    except Exception as e:
        print(f"Erro Card Leads: {e}")
        total_atual = 0
        elemento_variacao = html.P("-")

    return dbc.Card(
        dbc.CardBody([
            html.H6("Total de Leads", className="card-title"),
            html.H3(f"{total_atual:,.0f}", className="card-text"),
            html.P("Total de leads gerados", className="text-secondary", style={'marginBottom': '5px'}), 
            elemento_variacao
        ]),
        style={
            'backgroundColor': '#0d1b2a',
            'color': 'white',
            'border': '2px solid #08B9FF',
            'borderRadius': '10px',
            'textAlign': 'center',
            'padding': '5px',
            'height': '100%'
        }
    )


def card_taxa_conversao(dados_atual, dados_anterior):
    try:

        vis_at = pd.to_numeric(dados_atual['visits_count']).sum()
        conv_at = pd.to_numeric(dados_atual['conversion_count']).sum()
        taxa_at = (conv_at / vis_at * 100) if vis_at > 0 else 0
        

        if isinstance(dados_anterior, pd.DataFrame) and not dados_anterior.empty:
            vis_ant = pd.to_numeric(dados_anterior['visits_count']).sum()
            conv_ant = pd.to_numeric(dados_anterior['conversion_count']).sum()
            taxa_ant = (conv_ant / vis_ant * 100) if vis_ant > 0 else 0
        else:
            taxa_ant = 0

        elemento_variacao = gerar_indicador_variacao(taxa_at, taxa_ant)
        
    except Exception as e:
        print(f"Erro Card Taxa: {e}")
        taxa_at = 0
        elemento_variacao = html.P("-")

    return dbc.Card(
        dbc.CardBody([
            html.H6("Taxa de Conversão Média", className="card-title"),
            html.H3(f"{taxa_at:.2f}%", className="card-text"), 
            html.P("Média (Leads / Visitas)", className="text-secondary", style={'marginBottom': '5px'}),
            elemento_variacao
        ]),
        style={
            'backgroundColor': '#0d1b2a',
            'color': 'white',
            'border': '2px solid #08B9FF',
            'borderRadius': '10px',
            'textAlign': 'center',
            'padding': '5px',
            'height': '100%'
        }
    )


def card_conversao_comercial(dados_lp: pd.DataFrame, dados_vendas: pd.DataFrame):
    try:
        total_leads = pd.to_numeric(dados_lp['conversion_count']).sum()
        total_vendas = 0
        
        if 'status' in dados_vendas.columns:
            total_vendas = len(dados_vendas[dados_vendas['status'] =='won'])
        
        if total_leads > 0:
            taxa_comercial = (total_vendas / total_leads) * 100
        else:
            taxa_comercial = 0
            
    except Exception as e:
        print(f"Erro Card Comercial: {e}")
        taxa_comercial = 0
        total_vendas = 0 

    return dbc.Card(
            dbc.CardBody([
                html.H6("Conversão Comercial", className="card-title"),
                html.H3(f"{taxa_comercial:.2f}%", className="card-text"), 
                html.P(f"Total de {total_vendas} vendas", className="text-secondary")
            ]),
            style={
                'backgroundColor': '#0d1b2a',
                'color': 'white',
                'border': '2px solid #08B9FF',
                'borderRadius': '10px',
                'textAlign': 'center',
                'padding': '5px',
                'height': '100%'
            }
        )

def container_cards_lps(dados_lp_atual: pd.DataFrame, dados_lp_anterior: pd.DataFrame, dados_vendas: pd.DataFrame):
    
    if dados_lp_atual.empty:
        return None 

    return dbc.Row(
        [
            dbc.Col(card_visitas(dados_lp_atual, dados_lp_anterior), md=3),
            dbc.Col(card_leads(dados_lp_atual, dados_lp_anterior), md=3),
            dbc.Col(card_taxa_conversao(dados_lp_atual, dados_lp_anterior), md=3),
            dbc.Col(card_conversao_comercial(dados_lp_atual, dados_vendas), md=3),
        ],
        className="g-3 d-flex align-items-stretch",
    )