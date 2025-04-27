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

# [...] (O restante das funções e configurações permanecem iguais)

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
        datetime.datetime.strptime(st.session_state.dados['data'], "%d/%m/%Y").date(),
        label_visibility="collapsed"
    )
    st.session_state.dados['data'] = data_input.strftime("%d/%m/%Y")
    
    st.markdown("---")
    st.markdown("### Templates")
    
    selected_template = st.selectbox(
        "Carregar template:",
        list(TEMPLATES.keys()),
        index=0,
        label_visibility="visible"
    )
    
    if st.button("Aplicar Template") and selected_template != "Selecione um template":
        st.session_state.dados.update(TEMPLATES[selected_template])
        st.success(f"Template '{selected_template}' carregado com sucesso!")
    
    if st.button("Limpar Formulário"):
        st.session_state.dados = {k: "" for k in st.session_state.dados.keys()}
        st.session_state.dados.update({
            'nome_projeto': '',
            'responsavel': '',
            'data': datetime.date.today().strftime("%d/%m/%Y")
        })
        st.rerun()

# [...] (O restante do código permanece igual)
