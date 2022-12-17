import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.markdown("<h1 style='text-align: center; color: White;'>Predicción </h1>", unsafe_allow_html=True)
@st.cache
def cargar_datos(filename: str):
    return pd.read_csv(filename)

datos = cargar_datos("Colombianos_registrados.csv")

st.markdown('En base a que aparecen en la parte de abajo se puede predecir el país al que nos puede ir mejor si decidimos salir al extranjero')

area = st.selectbox(label="Área de Conocimiento", options=datos["Área Conocimiento"].unique())
sub = st.selectbox(label="Sub Área de Conocimiento", options=datos["Sub Area Conocimiento"].unique())
estado = st.selectbox(label="Estado Civil", options=datos["Estado civil"].unique())
nivel = st.selectbox(label="Nivel Académico", options=datos["Nivel Académico"].unique())


request_data = [
    {
        "Area_Conocimiento": area ,
        "Sub Área de Conocimiento": sub,
        "Estado Civil": estado,
        "Nivel Academico": nivel
    }
]