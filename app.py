import streamlit as st 
import pandas as pd

st.set_page_config(
    page_title="SistenCard",
    page_icon="🌏",
    layout="wide"
)

lateral = st.sidebar
data = lateral.date_input("Selicione a data")
cidade = lateral.selectbox("Selecione a cidade",
                           ["Belo Horizonte", "Rio de Janeiro", "Manaus"])


@st.cache_data
def carregar_dados():
    dados = pd.read_csv("acidentes.csv")
    return dados

dados = carregar_dados()
st.session_state["dados"] = dados
st.session_state["data"] = data
st.session_state["cidade"] = cidade



st.title("Dados")

col1, col2 = st.columns([0.7, 0.3])

tabela = col1.dataframe(dados)

municipios = dados["municipio"].value_counts()
col2.bar_chart(municipios)

st.subheader("Cidade")
st.write(f"Cidade Selecionada {cidade}")











