import streamlit as st
st.title("Evidencia Programacion Avanzada.")

with st.sidebar:
  st.subheader("Portafolio Programacion Avanzada")
  parrafo = (
    "Estudiante:"
    "Kevin Alexander Londoño Berrio"
  )
  st.write(parrafo)

col1, col2, col3, col4 = st.columns(4)

with col1:
 
 st.subheader("Vectores y matrices")
 url = "https://class12-08-buyjccl7jojmcxafltv9jh.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Calculo aplicado, gradiente.")
 url = "https://mw33faex2t89qg6mgbhatv.streamlit.app"
 st.write(f"[Enlace]({url})")

 st.subheader("Lógica, Big-O y Vectorización")
 url = "https://apqdekipvxawtttsi5fnfw.streamlit.app"
 st.write(f"[Enlace]({url})")

 st.subheader("Preparación de datos")
 url = "https://clsxccsmbpieulgdwcjbud.streamlit.app"
 st.write(f"[Enlace]({url})")

with col2: 

 st.subheader("Aplicación Preparación de datos")
 url = "https://vldlaxshnvhetqtymp7hse.streamlit.app"
 st.write(f"[Enlace]({url})")

 st.subheader("Regresión Lineal")
 url = "https://fjtsmjyw3w9cxahppk5e8r.streamlit.app"
 st.write(f"[Enlace]({url})")

 st.subheader("Series de Tiempo.")
 url = "https://f2q6cyoeo59flcp9edt7hn.streamlit.app"
 st.write(f"[Enlace]({url})")
  
 st.subheader("Aplicación: Predicción y modelado de la calidad de aire.")
 url = "https://vldlaxshnvhetqtymp7hse.streamlit.app"
 st.write(f"[Enlace]({url})")

with col3: 

 
 st.subheader("Sistema de IoT Captura de datos y procesamiento.")
 url = "https://bncqfo3fkcj2wgy2ppfbht.streamlit.app"
 st.write(f"[Enlace]({url})")

 st.subheader("De la regresión lineal a la logísitica.")
 url = "https://mxzgszmi5mm9c5zycm97nh.streamlit.app"
 st.write(f"[Enlace]({url})")

 st.subheader("Clasificación Knn")
 url = "https://docs.google.com/document/d/1HE76I49h-TEm-6Y51W0I737hu1vcI9W3MOHQzUSNfqs/edit?usp=sharing"
 st.write(f"[Enlace]({url})")

 st.subheader("Aplicación Knn: Clasificación de fertilidad de  suelos")
 url = "https://mpqqpyfq4spvldedmje5gw.streamlit.app"
 st.write(f"[Enlace]({url})")

with col4:
  
 st.subheader("Visualización de Datos, Story telling y PCA para datos energéticos")
 url = "https://docs.google.com/document/d/1Mod59Ps7cl2dn1uvrFTXgoPijxnAiVxIlJciDsrhP4Y/edit?usp=sharing"
 st.write(f"[Enlace]({url})")
