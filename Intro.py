import streamlit as st
from PIL import Image
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
 image = Image.open('{2A992445-356A-4541-B2C2-FBE8C68D4F54}.png')
 st.image(image, width=190)
 url = "https://class12-08-buyjccl7jojmcxafltv9jh.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Calculo aplicado, gradiente.")
 image = Image.open('{50CAA878-5A09-4237-BC38-B880877E541A}.png')
 st.image(image, width=190)
 url = "https://mw33faex2t89qg6mgbhatv.streamlit.app"
 st.write(f"[Enlace]({url})")

 st.subheader("Lógica, Big-O y Vectorización")
 image = Image.open('{D439EFA6-6749-47D9-BE7D-DA2DBD978A85}.png')
 st.image(image, width=190)
 url = "https://apqdekipvxawtttsi5fnfw.streamlit.app"
 st.write(f"[Enlace]({url})")

 st.subheader("Preparación de datos")
 image = Image.open('{4A1D7660-9AA6-4667-AAF0-69217C051BFB}.png')
 st.image(image, width=190)
 url = "https://clsxccsmbpieulgdwcjbud.streamlit.app"
 st.write(f"[Enlace]({url})")

with col2: 

 st.subheader("Aplicación Preparación de datos")
 image = Image.open('{26BFAEE2-8D4D-46DF-80B3-E9CE1ECA4E83}.png')
 st.image(image, width=190)
 url = "https://vldlaxshnvhetqtymp7hse.streamlit.app"
 st.write(f"[Enlace]({url})")

 st.subheader("Regresión Lineal")
 image = Image.open('{2D50DB2C-F9AC-4B5D-A9BC-3F3A2E3C5542}.png')
 st.image(image, width=190)
 url = "https://fjtsmjyw3w9cxahppk5e8r.streamlit.app"
 st.write(f"[Enlace]({url})")

 st.subheader("Series de Tiempo.")
 image = Image.open('{03400AD7-50FD-4CB1-A90F-D768969F7606}.png')
 st.image(image, width=190)
 url = "https://f2q6cyoeo59flcp9edt7hn.streamlit.app"
 st.write(f"[Enlace]({url})")
  
 st.subheader("Aplicación: Predicción y modelado de la calidad de aire.")
 image = Image.open('{609865AD-530B-4CD6-955B-AEAE2436A737}.png')
 st.image(image, width=190)
 url = "https://5gyr9emd8duwbkonhqf7ss.streamlit.app"
 st.write(f"[Enlace]({url})")

with col3: 

 
 st.subheader("Sistema de IoT Captura de datos y procesamiento.")
 image = Image.open('{563E5C3A-48B7-4D1E-A87E-5EF095F25205}.png')
 st.image(image, width=190)
 url = "https://bncqfo3fkcj2wgy2ppfbht.streamlit.app"
 st.write(f"[Enlace]({url})")

 st.subheader("De la regresión lineal a la logísitica.")
 image = Image.open('{1BC3E744-E71D-41A9-B27C-F5A0D60C1980}.png')
 st.image(image, width=190)
 url = "https://mxzgszmi5mm9c5zycm97nh.streamlit.app"
 st.write(f"[Enlace]({url})")

 st.subheader("Clasificación Knn")
 image = Image.open('{2BB767FC-FDD3-4388-9614-52C316FBE842}.png')
 st.image(image, width=190)
 url = "https://docs.google.com/document/d/1HE76I49h-TEm-6Y51W0I737hu1vcI9W3MOHQzUSNfqs/edit?usp=sharing"
 st.write(f"[Enlace]({url})")

 st.subheader("Aplicación Knn: Clasificación de fertilidad de  suelos")
 image = Image.open('{DB8E539B-B51F-4871-ACC9-124013A1648B}.png')
 st.image(image, width=190)
 url = "https://mpqqpyfq4spvldedmje5gw.streamlit.app"
 st.write(f"[Enlace]({url})")

with col4:
  
 st.subheader("Visualización de Datos, Story telling y PCA para datos energéticos")
 image = Image.open('{DE7FECD3-6BB2-4F4E-8E3A-C852953BC55E}.png')
 st.image(image, width=190)
 url = "https://docs.google.com/document/d/1Mod59Ps7cl2dn1uvrFTXgoPijxnAiVxIlJciDsrhP4Y/edit?usp=sharing"
 st.write(f"[Enlace]({url})")
