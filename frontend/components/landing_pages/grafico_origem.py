import plotly.express as px
import pandas as pd
from dash import dcc, html
import dash_bootstrap_components as dbc

def grafico_origem_visual(dados_vendas: pd.DataFrame):

    
    if dados_vendas.empty:
        return dbc.Alert("Sem dados de Vendas/Origem para o período.", color="secondary")
        

    dados_agrupados = dados_vendas.groupby('source_id').size().reset_index(name='Total_Oportunidades')
    
 
    fig = px.bar(
        dados_agrupados, 
        x='source_id',    
        y='Total_Oportunidades', 
        text='Total_Oportunidades',
        color='source_id',   
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
        title_text="ID da Origem", 
        showgrid=False, tickfont=dict(color='white'), linecolor='white'
    )
    fig.update_yaxes(
        title_text="Total de Oportunidades", 
        showgrid=True, gridcolor='rgba(255,255,255,0.2)', tickfont=dict(color='white'), linecolor='white'
    )
    fig.update_traces(textposition='outside', textfont_color='white')

    return dbc.Card(
        dbc.CardBody(
            [
                html.H6("Origem das Oportunidades (ID)", className="card-title", style={'marginBottom': '15px'}),
                dcc.Graph(
                    figure=fig, 
                    config={"displayModeBar": False},
                    style={'height': '100%'}
                )
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