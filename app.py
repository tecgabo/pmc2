# Código do app
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import datetime
import io

st.set_page_config(
    page_title="Project Model Canvas - Aprenda e Pratique",
    page_icon="📓",
    layout="wide"
)

PRIMARY_COLOR = "#003366"
BACKGROUND_COLOR = "#F5F5F5"
TEXT_COLOR = "#333333"

def generate_canvas_image(data):
    canvas_width = 1754
    canvas_height = 1240
    img = Image.new('RGB', (canvas_width, canvas_height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()

    sections = [
        ("Justificativas", (50, 100, 850, 250)),
        ("Pitch", (900, 100, 1700, 250)),
        ("Produto/Serviço", (50, 300, 850, 450)),
        ("Stakeholders", (900, 300, 1700, 450)),
        ("Premissas", (50, 500, 850, 600)),
        ("Riscos", (900, 500, 1700, 600)),
        ("Objetivos", (50, 650, 850, 750)),
        ("Requisitos", (900, 650, 1700, 750)),
        ("Equipe", (50, 800, 850, 900)),
        ("Entregas", (900, 800, 1700, 900)),
        ("Cronograma", (50, 950, 850, 1050)),
        ("Benefícios", (900, 950, 1700, 1050)),
        ("Restrições", (50, 1100, 850, 1200)),
        ("Custos", (900, 1100, 1700, 1200)),
        ("Observações", (50, 1210, 1700, 1230))
    ]

    draw.text((canvas_width // 2 - 300, 20), f"Project Model Canvas - {data.get('nome_projeto', '')}", font=font, fill=(0, 51, 102))

    for title, box in sections:
        draw.rectangle(box, outline=(0, 0, 0), fill=(240, 240, 240), width=2)
        draw.text((box[0] + 10, box[1] + 10), title, font=font, fill=(0, 51, 102))

    return img

if 'dados' not in st.session_state:
    st.session_state.dados = {campo: '' for campo in [
        'nome_projeto', 'responsavel', 'data',
        'justificativas', 'pitch', 'produto', 'stakeholders', 'premissas', 'riscos',
        'objetivos', 'requisitos', 'equipe', 'entregas', 'cronograma', 'beneficios',
        'restricoes', 'custos', 'observacoes']}
    st.session_state.dados['data'] = datetime.date.today().strftime("%d/%m/%Y")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["📚 Aprenda", "📄 Templates", "📦 Casos Reais", "🔄 Canvas Interativo", "🧠 Módulo Avançado"])

with tab1:
    st.header("Fundamentos do Project Model Canvas")
    st.markdown("""
    O **Project Model Canvas** é uma ferramenta visual para o planejamento de projetos com base em perguntas fundamentais.
    """)

with tab2:
    st.header("Templates para Preenchimento")
    st.info("Templates serão disponibilizados para download.")

with tab3:
    st.header("Exemplos Reais de Aplicação")
    st.image("cases/crm_case.png", caption="Case Business CRM")
    st.image("cases/nemo_case.png", caption="Case Procurando Nemo")
    st.image("cases/legal_case.png", caption="Case Serviços Jurídicos")

with tab4:
    st.header("Crie seu Canvas")
    with st.form("formulario"):
        st.session_state.dados['nome_projeto'] = st.text_input("Nome do Projeto*", value=st.session_state.dados['nome_projeto'])
        st.session_state.dados['responsavel'] = st.text_input("Responsável*", value=st.session_state.dados['responsavel'])
        st.session_state.dados['data'] = st.date_input("Data", datetime.datetime.strptime(st.session_state.dados['data'], "%d/%m/%Y")).strftime("%d/%m/%Y")

        col1, col2 = st.columns(2)
        with col1:
            for campo in ['justificativas', 'pitch', 'objetivos', 'produto', 'premissas', 'riscos', 'restricoes']:
                st.session_state.dados[campo] = st.text_area(campo.capitalize(), value=st.session_state.dados[campo])
        with col2:
            for campo in ['stakeholders', 'requisitos', 'entregas', 'cronograma', 'equipe', 'beneficios', 'custos', 'observacoes']:
                st.session_state.dados[campo] = st.text_area(campo.capitalize(), value=st.session_state.dados[campo])

        submitted = st.form_submit_button("Gerar Canvas")

    if st.session_state.dados['nome_projeto']:
        canvas_img = generate_canvas_image(st.session_state.dados)
        buf = io.BytesIO()
        canvas_img.save(buf, format="PNG")
        st.image(canvas_img, caption="Visualização do Canvas", use_column_width=True)
        st.download_button(
            label="💾 Baixar Canvas como PNG",
            data=buf.getvalue(),
            file_name=f"canvas_{st.session_state.dados['nome_projeto'].replace(' ', '_')}.png",
            mime="image/png"
        )
    else:
        st.warning("Preencha o nome do projeto para visualizar o Canvas.")

with tab5:
    st.header("Módulo Avançado: Estruturação Detalhada")
    st.info("Conteúdo complementar avançado será disponibilizado.")

st.markdown("---")
st.markdown("<p style='text-align:center;'>© 2024 Projeto Canvas - Educação e Inovação</p>", unsafe_allow_html=True)
