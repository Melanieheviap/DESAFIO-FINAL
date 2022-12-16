import os
import streamlit as st
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()
# Leer variable de API KEY desde archivo externo
WEATHER_API_KEY=os.getenv("API_KEY", "123APIKEY")

# Definir lugar a consultar
ubicacion = "Santiago,cl"
# Crear conexión a la API
URL = f"https://api.openweathermap.org/data/2.5/weather?q={ubicacion}&APPID={WEATHER_API_KEY}&lang=es&units=metric"
datos = requests.get(URL)

# Obetener datos desde la API
datos_json = datos.json()

# Configurar Aplicación
st.set_page_config(
  layout="wide"
)

# Mostrar datos en la Aplicación
st.header("Información desde API")

st.info("Temperaturas de una Comuna")
st.success(f"El clima ahora está: {datos_json['weather'][0]['description']}")
st.success(f"La Temperatura actual es: {datos_json['main']['temp']} °C")
st.success(f"La Sensación térmica actual es: {datos_json['main']['feels_like']} °C")
st.success(f"La Velocidad del viento es: {datos_json['wind']['speed']} m/seg")
st.write(datos_json)