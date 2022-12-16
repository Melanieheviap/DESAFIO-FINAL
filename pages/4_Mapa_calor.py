import streamlit as st

import pydeck as pdk
import numpy as np
import matplotlib.pyplot as plt

from utils import geo_data

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

geo_data = data_proyectos.query(" COMUNA==@comuna_selector ")

if geo_data.empty:
  st.warning("#### No hay registros")
else:
  lat = np.median(geo_data["LATITUD"])
  lng = np.median(geo_data["LONGITUD"])

  puntos = pdk.Deck(
    map_style=None,
      initial_view_state=pdk.ViewState(
          latitude=lat,
          longitude=lng,
          zoom=10,
          min_zoom=10,
          max_zoom=15,
          pitch=10,
      ),
      layers=[
        pdk.Layer(
          "HeatmapLayer",
          data=geo_data,
          pickable=True,
          auto_highlight=True,
          get_position='[LONGITUD, LATITUD]',
          opacity=0.6,
          get_weight=100
        )      
      ],
      tooltip={
        "html": "<b>Nombre Proyecto: </b> {NOMBRE} <br /> "
                "<b>Inmobiliaria: </b> {INMOBILIARIA} <br /> "
                "<b>Dirección: </b> {DIRECCIÓN} <br /> "
                "<b>Comuna: </b> {COMUNA} <br /> "
                "<b>Tipo Proyecto: </b> {TIPO} <br /> "
                "<b>Georeferencia (Lat, Lng): </b>[{LATITUD}, {LONGITUD}] <br /> "
        }
  )

  st.write(puntos)