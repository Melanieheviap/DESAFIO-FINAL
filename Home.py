import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
  page_icon=":thumbs_up:",
  layout="wide",
  
)


st.sidebar.write("## Mi primer aplicación para curso FAU")

st.write("### Proyectos Inmobiliarios en la región Metropolitana")

components.html("""
  <iframe width="560" height="315" 
    src="https://www.youtube.com/embed/SfPBtZnpCY0"
    title="YouTube video player" frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen>
  </iframe>
""", height=520)