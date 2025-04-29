# Project Model Canvas - Versão 2
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import datetime
import io

# Configuração inicial da página
st.set_page_config(
    page_title="Project Model Canvas - Versão 2",
    page_icon="📓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos
PRIMARY_COLOR = "#003366"
SECONDARY_COLOR = "#FF6600"
ACCENT_COLOR = "#00CCCC"
BACKGROUND_COLOR = "#F5F5F5"

# Sidebar - Navegação
st.sidebar.title("Menu")
menu = st.sidebar.radio(
    "Navegue pelo app:",
    ("🏠 Início", "📝 Criar Canvas", "📦 Templates e Exemplos", "🛠️ Módulo Avançado", "📥 Exportações")
)

# Página Inicial
if menu == "🏠 Início":
    st.title("📓 Project Model Canvas - Versão 2")
    st.subheader("Bem-vindo!")
    st.markdown("""
    ### O que você encontrará aqui:
    - Aprenda o que é o **Project Model Canvas** baseado na obra de José Finocchio Jr.
    - Estruture projetos de maneira visual, prática e estratégica.
    - Acesse templates e exemplos reais.
    - Construa seu projeto completo, desde o Canvas até a EAP, cronograma e plano de comunicação.
    - Prepare seu projeto para ser avaliado e valorizado!
    """)
    st.info("Use o menu à esquerda para começar a criar seu projeto! 🚀")
