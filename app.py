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
    ### Sobre o Project Model Canvas
    O Project Model Canvas é uma ferramenta visual para estruturar projetos de forma prática e colaborativa.
    
    Baseado na obra de José Finocchio Jr., ele permite:
    - Organizar ideias iniciais de um projeto.
    - Visualizar conexões entre entregas, riscos, custos e benefícios.
    - Acelerar o entendimento de escopo, prazos e valor.
    
    ### Como navegar:
    Use o menu lateral para criar seu Canvas, explorar templates, visualizar exemplos e desenvolver seu projeto até uma estrutura profissional!
    """)
    st.info("Comece seu projeto com organização e propósito! 🚀")

# Placeholder para Criar Canvas
elif menu == "📝 Criar Canvas":
    st.title("📝 Criar seu Project Model Canvas")
    st.warning("Formulário de criação interativa do Canvas - Em construção.")

# Placeholder para Templates e Exemplos
elif menu == "📦 Templates e Exemplos":
    st.title("📦 Templates e Exemplos Reais")
    st.warning("Área de templates prontos para prática - Em construção.")

# Placeholder para Módulo Avançado
elif menu == "🛠️ Módulo Avançado":
    st.title("🛠️ Planejamento Avançado")
    st.warning("Geração de EAP, cronogramas e planos - Em construção.")

# Placeholder para Exportações
elif menu == "📥 Exportações":
    st.title("📥 Exportação de Documentos")
    st.warning("Download de Canvas e documentos auxiliares - Em construção.")
