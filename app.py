# Importações
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import datetime
import io

# Configuração da página
st.set_page_config(
    page_title="Project Model Canvas - TecVitória",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cores e estilos
PRIMARY_COLOR = "#003366"
SECONDARY_COLOR = "#FF6600"
ACCENT_COLOR = "#00CCCC"
BACKGROUND_COLOR = "#F5F5F5"
TEXT_COLOR = "#333333"

# Logo da TecVitória
TECVITORIA_LOGO = "https://tecvitoria.com.br/wp-content/uploads/2025/04/logo-amarelo.webp"

# Templates
TEMPLATES = {
    "Selecione um template": {k: "" for k in [
        'justificativas', 'pitch', 'produto', 'stakeholders', 'premissas', 'riscos',
        'objetivos', 'requisitos', 'equipe', 'entregas', 'cronograma', 'beneficios',
        'restricoes', 'custos', 'observacoes']},
    
    "Projeto de Inovação": {
        'justificativas': "Mercado em transformação digital",
        'pitch': "Desenvolvimento de plataforma para PMEs.",
        'produto': "Plataforma SaaS modular",
        'stakeholders': "Diretoria, Departamentos",
        'premissas': "Equipe alocada, Orçamento aprovado",
        'riscos': "Atraso na aprovação",
        'objetivos': "Lançar MVP até 30/09/2024",
        'requisitos': "Integração bancária, Segurança de dados",
        'equipe': "GP: Ana Silva, Tech: Carlos Souza",
        'entregas': "Especificação e Módulo financeiro",
        'cronograma': "Especificação e Desenvolvimento",
        'beneficios': "Redução de 30% de processos",
        'restricoes': "Orçamento: R$ 1.8M",
        'custos': "Desenvolvimento: R$ 1.2M",
        'observacoes': ""
    }
}

# Função para gerar Canvas visual
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

    # Título principal
    draw.text((canvas_width // 2 - 300, 20), f"Project Model Canvas - {data.get('nome_projeto', '')}", font=font, fill=(0, 51, 102))

    for title, box in sections:
        draw.rectangle(box, outline=(0, 0, 0), fill=(240, 240, 240), width=2)
        text_x = box[0] + 10
        text_y = box[1] + 10
        conteudo = data.get(title.lower(), title)
        draw.text((text_x, text_y), f"{title}", font=font, fill=(0, 51, 102))

    return img

# Inicialização do estado
if 'dados' not in st.session_state:
    st.session_state.dados = {
        'nome_projeto': '',
        'responsavel': '',
        'data': datetime.date.today().strftime("%d/%m/%Y"),
        'justificativas': '', 'pitch': '', 'produto': '', 'stakeholders': '',
        'premissas': '', 'riscos': '', 'objetivos': '', 'requisitos': '',
        'equipe': '', 'entregas': '', 'cronograma': '', 'beneficios': '',
        'restricoes': '', 'custos': '', 'observacoes': ''
    }

# Sidebar
with st.sidebar:
    st.image(TECVITORIA_LOGO, width=200)
    st.title("Informações do Projeto")
    
    st.session_state.dados['nome_projeto'] = st.text_input("Nome do Projeto*", value=st.session_state.dados['nome_projeto'])
    st.session_state.dados['responsavel'] = st.text_input("Responsável*", value=st.session_state.dados['responsavel'])
    data_input = st.date_input("Data*", value=datetime.datetime.strptime(st.session_state.dados['data'], "%d/%m/%Y").date())
    st.session_state.dados['data'] = data_input.strftime("%d/%m/%Y")

    st.markdown("---")
    st.subheader("Templates")
    template_select = st.selectbox("Escolher Template", list(TEMPLATES.keys()))
    
    if st.button("Aplicar Template") and template_select != "Selecione um template":
        st.session_state.dados.update(TEMPLATES[template_select])

# Corpo principal
st.title("Project Model Canvas")

# Formulário
with st.form("formulario"):
    col1, col2 = st.columns(2)

    with col1:
        for campo in ['justificativas', 'pitch', 'objetivos', 'produto', 'premissas', 'riscos', 'restricoes']:
            st.session_state.dados[campo] = st.text_area(campo.capitalize(), value=st.session_state.dados[campo])

    with col2:
        for campo in ['stakeholders', 'requisitos', 'entregas', 'cronograma', 'equipe', 'beneficios', 'custos', 'observacoes']:
            st.session_state.dados[campo] = st.text_area(campo.capitalize(), value=st.session_state.dados[campo])

    submitted = st.form_submit_button("Atualizar Canvas")

# Visualizar Canvas
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
    st.warning("Preencha o nome do projeto para gerar o Canvas.")

# Rodapé
st.markdown("---")
st.markdown("<p style='text-align:center;'>© 2024 TecVitória</p>", unsafe_allow_html=True)
