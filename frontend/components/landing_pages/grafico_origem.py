import plotly.express as px
import pandas as pd
from dash import dcc, html
import dash_bootstrap_components as dbc

def grafico_origem_visual():
    df_fake = pd.DataFrame({
        "Origem": ["Google Ads", "Meta Ads", "Orgânico", "Direto", "Email"],
        "Visitas": [3000, 9000, 5000, 3000, 8229]
    })

    fig = px.bar(
        df_fake, 
        x='Origem',           
        y='Visitas',          
        text='Visitas',       
        color='Origem',       
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
        title_text="", 
        showgrid=False,
        tickfont=dict(color='white'), 
        linecolor='white' 
    )
    fig.update_yaxes(
        title_text="Total de Visitas",
        showgrid=True,
        gridcolor='rgba(255,255,255,0.2)',
        tickfont=dict(color='white'), 
        linecolor='white' 
    )


    fig.update_traces(textposition='outside', textfont_color='white')


    return dbc.Card(
        dbc.CardBody(
            [
                html.H6("Origem das Visitas", className="card-title", style={'marginBottom': '15px'}),
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