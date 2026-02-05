import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# --- 1. CONFIGURAÇÃO DA PÁGINA (Do app.py) ---
st.set_page_config(
    page_title="Dashboard RH - People Analytics",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILO CSS (Do app.py) ---
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

# --- 2. DADOS (Do Teste.py) ---
# Nota: Incluí os dados que estavam no ficheiro. Se houver mais, adicione à lista.
Dados_teste = [
  { "codcid": 81388, "nomcid": "BEBEDOURO", "admissao": "2020-04-09T08:38:22.040Z", "demissao": "None", "empregis": "None", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 88684, "nomcid": "SOROCABA", "admissao": "2021-07-19T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - SP", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 21415, "nomcid": "QUIRINOPOLIS", "admissao": "2020-08-10T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - GO", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 85448, "nomcid": "MOGI DAS CRUZES", "admissao": "2020-11-03T00:00:00.000Z", "demissao": "None", "empregis": "SMOKERS", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 83518, "nomcid": "GUARATINGUETA", "admissao": "2021-03-22T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - SP", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 88862, "nomcid": "TANABI", "admissao": "2021-03-01T00:00:00.000Z", "demissao": "None", "empregis": "LIKEBRANDS", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 88684, "nomcid": "SOROCABA", "admissao": "2024-02-20T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - SP", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 81388, "nomcid": "BEBEDOURO", "admissao": "2021-03-22T00:00:00.000Z", "demissao": "None", "empregis": "SOLLUS", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 18619, "nomcid": "ARAGARCAS", "admissao": "2021-10-18T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - GO", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 18546, "nomcid": "APARECIDA DE GOIANIA", "admissao": "2021-12-14T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - GO", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 39217, "nomcid": "UBERLANDIA", "admissao": "2021-12-13T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - MG", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 88684, "nomcid": "SOROCABA", "admissao": "2022-04-18T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - SP", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 86568, "nomcid": "PIEDADE", "admissao": "2023-01-03T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - SP", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 81388, "nomcid": "BEBEDOURO", "admissao": "2023-01-03T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - SP", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 31534, "nomcid": "JOAO PINHEIRO", "admissao": "2023-04-03T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - MG", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 21474, "nomcid": "RIO VERDE", "admissao": "2023-03-06T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - GO", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 88412, "nomcid": "SAO PAULO", "admissao": "2023-03-06T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - SP", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 81345, "nomcid": "BATATAIS", "admissao": "2023-11-06T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - SP", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 81086, "nomcid": "AVARE", "admissao": "2023-11-21T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - SP", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 81370, "nomcid": "BAURU", "admissao": "2024-01-16T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - SP", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 34010, "nomcid": "PATOS DE MINAS", "admissao": "2024-04-16T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - MG", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 80829, "nomcid": "ARACATUBA", "admissao": "2024-04-16T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - SP", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 18546, "nomcid": "APARECIDA DE GOIANIA", "admissao": "2024-09-03T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - GO", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 41378, "nomcid": "TRES LAGOAS", "admissao": "2024-09-23T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - MS", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 81990, "nomcid": "CAMPINAS", "admissao": "2019-11-11T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - SP", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 21784, "nomcid": "SAO LUIS DE MONTES BELOS", "admissao": "2021-02-01T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - GO", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 81388, "nomcid": "BEBEDOURO", "admissao": "2022-06-06T00:00:00.000Z", "demissao": "None", "empregis": "SOLLUS", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 88412, "nomcid": "SAO PAULO", "admissao": "2024-02-06T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - SP", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 88412, "nomcid": "SAO PAULO", "admissao": "2022-10-03T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - SP", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 83631, "nomcid": "HORTOLANDIA", "admissao": "2024-07-02T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - SP", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 39217, "nomcid": "UBERLANDIA", "admissao": "2024-10-01T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - MG", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 19917, "nomcid": "GOIAS", "admissao": "2023-01-16T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - GO", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 81388, "nomcid": "BEBEDOURO", "admissao": "2021-03-22T00:00:00.000Z", "demissao": "None", "empregis": "LIKEBRANDS", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 88412, "nomcid": "SAO PAULO", "admissao": "2022-03-14T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - SP", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 40851, "nomcid": "NOVA ANDRADINA", "admissao": "2024-11-05T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - MS", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 56995, "nomcid": "LONDRINA", "admissao": "2024-11-01T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - SP", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 18511, "nomcid": "ANAPOLIS", "admissao": "2021-03-22T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - GO", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 19321, "nomcid": "CERES", "admissao": "2021-09-20T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - GO", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 21318, "nomcid": "PORANGATU", "admissao": "2021-11-22T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - GO", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 20818, "nomcid": "NIQUELANDIA", "admissao": "2023-12-04T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - GO", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 88412, "nomcid": "SAO PAULO", "admissao": "2024-10-15T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - SP", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 83186, "nomcid": "FRANCISCO MORATO", "admissao": "2022-10-17T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - SP", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 39217, "nomcid": "UBERLANDIA", "admissao": "2024-12-10T00:00:00.000Z", "demissao": "None", "empregis": "TBSTORE - ADM", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 21474, "nomcid": "RIO VERDE", "admissao": "2024-06-18T00:00:00.000Z", "demissao": "None", "empregis": "TBSTORE - ADM GO", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 20303, "nomcid": "JATAI", "admissao": "2023-09-04T00:00:00.000Z", "demissao": "None", "empregis": "TBSTORE - ADM GO", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 39209, "nomcid": "UBERABA", "admissao": "2023-10-02T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - MG", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 83097, "nomcid": "FERNANDOPOLIS", "admissao": "2023-02-02T00:00:00.000Z", "demissao": "None", "empregis": "TBSTORE - JBZ", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 88323, "nomcid": "SAO JOSE DO RIO PRETO", "admissao": "2023-02-24T00:00:00.000Z", "demissao": "None", "empregis": "TBSTORE - JBZ", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 20575, "nomcid": "MINEIROS", "admissao": "2025-01-07T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - GO", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 87599, "nomcid": "SALTO", "admissao": "2025-02-04T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - SP", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 18546, "nomcid": "APARECIDA DE GOIANIA", "admissao": "2024-02-20T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - GO", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 83178, "nomcid": "FRANCA", "admissao": "2022-09-02T00:00:00.000Z", "demissao": "None", "empregis": "TBSTORE - CTR", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 81990, "nomcid": "CAMPINAS", "admissao": "2025-02-18T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - SP", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 86665, "nomcid": "PIRACICABA", "admissao": "2021-07-19T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - SP", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 80616, "nomcid": "AMERICANA", "admissao": "2023-06-05T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - SP", "codempresa": 1, "descricao": "CIFAL COMERCIAL " },
  { "codcid": 19070, "nomcid": "CALDAS NOVAS", "admissao": "2025-03-11T00:00:00.000Z", "demissao": "None", "empregis": "CIFAL - GO", "codempresa": 1, "descricao": "CIFAL COMERCIAL " }
  # ... Cole o restante dos dados aqui se a lista for maior
]

# --- 3. PROCESSAMENTO DOS DADOS ---
@st.cache_data
def load_and_process_data(data):
    df = pd.DataFrame(data)
    
    # Converter datas
    df['admissao'] = pd.to_datetime(df['admissao'], errors='coerce')
    
    # Tratar coluna demissao (string 'None' para datetime NaT)
    df['demissao'] = df['demissao'].replace('None', pd.NaT)
    df['demissao'] = pd.to_datetime(df['demissao'], errors='coerce')
    
    return df

df_raw = load_and_process_data(Dados_teste)

# --- 4. FILTROS (Do Teste.py) NA SIDEBAR ---
st.sidebar.header("🔍 Filtros")

# Filtro Empresa
empresa_opcoes = ["Todas"] + sorted(
    df_raw["descricao"].dropna().astype(str).unique().tolist()
)
empresa_selecionada = st.sidebar.selectbox("Empresa", options=empresa_opcoes)

# Filtro Cidade
cidade_opcoes = ["Todas"] + sorted(
    df_raw["nomcid"].dropna().astype(str).unique().tolist()
)
cidade_selecionada = st.sidebar.selectbox("Cidade", options=cidade_opcoes)

# Aplicar Filtros
df_filtered = df_raw.copy()

if empresa_selecionada != "Todas":
    df_filtered = df_filtered[df_filtered["descricao"] == empresa_selecionada]

if cidade_selecionada != "Todas":
    df_filtered = df_filtered[df_filtered["nomcid"] == cidade_selecionada]

# --- 5. AGREGAÇÃO DE DADOS PARA O DASHBOARD ---
# Precisamos transformar os dados individuais em dados mensais para os gráficos
def aggregate_monthly(df_in):
    # Definir range de datas (baseado nos dados ou ano atual)
    # Vamos pegar o intervalo de dados presentes
    if df_in.empty:
        return pd.DataFrame()
        
    min_date = df_in['admissao'].min()
    max_date = datetime.now() # ou df_in['admissao'].max()
    
    # Criar índice mensal
    dates = pd.date_range(start=min_date, end=max_date, freq='MS')
    
    results = []
    
    for date in dates:
        month_start = date
        month_end = date + pd.offsets.MonthEnd(0)
        
        # Admissões no mês
        admissoes = df_in[
            (df_in['admissao'] >= month_start) & 
            (df_in['admissao'] <= month_end)
        ].shape[0]
        
        # Desligamentos no mês
        desligamentos = df_in[
            (df_in['demissao'] >= month_start) & 
            (df_in['demissao'] <= month_end)
        ].shape[0]
        
        # Total Colaboradores Ativos no final do mês
        # Admitidos antes ou durante o mês E (não demitidos OU demitidos depois do mês)
        ativos = df_in[
            (df_in['admissao'] <= month_end) & 
            ((df_in['demissao'].isna()) | (df_in['demissao'] > month_end))
        ].shape[0]
        
        results.append({
            'Mês': month_start.strftime('%b/%Y'),
            'Data': month_start,
            'Total Colaboradores': ativos,
            'Admissões': admissoes,
            'Desligamentos': desligamentos,
            'Turnover %': round((desligamentos / ativos * 100), 2) if ativos > 0 else 0
        })
        
    return pd.DataFrame(results)

df_dashboard = aggregate_monthly(df_filtered)

# --- 6. VISUALIZAÇÃO (KPIs e Gráficos do app.py) ---

# Calcular métricas gerais (Total Atual)
if not df_dashboard.empty:
    total_colaboradores = df_dashboard.iloc[-1]['Total Colaboradores']
    total_admissoes = df_dashboard['Admissões'].sum()
    total_desligamentos = df_dashboard['Desligamentos'].sum()
    media_turnover = df_dashboard['Turnover %'].mean()
else:
    total_colaboradores = 0
    total_admissoes = 0
    total_desligamentos = 0
    media_turnover = 0

# Exibir Métricas
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Colaboradores", f"{total_colaboradores} 👤")
col2.metric("Admissões (Período)", f"{total_admissoes} 🟢")
col3.metric("Desligamentos (Período)", f"{total_desligamentos} 🔴")
col4.metric("Turnover Médio", f"{media_turnover:.1f}% 📉")

# Layout Gráficos
col_charts1, col_charts2 = st.columns(2)

if not df_dashboard.empty:
    with col_charts1:
        st.subheader("Evolução do Headcount")
        fig_line = px.line(
            df_dashboard, 
            x='Mês', 
            y='Total Colaboradores', 
            markers=True,
            line_shape='spline'
        )
        fig_line.update_traces(line_color='#3498db', line_width=3)
        fig_line.update_layout(height=350, margin=dict(l=20, r=20, t=30, b=20))
        st.plotly_chart(fig_line, use_container_width=True)

    with col_charts2:
        st.subheader("Admissões vs Desligamentos")
        fig_bar = go.Figure(data=[
            go.Bar(name='Admissões', x=df_dashboard['Mês'], y=df_dashboard['Admissões'], marker_color='#2ecc71'),
            go.Bar(name='Desligamentos', x=df_dashboard['Mês'], y=df_dashboard['Desligamentos'], marker_color='#e74c3c')
        ])
        fig_bar.update_layout(barmode='group', height=350, margin=dict(l=20, r=20, t=30, b=20))
        st.plotly_chart(fig_bar, use_container_width=True)
else:
    st.info("Sem dados para exibir com os filtros selecionados.")

# --- 7. TABELA DETALHADA ---
st.markdown("### 📋 Detalhamento dos Colaboradores (Dados Filtrados)")
st.dataframe(
    df_filtered[['codcid', 'nomcid', 'admissao', 'demissao', 'empregis', 'descricao']],
    use_container_width=True,
    column_config={
        "admissao": st.column_config.DateColumn("Admissão", format="DD/MM/YYYY"),
        "demissao": st.column_config.DateColumn("Demissão", format="DD/MM/YYYY"),
    }
)