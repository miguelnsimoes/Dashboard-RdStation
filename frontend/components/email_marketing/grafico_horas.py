import pandas as pd
import plotly.express as px

def grafico_horario_envio(df):
    df['data_envio'] = pd.to_datetime(df['data_envio'], errors='coerce')
    df['hora'] = df['data_envio'].dt.hour

    resumo = (
        df.groupby('hora')
        .agg(
            quantidade_envios=('hora', 'count'),
            media_abertura=('taxa_abertura', 'mean'),
            media_clique=('taxa_clique', 'mean')
        )
        .reset_index()
        .sort_values('hora')
    )

    resumo['media_abertura'] = resumo['media_abertura'].round(2)
    resumo['media_clique'] = resumo['media_clique'].round(2)

    fig = px.line(
        resumo,
        x='hora',
        y='quantidade_envios',
        markers=True,
        title='Quantidade de E-mails Enviados por Hora',
        labels={
            'hora': 'Hora do Dia',
            'quantidade_envios': 'E-mails Enviados',
            'media_abertura': 'Média de Abertura (%)',
            'media_clique': 'Média de Clique (%)'
        },
        hover_data={
            'media_abertura': True,
            'media_clique': True,
            'quantidade_envios': True
        }
    )

    fig.update_traces(
        line=dict(color='#df6919', width=3),
        marker=dict(color='#df6919', size=8, line=dict(color='white', width=1))
    )

    fig.update_layout(
        plot_bgcolor='rgba(15, 17, 26, 1)',
        paper_bgcolor='rgba(10, 12, 20, 1)',
        title=dict(
            font=dict(family='Montserrat', size=18, color='white'),
            x=0.5,
            xanchor='center'
        ),
        xaxis=dict(
            tickmode='linear',
            tick0=0,
            dtick=1,
            title=dict(text='Hora do Dia', font=dict(size=14, color='#DADADA')),
            tickfont=dict(size=12, color='#CCCCCC'),
            gridcolor='rgba(255,255,255,0.1)',
            zeroline=False
        ),
        yaxis=dict(
            title=dict(text='E-mails Enviados', font=dict(size=14, color='#DADADA')),
            tickfont=dict(size=12, color='#CCCCCC'),
            gridcolor='rgba(255,255,255,0.1)',
            zeroline=False
        ),
        font=dict(family='Montserrat', color='white'),
        margin=dict(l=50, r=40, t=80, b=50),
        hovermode='x unified',
        hoverlabel=dict(
            bgcolor='rgba(30,144,255,0.9)',
            bordercolor='rgba(255,255,255,0.2)',
            font_size=16,
            font_family='Montserrat',
            font_color='white'
        ),
        showlegend=False
    )

    return fig
