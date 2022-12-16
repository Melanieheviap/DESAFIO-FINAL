import streamlit as st
import pandas as pd
from datetime import date
import os
import requests
from dotenv import load_dotenv
import json

fecha_actual = date.today()
print(fecha_actual)

bip=pd.read_excel("BBDD_PROYECTOS.xlsx", header=0)
print("BBDD Proyectos", bip)

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

load_dotenv()
WEATHER_API_KEY=os.getenv("API_KEY", "123APIKEY")

ubicacion = "Macul,cl"

URL = f"https://api.openweathermap.org/data/2.5/weather?q={ubicacion}&APPID={WEATHER_API_KEY}&lang=es&units=metric"
datos = requests.get(URL)

datos_api = datos.json()

st.set_page_config(
  layout="wide"
)
st.header("Información desde API")

st.info("Temperaturas de una Comuna")
st.success(f"El clima ahora está: {datos_api['weather'][0]['description']}")
st.success(f"La Temperatura actual es: {datos_api['main']['temp']} °C")
st.success(f"La Sensación térmica actual es: {datos_api['main']['feels_like']} °C")
st.success(f"La Velocidad del viento es: {datos_api['wind']['speed']} m/seg")
st.write(datos_api)
