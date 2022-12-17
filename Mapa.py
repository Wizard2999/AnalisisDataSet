import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

#Title
st.markdown("<h1 style='text-align: center; color: White;'>Mapa Interactivo. </h1>", unsafe_allow_html=True)
st.markdown("Revision de colombianos por todo el mapa")
#Loading data
@st.cache(allow_output_mutation=True)
def cargar_datos1(filename: str):
    return pd.read_csv(filename)

datos = cargar_datos1("Colombianos_registrados.csv")

#Mapping
#@st.cache(allow_output_mutation=True)
#op = [x for x in datos["País"]]
#pais = st.selectbox(label="fgdfg0", options=op)
#data = datos[datos["País"]=="ESPAÑA"]
pais = st.selectbox(label="Busqueda por pais", options=datos["País"].unique())
def grap(df,ps):
    df = df[df["País"]==ps]
    fig = px.scatter_mapbox(df,
                        lat=df.LocalizaciónY,
                        lon=df.LocalizaciónX,
                        size="Cantidad de personas",
                        zoom=6,
                        hover_data=["Cantidad de personas"],
                        hover_name="País",
                        color_discrete_sequence=["fuchsia"],
                        #center = {'lat': 8.74798, 'lon': -75.88143},
                        #size_max=15,
                        #height=300
                        #projection="natural earth"
                        )
    fig.update_layout(mapbox_style="open-street-map")
    #fig.update_traces(cluster=dict(enabled=True))
    #fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

st.plotly_chart(
    grap(datos,pais),
    use_container_width=True,
)
