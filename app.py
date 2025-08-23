import plotly.express as px
import pandas as pd
import streamlit as st

st.title("SPRINT 7")
st.header("VEHICLES US")  # Corregí "VEICLES" a "VEHICLES"

# Leer los datos del archivo CSV
df = pd.read_csv('vehicles_us.csv')

# Obtener columnas numéricas
numeric_cols = df.select_dtypes(include='number').columns.tolist()

# Selector de columna para el histograma
columna_seleccionada = st.selectbox(
    "Selecciona una columna para realizar el histograma:", numeric_cols
)

# Inicializar número de bins en el estado de la sesión
if 'mi_numero' not in st.session_state:
    st.session_state['mi_numero'] = 50

# Slider para número de bins
nbins = st.slider("Número de bins", 10, 100, 50, key='mi_numero')

# Botón para generar el histograma
if st.button("Generar Histograma"):
    fig = px.histogram(
        df,
        x=columna_seleccionada,
        nbins=nbins,
        title=f"Distribución de {columna_seleccionada}"
    )
    st.plotly_chart(fig)
