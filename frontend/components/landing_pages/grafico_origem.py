import plotly.express as px
import pandas as pd
from dash import dcc, html
import dash_bootstrap_components as dbc

def grafico_origem_visual(dados_enriquecidos: pd.DataFrame):
    if dados_enriquecidos.empty or 'origin' not in dados_enriquecidos:
        return dbc.Alert("Dados de origem vazios/nao encontrados", color= "secondary")

    df_agrupado = dados_enriquecidos.groupby('origin').size().reset_index(name='Total_Oportunidades')

    fig = px.bar(
        df_agrupado, 
        x='origin',      
        y='Total_Oportunidades',
        text='Total_Oportunidades',
        color='origin',   
        color_discrete_sequence=px.colors.qualitative.Pastel
    )

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color="white",
        showlegend=False,
        margin=dict(t=20, b=20, l=20, r=20)
    )
    
    fig.update_xaxes(
        title_text="Canais de Origem", 
        showgrid=False, tickfont=dict(color='white'), linecolor='white'
    )
    fig.update_yaxes(
        title_text="Total de Oportunidades", 
        showgrid=True, gridcolor='rgba(255,255,255,0.2)', tickfont=dict(color='white'), linecolor='white'
    )
    fig.update_traces(textposition='outside', textfont_color='white')

 
    return dbc.Card(
        dbc.CardBody([
            html.H6("Origem das Oportunidades (Canais)", className="card-title", style={'marginBottom': '15px'}),
            dcc.Graph(figure=fig, config={"displayModeBar": False}, style={'height': '100%'})
        ],
        style={'height': '100%', 'display': 'flex', 'flexDirection': 'column'}
        ),
        style={
            'backgroundColor': '#0d1b2a', 
            'color': 'white', 
            'border': '1px solid rgba(255,255,255,0.2)',
            'borderRadius': '10px',
            'height': '100%'
        }
    )