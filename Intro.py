import streamlit as st
from PIL import Image
st.title("Aplicaciones de Machine Learning y Análisis de Datos")

with st.sidebar:
  st.subheader("Aplicaciones de Machine Learning y Análisis de Datos.")
  parrafo = (
    "La inteligencia artificial y el análisis de datos transforman grandes volúmenes de , "
    "información en conocimiento estratégico, permitiendo automatizar procesos, identificar, "
    "patrones y tomar decisiones más precisas, rápidas e inteligentes."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/computacinavanzada/inicio?pli=1&authuser=0"
st.subheader("En el siguiente enlace puedes encontrar ejercicios prácticos e información útil relacionada al análisis de datos y al machine learning")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Análisis Ríos y Quebras en La Ceja, Antioquia")
 image = Image.open('txt_to_audio2.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace podemos encontrar un estudio de análiss de nivel del agua enfocado en éste caso a los niveles de llde ríos y quebradas de La Ceja, Antioquia") 
 url = "https://appnivelcornare-bkqfxz6qorqesghcdrtkmr.streamlit.app/"
 st.write(f"Enlace app: [Enlace]({url})")

 st.subheader("Predictor de calidad de aire")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace podemos ver el análisis de la calidad del aire en un área específica, relacionando un archivo de datos de cierta área realizado por Cornare") 
 url = "https://apppron-sticoairecornare-zvdempatq2pygdzewws59m.streamlit.app/"
 st.write(f"Enlace app: [Enlace]({url})")

 st.subheader("Regresión logística de Lluvia")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace podemos observar el estudio probabilístico tomando diferentes factores en cuenta para determinar la probabilidad de lluvias en un sector en específico.") 
 url = "https://appregresionlogistica-6m6jzsezvhh7eozbvgfydd.streamlit.app/"
 st.write(f"Enlace app: [Enlace]({url})")

with col2: 
 st.subheader("Series de tiempo")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente se puede observar un aplicativo enfocado a series de tiempo con el modelo SARIMA por medio de un simulador de dispositivo iot para explicar el impacto y el relacionamiento de los conceptos de series de tiempo.") 
 url = "https://appseriestiempo-gab5wq5rzbuyfxwuwjkwwd.streamlit.app/"
 st.write(f"Enlace app: [Enlace]({url})")

 st.subheader("Descenso de gradiente")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace se puede observar un simulador visual e interactivo para entender como funciona el algoritmo de Descenso de Gradiente en la optimización de funciones matemáticas.") 
 url = "https://tomasg15-app-gradient-app-gradient-rama2-4cmcjp.streamlit.app/"
 st.write(f"Enlace app: [Enlace]({url})")

 st.subheader("Detector de Anomalías")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace podemos observar como funciona la detección de anomalías mediante lógica condicional, y como optimizar este proceso usando NumPy y análisis de complejidad computacional (Big-O.") 
 url = "https://detector-anomal-as-h3tvmqfn3buwpbgkhgxx3p.streamlit.app/"
 st.write(f"Enlace app: [Enlace]({url})")


with col3: 
 st.subheader("Análisis de futas")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En el siguiente enlace vemos un aplicativo interactivo el cual analiza diferentes cualidades y propiedades de una fruta para al final, determinar a cual de las 4 opciones disponibles se parece.") 
 url = "https://frutasapppy-cawrkr6g3napm5uac9xfg4.streamlit.app/"
 st.write(f"Enlace app: [Enlace]({url})")

 st.subheader("Estudio de fertilidad de Suelos")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En el siguiente aplicativo podemos observar una herramienta para entender como la IA puede clasificar terrenos agrícolas buscando patrones y similitudes con muestras históricas de laboratorio.") 
 url = "https://knnconsuelosagrosavia-shtkfth74t9y8ee5bppcyq.streamlit.app/"
 st.write(f"Enlacce app: [Enlace]({url})")
 
 st.subheader("Predictor de sensación térmica")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace podemos observar un aplicativo con datos reales de temperatura y humedad tomados por un sensor IoT, usados para entrenar un modelo de regresión lineal que predice la sensación térmica..") 
 url = "https://predictorsensaciontermica-ua8hhhrw8d3vg4z3ujtsfr.streamlit.app/"
 st.write(f"Enlace app: [Enlace]({url})")


