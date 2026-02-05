import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Dashboard RH - People Analytics",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILO CSS PERSONALIZADO (Para deixar mais "clean") ---
st.markdown("""
<style>
    [data-testid="stMetricValue"] {
        font-size: 24px;
    }
    .css-1d391kg {
        padding-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# --- FUNÇÃO PARA GERAR DADOS FICTÍCIOS (MOCK DATA) ---
@st.cache_data
def get_data():
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    
    data = []
    base_colaboradores = 350
    
    for mes in meses:
        admissoes = np.random.randint(5, 15)
        desligamentos = np.random.randint(2, 12)
        base_colaboradores = base_colaboradores + admissoes - desligamentos
        turnover = (desligamentos / base_colaboradores) * 100
        
        data.append({
            "Mês": mes,
            "Total Colaboradores": base_colaboradores,
            "Admissões": admissoes,
            "Desligamentos": desligamentos,
            "Turnover (%)": round(turnover, 2),
            "Meta Turnover": 3.0
        })
    
    return pd.DataFrame(data)

df = get_data()

# --- BARRA LATERAL (FILTROS) ---
st.sidebar.header("🎛️ Filtros Globais")

# Filtros visuais simulados (na vida real filtrariam o DataFrame)
st.sidebar.subheader("Estrutura Organizacional")
empresas = st.sidebar.multiselect(
    "Empresa",
    ["Asteca", "Autopetro", "Cifal", "Sollus", "Transveloz"],
    default=["Asteca", "Cifal"]
)

areas = st.sidebar.multiselect(
    "Área",
    ["Administrativo", "Comercial", "Operacional", "TI", "Logística"],
    default=["Comercial", "Operacional"]
)

centros_custo = st.sidebar.multiselect(
    "Centro de Custo",
    ["Adm. Pessoal", "Vendas", "Fabrica 01", "Fabrica 02"],
    default=["Vendas", "Fabrica 01"]
)

st.sidebar.markdown("---")
periodo = st.sidebar.slider(
    "Período de Análise",
    min_value=datetime(2025, 1, 1),
    max_value=datetime(2025, 12, 31),
    value=(datetime(2025, 1, 1), datetime(2025, 12, 31)),
    format="DD/MM/YY"
)

# --- CABEÇALHO ---
st.title("📊 Dashboard de People Analytics")
st.markdown(f"**Visão Geral:** Acompanhamento de Headcount e Turnover ({', '.join(empresas)})")
st.markdown("---")

# --- KPIs (INDICADORES DE TOPO) ---
# Cálculo dos totais para exibir nos cartões
total_colaboradores = df["Total Colaboradores"].iloc[-1] # Último mês
total_desligamentos = df["Desligamentos"].sum()
media_turnover = df["Turnover (%)"].mean()
meta_global = 36.0 # Exemplo da imagem

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="👥 Total Colaboradores (Atual)", value=total_colaboradores, delta="5 vs mês anterior")
with col2:
    st.metric(label="🔻 Total Desligamentos (Ano)", value=total_desligamentos, delta="-2% vs ano passado")
with col3:
    st.metric(label="🔄 Turnover Médio", value=f"{media_turnover:.2f}%", delta=f"{media_turnover - 3.0:.1f}p.p.", delta_color="inverse")
with col4:
    st.metric(label="🎯 Meta Anual", value=f"{meta_global}%")

st.markdown("---")

# --- LAYOUT PRINCIPAL ---
# Dividir em: Gráfico Principal (Esquerda) e Medidores (Direita)
col_main, col_gauge = st.columns([2, 1])

with col_main:
    st.subheader("📈 Evolução: Headcount vs Turnover")
    
    # Criar gráfico combinado (Combo Chart) com Plotly
    fig_combo = go.Figure()

    # Barras: Total de Colaboradores
    fig_combo.add_trace(go.Bar(
        x=df["Mês"],
        y=df["Total Colaboradores"],
        name="Total Colaboradores",
        marker_color='#2E86C1',
        yaxis='y'
    ))

    # Linha: Turnover
    fig_combo.add_trace(go.Scatter(
        x=df["Mês"],
        y=df["Turnover (%)"],
        name="Turnover %",
        mode='lines+markers+text',
        text=df["Turnover (%)"],
        textposition="top center",
        marker=dict(size=8, color='#E74C3C'),
        line=dict(width=3, color='#E74C3C'),
        yaxis='y2'
    ))

    # Configuração dos dois eixos Y
    fig_combo.update_layout(
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=450,
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        yaxis=dict(
            title="Nº Colaboradores",
            showgrid=False
        ),
        yaxis2=dict(
            title="Turnover (%)",
            overlaying='y',
            side='right',
            showgrid=False
        )
    )
    
    st.plotly_chart(fig_combo, use_container_width=True)

with col_gauge:
    st.subheader("🎯 Metas de Turnover")
    
    # Gráfico de Velocímetro (Gauge Chart) 1
    fig_gauge1 = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = 47.03,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Turnover Geral (%)", 'font': {'size': 18}},
        delta = {'reference': 36.0, 'increasing': {'color': "red"}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "white"},
            'bar': {'color': "#3498DB"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 36], 'color': "rgba(0, 255, 0, 0.3)"},
                {'range': [36, 100], 'color': "rgba(255, 0, 0, 0.3)"}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 36.0}
        }
    ))
    fig_gauge1.update_layout(height=250, margin=dict(l=20, r=20, t=30, b=20), paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_gauge1, use_container_width=True)

    # Gráfico de Velocímetro (Gauge Chart) 2
    fig_gauge2 = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 38.53,
        title = {'text': "Sem Reduções (%)", 'font': {'size': 18}},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': "#F1C40F"},
            'steps': [
                {'range': [0, 36], 'color': "gray"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 36.0}
        }
    ))
    fig_gauge2.update_layout(height=250, margin=dict(l=20, r=20, t=30, b=20), paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_gauge2, use_container_width=True)

# --- TABELA DETALHADA ---
st.markdown("### 📋 Detalhamento Mensal")

# Usando st.dataframe com column_config para formatação visual sem depender do matplotlib
st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Mês": st.column_config.TextColumn("Mês"),
        "Total Colaboradores": st.column_config.NumberColumn(
            "Total Colaboradores",
            format="%d 👤"
        ),
        "Admissões": st.column_config.NumberColumn(
            "Admissões",
            format="%d 🟢"
        ),
        "Desligamentos": st.column_config.NumberColumn(
            "Desligamentos",
            format="%d 🔴"
        ),
        "Turnover (%)": st.column_config.ProgressColumn(
            "Turnover (%)",
            format="%.2f%%",
            min_value=0,
            max_value=10,  # Ajuste conforme o range esperado
        ),
        "Meta Turnover": st.column_config.NumberColumn(
            "Meta (%)",
            format="%.1f%%"
        ),
    }
)