# Project Model Canvas - PRO Edition - Atualizado
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import datetime
import io

# Configuração da página
st.set_page_config(
    page_title="Project Model Canvas - PRO Edition",
    page_icon="📓",
    layout="wide",
    initial_sidebar_state="expanded"
)

PRIMARY_COLOR = "#003366"
SECONDARY_COLOR = "#FF6600"
ACCENT_COLOR = "#00CCCC"
BACKGROUND_COLOR = "#F5F5F5"

# Templates
TEMPLATES = {
    "Canvas em Branco": {campo: "" for campo in [
        'justificativas', 'pitch', 'produto', 'stakeholders', 'premissas', 'riscos',
        'objetivos', 'requisitos', 'equipe', 'entregas', 'cronograma', 'beneficios',
        'restricoes', 'custos', 'observacoes']},
    "CRM de Vendas B2B": {
        'justificativas': "Necessidade de automatizar o funil de vendas.",
        'pitch': "Sistema CRM para vendas B2B integrado ao ERP.",
        'produto': "Plataforma SaaS de CRM para vendas complexas.",
        'stakeholders': "Diretores Comerciais, Equipe de Vendas, TI",
        'premissas': "Infraestrutura existente será aproveitada.",
        'riscos': "Resistência da equipe, integração falha com ERP.",
        'objetivos': "Reduzir ciclo de vendas em 20% até dezembro.",
        'requisitos': "Login unificado, Relatórios analíticos.",
        'equipe': "PM, Devs, UX Designer, Analista Comercial",
        'entregas': "MVP do CRM em 3 meses.",
        'cronograma': "Fase 1: Especificação (1 mês), Fase 2: Dev (2 meses).",
        'beneficios': "Aumento de receita e previsibilidade de vendas.",
        'restricoes': "Orçamento máximo de R$ 300k.",
        'custos': "Desenvolvimento e Licenciamento SaaS.",
        'observacoes': "Possível expansão para CRM Mobile."
    },
    "Projeto Procurando Nemo": {
        'justificativas': "Criar experiência imersiva para crianças.",
        'pitch': "Projeto lúdico baseado no filme 'Procurando Nemo'.",
        'produto': "Espaço de realidade aumentada para crianças.",
        'stakeholders': "Pais, Escolas, Crianças, Empresas de tecnologia.",
        'premissas': "Autorização de direitos de imagem obtida.",
        'riscos': "Baixa adoção tecnológica em público infantil.",
        'objetivos': "Atingir 10.000 visitantes no primeiro ano.",
        'requisitos': "Ambiente seguro, interação intuitiva.",
        'equipe': "Gerente de Projeto, Equipe de TI, Educadores.",
        'entregas': "Espaço interativo pronto em 6 meses.",
        'cronograma': "Fase 1: Design (2 meses), Fase 2: Execução (4 meses).",
        'beneficios': "Educação lúdica e aumento do turismo.",
        'restricoes': "Espaço máximo de 500m².",
        'custos': "Instalação de equipamentos tecnológicos.",
        'observacoes': "Parceria com Disney prevista."
    }
}

# Funções auxiliares
def calcular_progresso(dados):
    total_campos = len(dados) - 3
    preenchidos = sum(1 for k, v in dados.items() if v and k not in ['nome_projeto', 'responsavel', 'data'])
    return int((preenchidos / total_campos) * 100)

# Sidebar
st.sidebar.title("Menu")
menu = st.sidebar.radio(
    "Navegue pelo aplicativo:",
    ("Início", "Criar Plano de Projeto", "Templates e Exemplos", "Planejamento Avançado", "Exportar")
)

# Inicializar dados se não existir
if 'dados' not in st.session_state:
    st.session_state.dados = {campo: '' for campo in [
        'nome_projeto', 'responsavel', 'data',
        'justificativas', 'pitch', 'produto', 'stakeholders', 'premissas', 'riscos',
        'objetivos', 'requisitos', 'equipe', 'entregas', 'cronograma', 'beneficios',
        'restricoes', 'custos', 'observacoes']}
    st.session_state.dados['data'] = datetime.date.today().strftime("%d/%m/%Y")

# Conteúdo das páginas
if menu == "Início":
    st.title("Project Model Canvas - PRO Edition")
    st.markdown("Ferramenta de apoio ao desenvolvimento de projetos baseada no método de José Finocchio Jr.")

elif menu == "Criar Plano de Projeto":
    st.title("Criar seu Plano de Projeto")
    st.session_state.dados['nome_projeto'] = st.text_input("Nome do Projeto*", value=st.session_state.dados['nome_projeto'])
    st.session_state.dados['responsavel'] = st.text_input("Responsável*", value=st.session_state.dados['responsavel'])
    st.session_state.dados['data'] = st.date_input("Data", datetime.datetime.strptime(st.session_state.dados['data'], "%d/%m/%Y")).strftime("%d/%m/%Y")

    col1, col2 = st.columns(2)
    with col1:
        st.session_state.dados['justificativas'] = st.text_area("Justificativas", value=st.session_state.dados['justificativas'])
        st.session_state.dados['pitch'] = st.text_area("Pitch", value=st.session_state.dados['pitch'])
        st.session_state.dados['objetivos'] = st.text_area("Objetivos", value=st.session_state.dados['objetivos'])
        st.session_state.dados['produto'] = st.text_area("Produto/Serviço", value=st.session_state.dados['produto'])
    with col2:
        st.session_state.dados['stakeholders'] = st.text_area("Stakeholders", value=st.session_state.dados['stakeholders'])
        st.session_state.dados['requisitos'] = st.text_area("Requisitos", value=st.session_state.dados['requisitos'])
        st.session_state.dados['entregas'] = st.text_area("Entregas", value=st.session_state.dados['entregas'])
        st.session_state.dados['cronograma'] = st.text_area("Cronograma", value=st.session_state.dados['cronograma'])

    st.progress(calcular_progresso(st.session_state.dados))
    st.success(f"Progresso: {calcular_progresso(st.session_state.dados)}% completo.")

elif menu == "Templates e Exemplos":
    st.title("Templates e Exemplos")
    template = st.selectbox("Escolha um Template:", list(TEMPLATES.keys()))
    if st.button("Aplicar Template"):
        for campo, valor in TEMPLATES[template].items():
            if campo in st.session_state.dados:
                st.session_state.dados[campo] = valor
        st.success(f"Template '{template}' aplicado!")

elif menu == "Planejamento Avançado":
    st.title("Planejamento Avançado (beta)")
    if st.button("Gerar Estrutura Analítica do Projeto"):
        entregas = st.session_state.dados.get('entregas', '')
        if entregas:
            lista_entregas = entregas.split('\n')
            st.subheader("EAP Gerada:")
            for idx, entrega in enumerate(lista_entregas, 1):
                st.markdown(f"{idx}. {entrega.strip()}")
        else:
            st.warning("Nenhuma entrega preenchida para gerar a EAP.")

elif menu == "Exportar":
    st.title("Exportação")
    st.warning("Funcionalidade de exportação será adicionada em breve.")
