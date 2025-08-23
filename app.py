import plotly.express as px
import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')


df = pd.DataFrame({
    "Animal": ["Perro", "Gato", "Loro", "Pez"],
    "Cantidad": [10, 15, 7, 3]
})

fig = px.bar(df, x="Animal", y="Cantidad", title="Cantidad de animales")
fig.show()  # Abre el gráfico en el navegador
