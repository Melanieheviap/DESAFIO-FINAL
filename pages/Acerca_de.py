import streamlit as st
import streamlit.components.v1 as components

st.write("## Mi primera Aplicación Web para Curso de Visualización de Datos Geográficos en Internet")

components.html("""
<div style="background: gray;border-radius: 5px;padding: 10px 25px;">
  <h3>
    Creado para el curso de FAU - 2022
  </h3>
  <p>
    Creado por: <b>Melanie L. Hevia P.</b>
  </p>
  <p>
    Contacto: <b>melanieheviap@gmail.com</b>
  </p>
  <p>
    LinkedIn: <b><a href=”https://cl.linkedin.com/in/melanieheviapiña”>https://cl.linkedin.com/in/melanieheviapiña</a></b>
  </p>
</div>
""",width=620, height=330)