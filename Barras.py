import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import numpy as np



#Title
st.markdown("<h1 style='text-align: center; color: White;'>Gráficos de Barras </h1>", unsafe_allow_html=True)
#Loading data
@st.cache
def cargar_datos(filename: str):
    return pd.read_csv(filename)

datos = cargar_datos("Colombianos_registrados.csv")

st.markdown("# Cantidad de personas por área de conocimiento de los colombianos en el exterior")

@st.cache(allow_output_mutation=True)
def graph_bar(df):
    fig =  px.bar(
        df.groupby(["Área Conocimiento", "Cantidad de personas"])
        .count()
        .reset_index(),
        color_discrete_sequence=["Blue"],
        x ="Área Conocimiento",
        y ="Cantidad de personas",
        log_y=True)
    return fig

st.plotly_chart(
   graph_bar(datos),
    use_container_width=False, 
)


st.markdown("# Nivel academico de colombianos en el exterior")

@st.cache(allow_output_mutation=True)
def graph_bar1(df):
    fig = px.bar(
        df.groupby(["Nivel Académico", "Cantidad de personas"])
        .count()
        .reset_index(),
        color_discrete_sequence=["Blue"],
        x ="Nivel Académico",
        y ="Cantidad de personas",
        log_y=True
    )
    return fig

st.plotly_chart(
    graph_bar1(datos),
    use_container_width=False, 
)