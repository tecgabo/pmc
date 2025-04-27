# Importações necessárias
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import datetime

# Configuração da página
st.set_page_config(
    page_title="Project Model Canvas - TecVitória",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cores e estilos da TecVitória (baseado no site)
PRIMARY_COLOR = "#003366"  # Azul marinho
SECONDARY_COLOR = "#FF6600"  # Laranja
ACCENT_COLOR = "#00CCCC"  # Azul claro
BACKGROUND_COLOR = "#F5F5F5"
TEXT_COLOR = "#333333"
FONT = "Arial"

# CSS personalizado com estilo TecVitória
st.markdown(f"""
<style>
    /* Estilos gerais */
    body {{
        background-color: {BACKGROUND_COLOR};
        color: {TEXT_COLOR};
        font-family: {FONT}, sans-serif;
    }}
</style>
""", unsafe_allow_html=True)

# Cabeçalho personalizado no estilo TecVitória
st.markdown(f"""
<div class="header">
    <h1>Project Model Canvas</h1>
    <p>Siga o modelo da TecVitória para estruturar seu projeto</p>
</div>
""", unsafe_allow_html=True)

# Função para gerar o canvas
def generate_canvas(data):
    """Gera a imagem do canvas com as informações fornecidas"""
    img = Image.new('RGB', (1754, 1240), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    try:
        font_text = ImageFont.truetype("arial.ttf", 20)
    except:
        font_text = ImageFont.load_default()
    d.text((50, 50), "Project Model Canvas - TecVitória", font=font_text, fill="black")
    return img

# Dicas detalhadas para cada campo
field_hints = {
    'justificativas': "Preencha justificativas...",
    'pitch': "Apresente o resumo do projeto...",
    'produto': "Descreva o que será entregue...",
    'stakeholders': "Liste as partes interessadas...",
    'premissas': "Defina as suposições base...",
    'riscos': "Identifique os riscos...",
    'objetivos': "Estabeleça objetivos SMART...",
    'requisitos': "Liste os requisitos...",
    'equipe': "Indique a equipe responsável...",
    'entregas': "Defina as entregas do projeto...",
    'cronograma': "Apresente o cronograma...",
    'beneficios': "Liste os benefícios esperados...",
    'restricoes': "Identifique as restrições...",
    'custos': "Apresente os custos detalhados..."
}

# Templates pré-definidos
templates = {
    "Selecione um template": {k: "" for k in field_hints},
    "Projeto de Inovação": {
        'justificativas': "• Mercado em transformação digital\n• Concorrência lançou novo produto",
        'pitch': "Desenvolvimento de plataforma integrada de gestão para PMEs.",
        'produto': "• Plataforma SaaS modular\n• Integração com bancos e marketplaces",
        'stakeholders': "• Diretoria Executiva\n• Líderes de departamento",
        'premissas': "• Equipe permanecerá alocada\n• Orçamento aprovado",
        'riscos': "• Atraso na aprovação [Prob: Média] [Impacto: Alto]",
        'objetivos': "• Lançar MVP até 30/09/2024",
        'requisitos': "[MUST] Integração com bancos\n[MUST] Segurança de dados",
        'equipe': "• GP: Ana Silva\n• Tech Lead: Carlos Souza",
        'entregas': "1. Especificação técnica\n2. Módulo financeiro",
        'cronograma': "• F1 (M1-2): Especificação\n• F2 (M3-5): Desenvolvimento",
        'beneficios': "• Redução de 30% em processos manuais",
        'restricoes': "• Orçamento: R$ 1.8M\n• Prazo: 7 meses",
        'custos': "• Desenvolvimento: R$ 1.2M\n• Infra: R$ 300k"
    }
}

# Sidebar com informações básicas
with st.sidebar:
    st.image("https://tecvitoria.com.br/wp-content/uploads/2022/03/logo-tecvitoria-horizontal.png", width=200)
    st.markdown("### Informações do Projeto")
    nome_projeto = st.text_input("Nome do Projeto", placeholder="Digite o nome do projeto")
    responsavel = st.text_input("Responsável", placeholder="Nome do gerente de projeto")
    data = st.date_input("Data", datetime.date.today())
    st.markdown("---")
    st.markdown("### Templates")
    selected_template = st.selectbox("Selecione um template:", list(templates.keys()))
    if selected_template != "Selecione um template":
        st.button("Carregar Template")

# Formulário principal
tab1, tab2 = st.tabs(["📝 Formulário", "🖼️ Visualizar Canvas"])
with tab1:
    st.markdown("## Preencha os campos do Project Model Canvas")
    justificativas = st.text_area("Justificativas", height=100)
    pitch = st.text_area("Pitch", height=100)

with tab2:
    st.markdown("### Visualize o Canvas")
    st.image(generate_canvas({'justificativas': justificativas, 'pitch': pitch}), caption="Preview do Canvas")

# Rodapé
st.markdown("---")
st.markdown("<p style='text-align:center;'>© 2025 TecVitória - Todos os direitos reservados.</p>", unsafe_allow_html=True)
