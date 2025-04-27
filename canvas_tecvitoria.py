# Importações necessárias
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import datetime
import textwrap

# Configuração da página
st.set_page_config(
    page_title="Project Model Canvas - TecVitória",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cores e estilos
PRIMARY_COLOR = "#003366"
SECONDARY_COLOR = "#FF6600"  # Cor do novo logo amarelo
ACCENT_COLOR = "#00CCCC"
BACKGROUND_COLOR = "#F5F5F5"

# URL do novo logo da TecVitória (amarelo)
TECVITORIA_LOGO = "https://tecvitoria.com.br/wp-content/uploads/2025/04/logo-amarelo.webp"

# Templates atualizados
TEMPLATES = {
    "Selecione um template": {k: "" for k in [
        'justificativas', 'pitch', 'produto', 'stakeholders', 'premissas', 'riscos', 
        'objetivos', 'requisitos', 'equipe', 'entregas', 'cronograma', 'beneficios', 
        'restricoes', 'custos', 'observacoes']},
    
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
        'custos': "• Desenvolvimento: R$ 1.2M\n• Infra: R$ 300k",
        'observacoes': ""
    }
}

# CSS personalizado
st.markdown(f"""
<style>
    .stApp {{
        background-color: {BACKGROUND_COLOR};
    }}
    .header {{
        background: linear-gradient(135deg, {PRIMARY_COLOR}, {ACCENT_COLOR});
        color: white;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }}
    .sidebar-logo {{
        margin-bottom: 1.5rem;
        text-align: center;
    }}
    .required-field::after {{
        content: " *";
        color: red;
    }}
</style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown(f"""
<div class="header">
    <h1>Project Model Canvas</h1>
    <p>Estruture seu projeto com o modelo da TecVitória</p>
</div>
""", unsafe_allow_html=True)

# Função para gerar o canvas
def generate_canvas(data):
    img = Image.new('RGB', (1754, 1240), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()
    
    d.text((50, 50), f"Project Model Canvas - {data.get('nome_projeto', '')}", font=font, fill=PRIMARY_COLOR)
    return img

# Inicializar session_state
if 'dados' not in st.session_state:
    st.session_state.dados = {
        'nome_projeto': '',
        'responsavel': '',
        'data': datetime.date.today().strftime("%d/%m/%Y"),
        'justificativas': '',
        'pitch': '',
        'produto': '',
        'stakeholders': '',
        'premissas': '',
        'riscos': '',
        'objetivos': '',
        'requisitos': '',
        'equipe': '',
        'entregas': '',
        'cronograma': '',
        'beneficios': '',
        'restricoes': '',
        'custos': '',
        'observacoes': ''
    }

# Sidebar atualizado com novo logo
with st.sidebar:
    # Novo logo da TecVitória (amarelo)
    st.markdown(f"""
    <div class="sidebar-logo">
        <img src="{TECVITORIA_LOGO}" width="200" alt="TecVitória">
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Informações Básicas")
    
    # Campos obrigatórios com indicação visual
    st.markdown('<label class="required-field">Nome do Projeto</label>', unsafe_allow_html=True)
    st.session_state.dados['nome_projeto'] = st.text_input(
        "nome_projeto_input",
        value=st.session_state.dados['nome_projeto'],
        label_visibility="collapsed"
    )
    
    st.markdown('<label class="required-field">Responsável</label>', unsafe_allow_html=True)
    st.session_state.dados['responsavel'] = st.text_input(
        "responsavel_input",
        value=st.session_state.dados['responsavel'],
        label_visibility="collapsed"
    )
    
    st.markdown('<label class="required-field">Data</label>', unsafe_allow_html=True)
    data_input = st.date_input(
        "data_input",
        value=datetime.datetime.strptime(st.session_state.dados['data'], "%d/%m/%Y").date(),
        label_visibility="collapsed"
    )
    st.session_state.dados['data'] = data_input.strftime("%d/%m/%Y")
    
    st.markdown("---")
    st.markdown("### Templates")
    
    selected_template = st.selectbox(
        "Carregar template:",
        options=list(TEMPLATES.keys()),
        index=0,
        label_visibility="visible"
    )
    
    if st.button("Aplicar Template") and selected_template != "Selecione um template":
        st.session_state.dados.update(TEMPLATES[selected_template])
        st.success(f"Template '{selected_template}' carregado com sucesso!")
    
    if st.button("Limpar Formulário"):
        for key in st.session_state.dados:
            st.session_state.dados[key] = ""
        st.session_state.dados['data'] = datetime.date.today().strftime("%d/%m/%Y")
        st.rerun()

# Formulário principal
tab1, tab2 = st.tabs(["📝 Formulário", "🖼️ Visualizar Canvas"])

with tab1:
    cols = st.columns(2)
    
    with cols[0]:
        st.session_state.dados['justificativas'] = st.text_area(
            "Justificativas",
            value=st.session_state.dados['justificativas'],
            height=150
        )
        
        st.session_state.dados['pitch'] = st.text_area(
            "Pitch",
            value=st.session_state.dados['pitch'],
            height=100
        )
        
        st.session_state.dados['objetivos'] = st.text_area(
            "Objetivos",
            value=st.session_state.dados['objetivos'],
            height=150
        )
        
        st.session_state.dados['produto'] = st.text_area(
            "Produto/Serviço",
            value=st.session_state.dados['produto'],
            height=150
        )
    
    with cols[1]:
        st.session_state.dados['stakeholders'] = st.text_area(
            "Stakeholders",
            value=st.session_state.dados['stakeholders'],
            height=120
        )
        
        st.session_state.dados['requisitos'] = st.text_area(
            "Requisitos",
            value=st.session_state.dados['requisitos'],
            height=120
        )
        
        st.session_state.dados['entregas'] = st.text_area(
            "Entregas",
            value=st.session_state.dados['entregas'],
            height=120
        )
        
        st.session_state.dados['cronograma'] = st.text_area(
            "Cronograma",
            value=st.session_state.dados['cronograma'],
            height=120
        )
    
    st.session_state.dados['premissas'] = st.text_area(
        "Premissas",
        value=st.session_state.dados['premissas'],
        height=100
    )
    
    st.session_state.dados['riscos'] = st.text_area(
        "Riscos",
        value=st.session_state.dados['riscos'],
        height=100
    )
    
    st.session_state.dados['restricoes'] = st.text_area(
        "Restrições",
        value=st.session_state.dados['restricoes'],
        height=100
    )
    
    st.session_state.dados['equipe'] = st.text_area(
        "Equipe",
        value=st.session_state.dados['equipe'],
        height=100
    )
    
    st.session_state.dados['beneficios'] = st.text_area(
        "Benefícios",
        value=st.session_state.dados['beneficios'],
        height=100
    )
    
    st.session_state.dados['custos'] = st.text_area(
        "Custos",
        value=st.session_state.dados['custos'],
        height=100
    )
    
    st.session_state.dados['observacoes'] = st.text_area(
        "Observações",
        value=st.session_state.dados['observacoes'],
        height=100
    )

with tab2:
    if st.session_state.dados['nome_projeto']:
        st.image(
            generate_canvas(st.session_state.dados), 
            caption=f"Canvas para {st.session_state.dados['nome_projeto']}"
        )
    else:
        st.warning("Preencha o nome do projeto para visualizar o canvas.")

# Rodapé
st.markdown("---")
st.markdown("<p style='text-align:center;'>© 2024 TecVitória</p>", unsafe_allow_html=True)
