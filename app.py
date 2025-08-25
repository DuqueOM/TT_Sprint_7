"""
Este módulo trabaja un DF de vehículos usados en EE.UU. 
Permite al usuario generar una muestra aleatoria del DF,
y visualizar gráficos interactivos.
Autor: Wberto Duque Ortega Mutis
Fecha: 2025-08-25
"""

import plotly.express as px
import pandas as pd
import streamlit as st

st.image("tt.png", use_container_width=True)

# ----------------- Títulos centrados -----------------

st.markdown("<h1 style='text-align: center;'>PROYECTO SPRINT 7</h1>",
            unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Análisis de Datos de Vehículos en EE.UU</h4>",
            unsafe_allow_html=True)
st.markdown("##### \nEjemplo de tabla")

# ----------------- Leer datos -----------------

df = pd.read_csv('vehicles_us.csv')

# Renombrar columnas
df.columns = ['Precio', 'Año', 'Modelo', 'Condición', 'Cilindros',
              'Combustible', 'Kilometraje', 'Transmisión', 'Tipo',
              'Color', 'Tracción 4×4', 'Fecha de publicación', 'Días en lista']

# Columnas numéricas y relevantes para el análisis gráfico
numeric_cols = ["Precio", "Año",
                "Kilometraje", "Cilindros", "Días en lista"]


# ----------------- Mostrar muestra aleatoria -----------------

# Botón para generar muestra
if st.button("Generar ejemplo"):
    st.session_state['sample_df'] = df.sample(5)

# Mostrar la muestra si existe
if "sample_df" in st.session_state:
    st.write(st.session_state['sample_df'])

# ----------------- Checkboxes mutuamente excluyentes -----------------

if "check1" not in st.session_state:
    st.session_state.check1 = False
if "check2" not in st.session_state:
    st.session_state.check2 = False

# Funciones para manejar el cambio


def toggle_check1():
    """
    Aplica las condiciones de estado del checkbox 1.
    """
    if st.session_state.check1:
        st.session_state.check2 = False  # Desactivar el otro


def toggle_check2():
    """
    Aplica las condiciones de estado del checkbox 1.
    """
    if st.session_state.check2:
        st.session_state.check1 = False  # Desactivar el otro


st.header("Selección de Gráficos")
# Crear dos columnas
col1, col2 = st.columns(2)

# Checkbox en la primera columna
with col1:
    checkbox1 = st.checkbox("Histograma", value=st.session_state.check1,
                            key="check1", on_change=toggle_check1)

# Checkbox en la segunda columna
with col2:
    checkbox2 = st.checkbox("Gráfico de dispersión", value=st.session_state.check2,
                            key="check2", on_change=toggle_check2)


# ----------------- Histograma -----------------

if checkbox1:
    # Selector de columna
    columna_seleccionada = st.selectbox(
        "Selecciona una columna para el histograma:", numeric_cols
    )

    if 'hist_generado' not in st.session_state:
        st.session_state['hist_generado'] = False
    if 'ultima_columna' not in st.session_state:
        st.session_state['ultima_columna'] = None

# Función para generar histograma al presionar el botón

    def generar_histograma():
        """
        Aplica las condiciones de session state al gráfico de histograma.
        """
        st.session_state['hist_generado'] = True
        st.session_state['ultima_columna'] = columna_seleccionada

    st.button("Generar Histograma", on_click=generar_histograma)
    st.slider(
        "Número de bins",
        10,
        100,
        value=50,
        key='nbins'
    )
    if st.session_state['hist_generado'] and \
            st.session_state['ultima_columna'] == columna_seleccionada:
        fig = px.histogram(
            df,
            x=columna_seleccionada,
            nbins=st.session_state['nbins'],
            title=f"Distribución de {columna_seleccionada}"
        )
        st.plotly_chart(fig, key='histograma')

# ----------------- Gráfico de dispersión -----------------

if st.session_state.check2:

    columna_disp_x = st.selectbox(
        "Selecciona una columna para el eje X del"
        "gráfico de dispersión:", numeric_cols, key='col_disp_x')
    columna_disp_y = st.selectbox(
        "Selecciona una columna para el eje Y del"
        "gráfico de dispersión:", numeric_cols, key='col_disp_y')


# Inicializar session_state
    if 'dispersion_generado' not in st.session_state:
        st.session_state['dispersion_generado'] = False
    if 'ultima_columna_x' not in st.session_state:
        st.session_state['ultima_columna_x'] = None
    if 'ultima_columna_y' not in st.session_state:
        st.session_state['ultima_columna_y'] = None
# Función para generar dispersión al presionar el botón

    def generar_dispersion():
        """
        Aplica las condiciones de session state al gráfico de dispersión.
        """
        st.session_state['dispersion_generado'] = True
        st.session_state['ultima_columna_x'] = columna_disp_x
        st.session_state['ultima_columna_y'] = columna_disp_y


# Botón para generar dispersión
    st.button("Generar gráfico de dispersión", on_click=generar_dispersion)


# Mostrar dispersión solo si ya fue generado y no cambió la columna
    if st.session_state['dispersion_generado'] and \
            st.session_state['ultima_columna_x'] == columna_disp_x and \
            st.session_state['ultima_columna_y'] == columna_disp_y:
        fig = px.scatter(df, x=columna_disp_x, y=columna_disp_y,  # Asumí 'Precio' para eje Y
                         title=f"Distribución de {columna_disp_x} vs {columna_disp_y}")
        st.plotly_chart(fig, key='dispersion')
