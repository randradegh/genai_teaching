import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(
    page_title="GenAI Edu - Revoluciona tu Enseñanza", 
    page_icon="🧠", 
    layout="wide", 
    initial_sidebar_state="auto"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        color: #E6E6E6;
        background-color: #0431B4;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        color: #F6E3CE;    
        height: 50px;
        white-space: pre-wrap;
        background-color: #4682B4;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-right: 5px;
        padding-left: 5px;
        padding-bottom: 10px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #1E90FF;
    }
    h1, h2, h3, h4 {
        color: #E6E6E6;
    }
    .highlight {
        color: #0B3861;
        background-color: #FACC2E;
        padding: 0.2em 0.5em;
        border-radius: 0.3em;
    }
</style>
""", unsafe_allow_html=True)

# Header
col1, col2 = st.columns([3, 1])
with col1:
    st.title("🚀 Revoluciona tu Enseñanza con Inteligencia Artificial Generativa")
    st.subheader("Curso intensivo para docentes visionarios")
with col2:
    # lottie_url = "https://assets5.lottiefiles.com/packages/lf20_SI8fvW.json"
    
    # lottie_json = load_lottieurl(lottie_url)
    # if lottie_json:
    #     st_lottie(lottie_json, height=150)
    st.image('profesor.jpeg')

tab1, tab2, tab3, tab4 = st.tabs(["🌟 Descubre", "📚 Programa", "🗓️ Detalles", "✍️ Inscripción"])

with tab1:
    st.header("🎯 Descubre el Futuro de la Educación")
    
    st.markdown("""
    ### ¿Estás listo para transformar tu enseñanza?

    En la era digital, la Inteligencia :orange[**Artificial Generativa (GenIA)**] no es solo una herramienta, es una revolución educativa. 
    Este curso te posicionará a la vanguardia de esta transformación.

    ### ¿Por qué este curso es tu mejor inversión?

    - 🚀 **Innovación Instantánea**: Implementa lo aprendido inmediatamente en tus clases.
    - 🎨 **Creatividad Amplificada**: Crea contenido educativo que cautive a tus estudiantes.
    - 🧠 **Aprendizaje Personalizado**: Adapta tu enseñanza a cada estudiante con el poder de la IA.
    - 🌐 **Networking Poderoso**: Conéctate con educadores visionarios como tú.

    ### Modalidad Flexible

    Aprende desde donde estés con nuestras sesiones virtuales vía Google Meet. 
    La educación del futuro está a un clic de distancia.

    ### No te quedes atrás

    <div class="highlight">La IA está redefiniendo la educación AHORA. Sé parte del cambio o quédate observando. La elección es tuya.</div>
    """, unsafe_allow_html=True)

with tab2:
    st.header("📚 Programa del Curso")
    """
    En este curso, aprenderás a integrar las herramientas de IA Generativa en tu práctica docente, llevando tus clases al siguiente nivel y preparando a tus estudiantes para los desafíos del siglo XXI.

    - Conoce los conceptos básicos de la tecnología de los grandes modelos de lenguaje (LLMs) y la manera de aprovecharlos para la educación.
    - Descubre cómo la IA puede revolucionar la creación de contenido educativo, desde guías de estudio hasta exámenes de varios tipos.
    - Aprende a utilizar la IA Generativa  para personalizar el aprendizaje, automatizar evaluaciones y desarrollar proyectos prácticos que fomenten el pensamiento crítico y la resolución de problemas.
    - Crea, de manera automática y en muy poco tiempo, experiencias de aprendizaje personalizadas utilizando ChatGPT y otros modelos de inteligencia artificial generativa.
    - Reflexiona sobre las implicaciones éticas de la IA en la educación, asegurando un uso responsable y equitativo de estas tecnologías.

    ### :blue_book: ¿Por qué este curso es para ti?

    Porque la educación del futuro necesita docentes preparados para aprovechar las herramientas tecnológicas que están transformando el mundo. Este curso te dará las habilidades necesarias para innovar en tu enseñanza y maximizar el potencial de tus estudiantes.

    No pierdas esta oportunidad! Inscríbete y sé parte del cambio en la educación. 
    
    Juntos, podemos hacer que el aprendizaje sea más dinámico, accesible y efectivo.

    ### :compass: Programa del curso

    1. Fundamentos de la IA Generativa:

        1. **Introducción a la IA Generativa y su aplicación en la educación**: Conoce cómo la IA puede revolucionar el aula, facilitando la creación de contenido personalizado y adaptado a las necesidades de cada estudiante.

        2. **Herramientas de IA Generativa**: Descubre las herramientas más avanzadas como ChatGPT y Claude, y aprende a utilizarlas para crear recursos didácticos innovadores.

        3. **Creación de Recursos Didácticos con IA Generativa**: Aprende a diseñar materiales educativos que capten la atención de tus estudiantes y faciliten el aprendizaje
    
    2. Implementación Práctica en la Enseñanza:

        1. **Evaluación con IA Generativa**: Optimiza tus evaluaciones y conoce cómo la IA puede ayudarte a medir el progreso de tus estudiantes de manera más precisa.

        2. **Integración en la Planificación de Lecciones**: Descubre cómo integrar la IA en tu planificación diaria para atender mejor la diversidad en el aula.

        3. **Proyectos Prácticos y Desarrollo de Competencias**: Aplica lo aprendido en proyectos concretos que mejoren tus habilidades y las de tus estudiantes.


    ### :calendar: Inscríbete ahora y lleva tu enseñanza al siguiente nivel.
"""
with tab3:
    st.header("🗓️ Detalles del Curso")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📅 Fechas y Horarios
        - **Inicio**: 16 de septiembre de 2024
        - **Fin**: 20 de septiembre de 2024
        - **Horario**: 17:00 - 20:00 hrs
        
        ### ⏳ Duración Total
        15 horas de pura transformación educativa
        
        ### 💻 Modalidad
        100% virtual vía Google Meet
        """)
    
    with col2:
        st.markdown("""
        ### 💰 Inversión en tu Futuro
        - **Precio**: $1,500 MXN 
        - **(+IVA si requiere factura)**
                       
        <div class="highlight">¡Plazas limitadas! Asegura tu lugar en la revolución educativa.</div>
        """, unsafe_allow_html=True)

with tab4:
    st.header("✍️ Inscripción")
    
    st.markdown("""
    ### 🚀 ¡Únete a la Élite Educativa!
    
    Para asegurar tu lugar, sigue estos sencillos pasos:
    
    1. **Envía tus datos** a randradedev@gmail.com:
       - Nombre completo
       - Grado máximo de estudios
       - Nivel en el que ejerces la docencia
       - Teléfono (opcional)
       - Correo electrónico
       - Ciudad y país de residencia
       - Experiencia con IA generativa
    
    2. **Realiza tu pago**:
       - Monto: $1,500 MXN
       - Cuenta: Roberto Andrade Fonseca
       - Banco: Banorte
       - Número de cuenta: 0015014967
       - CLABE: 072 180 00015014967 5
    
    3. **Confirma tu pago**:
       Envía el comprobante a randradedev@gmail.com con el asunto:
       "[Tu Nombre] - Pago del curso de GenAI en educación"
    
    <div class="highlight">¡Tu viaje hacia la educación del futuro comienza aquí!</div>
    
    ¿Preguntas? Estamos aquí para ayudarte: randradedev@gmail.com
    """, unsafe_allow_html=True)

st.markdown("""
---
#### #EducaciónDelFuturo #IAenEducación #InnovaciónDocente #AprendizajePersonalizado #TransformaciónDigital
""")
