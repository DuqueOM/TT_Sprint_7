import plotly.express as px
import plotly.graph_objects as go
import pandas as pd  # Importación de plotly.graph_objects como go
import streamlit as st

# Leer los datos del archivo CSV
df = pd.read_csv('vehicles_us.csv')

st.title("SPRINT 7\n")
st.header("VEICLES US")
# leer dataset

lista = df.columns.tolist()

numeric_cols = df.select_dtypes(include='number').columns.tolist()
columna_seleccionada = st.selectbox("Selecciona columna:", numeric_cols)

if st.button("Generar Histograma"):
    nbins = st.slider("Número de bins", 10, 100, 50)
    st.session_state.nbins = True

    fig = px.histogram(df, x=columna_seleccionada, nbins=nbins,
                       title=f"Distribución de {columna_seleccionada}")
    st.plotly_chart(fig)
