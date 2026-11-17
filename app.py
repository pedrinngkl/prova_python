import streamlit as st
import pandas as pd
import openpyxl
import plotly.express as px

st.set_page_config(page_title="Pessoas com Mestrado - Homens e Mulheres", layout="wide")

st.title("Pessoas com Mestrado - Homens e Mulheres")
st.sidebar.header("Controles")
opcao = st.sidebar.radio("Selecione a visualização:", ["Tabela", "Gráficos"])

df = pd.read_excel("dados-educacao.xlsx", engine="openpyxl")
st.dataframe(df)

df_filtrado = pd.DataFrame(df)

df_filtrado = df[
    (df["escolaridade"].isin(["Mestrado"]))
].copy()

df_tabela = df_filtrado[["escolaridade"]]

if opcao == "Tabela":
    st.dataframe(df_tabela, use_container_width=True, hide_index=True)

elif opcao == "Gráficos":
    st.subheader("1. Gráfico de Linha — mestrado")
df_idade = df_tabela[df_tabela["escolaridade"] == "Mestrado"]

fig_linha_mestrado = px.line(
    df_idade,
    x="escolaridade",
    y="escolaridade",
    markers=True,
    title="Idade de pessoas com mestrado",
    template="plotly_dark"
)
fig_linha_mestrado.update_traces(line_color="#FF6B6B", line_width=3, marker_size=8)
fig_linha_mestrado.update_xaxes(type="category")
fig_linha_mestrado.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
st.plotly_chart(fig_linha_mestrado, use_container_width=True)
