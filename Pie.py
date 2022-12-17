import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np



#Title
st.markdown("<h1 style='text-align: center; color: White;'>Porcentaje de grupos de edad para los colombianos en el exterior </h1>", unsafe_allow_html=True)
#Loading data
@st.cache
def cargar_datos(filename: str):
    return pd.read_csv(filename)

datos = cargar_datos("Colombianos_registrados.csv")

#body



#graphics
@st.cache(allow_output_mutation=True)
def graph_pie(df):
    fig = px.pie(df.groupby(["Edad (años)", "Grupo edad"]).count().reset_index(),
        values="Edad (años)",
        names="Grupo edad",
        color_discrete_sequence=["Blue"],    
    )
    return fig

st.plotly_chart(
    graph_pie(datos),
    use_container_width=True,
)

