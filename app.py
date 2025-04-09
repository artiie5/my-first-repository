import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar datos
df = pd.read_csv("vehicles_us.csv")

# Crear título
st.header("Análisis de anuncios de venta de coches")

# Crear casillas de verificación
if st.checkbox("Mostrar histograma del odómetro"):
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox("Mostrar gráfico de dispersión Precio vs Odómetro"):
    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
