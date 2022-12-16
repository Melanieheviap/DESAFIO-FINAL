import streamlit as st

import pydeck as pdk
import numpy as np
import matplotlib.pyplot as plt

from utils import geo_data

# Crear una página que presente al menos 2 filtros de tipo multiselect en el Sidebar
# 2 Puntos
# Los filtros deben reflejar el resultado en gráficos en el área central de la página, desplegar gráficos de: barra, línea y torta, estos distribuidos en 3 columnas.
# 3 Puntos

data_proyectos = geo_data()

with st.sidebar:
  st.write("##### Filtros de Información")
  st.write("---")


  comunas_ordenadas = data_proyectos["COMUNA"].sort_values().unique()
  
  comuna_selector = st.multiselect(
    label="Comunas",
    options=comunas_ordenadas,
    default=[]
  )
  
  if not comuna_selector:
    comuna_selector = comunas_ordenadas.tolist()

  tipo_ordenadas = data_proyectos["TIPO PROYECTO"].sort_values().unique()  

  tipo_selector = st.multiselect(
    label="Proyectos Habitacionales por Comuna",
    options=tipo_ordenadas,
    default=[]
  )
  
  if not tipo_selector:
    tipo_selector = tipo_ordenadas.tolist()

  geo_data = data_proyectos.query("COMUNA == @comuna_selector")
    

col_bar, col_pie, col_line = st.columns(3, gap="small")

group_comuna = data_proyectos.groupby(["COMUNA"]).size()
group_comuna.sort_values(axis="index", ascending=False, inplace=True)
top10 = group_comuna[0:10]

def formato_porciento(dato: float):
  return f"{round(dato, ndigits=2)}%"

with col_bar:
  bar = plt.figure()
  group_comuna.plot.bar(
    title="Cantidad por Comuna",
    label="Total de Puntos",
    xlabel="Comuna",
    ylabel="Cantidad",
    color="lightblue",
    grid=True,
  ).plot()
  st.pyplot(bar)  

with col_pie:
  pie = plt.figure()
  top10.plot.pie(
    y="index",
    title="Cantidad por Comuna",
    legend=None,
    autopct=formato_porciento
  ).plot()
  st.pyplot(pie)

with col_line:
  line = plt.figure()
  top10.plot.line(
    title="Cantidad por Comuna",
    label="Total de Puntos",
    xlabel="Comuna",
    ylabel="Cantidad",
    color="red",
    grid=True
  ).plot()
  st.pyplot(line)

