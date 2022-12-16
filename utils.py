import streamlit as st
import pandas as pd
from datetime import date

fecha_actual = date.today()
print(fecha_actual)

@st.cache
def geo_data():
  bip=pd.read_excel("BBDD_PROYECTOS.xlsx", header=0)

  data_columnas = bip[ ["ID","NOMBRE", "DIRECCIÓN", "COMUNA", "LATITUD", "LONGITUD", "INMOBILIARIA", "TIPO", "FECHA DE ENTREGA", "SUP. MEDIA OFERTA", "TOTAL UNIDADES PROYECTO", "VIGENCIA"]]
  
  correccion_columnas = data_columnas.rename(columns={
    "NOMBRE": "NOMBRE PROYECTO", 
    "TIPO": "TIPO PROYECTO", 
    "SUP. MEDIA OFERTA": "SUP. PROMEDIO"
  })
  print("Columnas Corregidas", correccion_columnas)
  
  correccion_columnas.dropna(subset=["COMUNA"], inplace=True)
  
  correccion_columnas['FECHA DE PROCESO'] = fecha_actual
  print("Nueva Columna", correccion_columnas)


  return(correccion_columnas)
  


