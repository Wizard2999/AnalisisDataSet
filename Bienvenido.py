import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(layout="wide")
st.header("App para el Diplomado de Python")
APP_TITLE = 'Colombianos en el Extranjero'

@st.cache
def cargar_datos(filename: str):
    return pd.read_csv(filename)

datos = cargar_datos("Colombianos_registrados.csv")

st.markdown("<h1 style='text-align: center; color: White;'>BIENVENIDOS </h1>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("Bienvenidos al tablero digital del Grupo , en este tablero se mostraran datos los cuales creemos que son relevantes para la toma de desiciones. Los datos utilizados para este análisis tiene por nombre Colombianos Registrados en el Extranjero, dicho dataset se encuentra información sociodemografica de los colombianos que se encuentran en el extranjero.")

st.markdown("---")

st.markdown("Número de Colombianos en el extranjero.")
st.markdown('{:,}'.format(datos['Cantidad de personas'].sum()))
