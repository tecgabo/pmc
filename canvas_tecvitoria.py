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

# Cores e estilos da TecVitória
PRIMARY_COLOR = "#003366"  # Azul marinho
SECONDARY_COLOR = "#FF6600"  # Laranja
ACCENT_COLOR = "#00CCCC"  # Azul claro
BACKGROUND_COLOR = "#F5F5F5"
TEXT_COLOR = "#333333"
FONT = "Arial"

# CSS personalizado
st.markdown(f"""
<style>
    /* Estilos gerais */
    .stApp {{
        background-color: {BACKGROUND_COLOR};
    }}
    .header {{
        background: linear-gradient(135deg, {PRIMARY_COLOR}, {ACCENT_COLOR});
        color: white;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }}
    .header h1 {{
        color: white;
        font-weight: 700;
    }}
    .header p {{
        color: white;
        opacity: 0.9;
    }}
    .section {{
        background-color: white;
        border-radius: 8px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        border-left: 4px solid {SECONDARY_COLOR};
    }}
    .section h2 {{
        color: {PRIMARY_COLOR};
        font-size: 1.2rem;
        margin-top: 0;
    }}
    .sidebar .sidebar-content {{
        background-color: {PRIMARY_COLOR};
        color: white;
    }}
    .stButton button {{
        background-color: {SECONDARY_COLOR};
        color: white;
        border: none;
        border-radius: 4px;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }}
    .stButton button:hover {{
        background-color: #E55C00;
        color: white;
    }}
    .stDownloadButton button {{
        background-color: {PRIMARY_COLOR};
        color: white;
    }}
    .footer {{
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        color: {TEXT_COLOR};
        font-size: 0.9rem;
    }}
</style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown(f"""
<div class="header">
    <h1>Project Model Canvas</h1>
    <p>Estruture seu projeto de forma clara e objetiva com o modelo da TecVitória</p>
</div>
""", unsafe_allow_html=True)

# Função para gerar o canvas com layout melhorado
def generate_canvas(data):
    """Gera a imagem do canvas com as informações fornecidas"""
    # Criar imagem base
    img = Image.new('RGB', (2480, 3508), color=(255, 255, 255))  # Tamanho A4 em 300dpi
    d = ImageDraw.Draw(img)
    
    try:
        font_title = ImageFont.truetype("arial.ttf", 36)
        font_section = ImageFont.truetype("arial.ttf", 24)
        font_text = ImageFont.truetype("arial.ttf", 18)
    except:
        font_title = ImageFont.load_default()
        font_section = ImageFont.load_default()
        font_text = ImageFont.load_default()
    
    # Cabeçalho
    d.rectangle([(100, 100), (2380, 200)], fill=PRIMARY_COLOR)
    d.text((150, 150), "PROJECT MODEL CANVAS - TECVITÓRIA", font=font_title, fill="white", anchor="mm")
    
    # Informações do projeto
    d.rectangle([(100, 220), (2380, 300)], fill=ACCENT_COLOR)
    d.text((150, 260), f"Projeto: {data.get('nome_projeto', '')}", font=font_section, fill="white")
    d.text((1000, 260), f"Responsável: {data.get('responsavel', '')}", font=font_section, fill="white")
    d.text((1800, 260), f"Data: {data.get('data', '')}", font=font_section, fill="white")
    
    # Grid do canvas (9 seções)
    sections = [
        {"name": "Justificativas", "pos": (100, 350, 780, 650)},
        {"name": "Pitch", "pos": (800, 350, 1480, 650)},
        {"name": "Produto/Serviço", "pos": (1500, 350, 2380, 650)},
        {"name": "Stakeholders", "pos": (100, 700, 780, 1000)},
        {"name": "Premissas", "pos": (800, 700, 1480, 1000)},
        {"name": "Riscos", "pos": (1500, 700, 2380, 1000)},
        {"name": "Objetivos", "pos": (100, 1050, 780, 1350)},
        {"name": "Requisitos", "pos": (800, 1050, 1480, 1350)},
        {"name": "Equipe", "pos": (1500, 1050, 2380, 1350)},
        {"name": "Entregas", "pos": (100, 1400, 780, 1700)},
        {"name": "Cronograma", "pos": (800, 1400, 1480, 1700)},
        {"name": "Benefícios", "pos": (1500, 1400, 2380, 1700)},
        {"name": "Restrições", "pos": (100, 1750, 780, 2050)},
        {"name": "Custos", "pos": (800, 1750, 1480, 2050)},
        {"name": "Observações", "pos": (1500, 1750, 2380, 2050)}
    ]
    
    for section in sections:
        # Desenhar retângulo da seção
        d.rectangle(section["pos"], outline=PRIMARY_COLOR, width=2)
        
        # Adicionar título da seção
        d.rectangle([(section["pos"][0], section["pos"][1]), 
                    (section["pos"][2], section["pos"][1]+50)], 
                    fill=SECONDARY_COLOR)
        d.text((section["pos"][0]+10, section["pos"][1]+25), 
              section["name"].upper(), font=font_section, fill="white")
        
        # Adicionar conteúdo (com quebra de linha)
        content = data.get(section["name"].lower().replace("/", "").replace(" ", "_"), "")
        if content:
            wrapped_text = textwrap.wrap(content, width=60)
            y_text = section["pos"][1] + 80
            for line in wrapped_text:
                d.text((section["pos"][0]+20, y_text), line, font=font_text, fill=TEXT_COLOR)
                y_text += 30
    
    return img

# Dicas detalhadas para cada campo
field_hints = {
    'justificativas': "Por que este projeto existe? Quais problemas ele resolve? Quais oportunidades ele aproveita?",
    'pitch': "Resuma seu projeto em 1-2 frases impactantes. O que faz, para quem e qual o diferencial?",
    'produto_servico': "O que será entregue? Descreva os principais componentes, funcionalidades e características.",
    'stakeholders': "Quem são as partes interessadas? (clientes, patrocinadores, equipe, reguladores, etc.)",
    'premissas': "Quais suposições estão sendo feitas? O que precisa ser verdade para o projeto ter sucesso?",
    'riscos': "Quais são os principais riscos? Probabilidade e impacto de cada um. Como mitigar?",
    'objetivos': "Quais resultados concretos o projeto deve alcançar? Use critérios SMART.",
    'requisitos': "Quais são as necessidades obrigatórias (MUST) e desejáveis (SHOULD)?",
    'equipe': "Quem são os principais responsáveis? Papéis e responsabilidades.",
    'entregas': "Quais são os principais marcos e entregáveis do projeto?",
    'cronograma': "Principais fases e prazos. Marcos importantes.",
    'beneficios': "Quais benefícios o projeto trará? Para a organização, clientes e stakeholders.",
    'restricoes': "Quais são as limitações? (orçamento, tempo, recursos, regulamentações)",
    'custos': "Principais categorias de custos e estimativas.",
    'observacoes': "Outras informações relevantes que não se encaixam nas outras seções."
}

# Templates pré-definidos
templates = {
    "Selecione um template": {k: "" for k in field_hints},
    "Projeto de Inovação Tecnológica": {
        'justificativas': "• Mercado em transformação digital\n• Concorrência lançou novo produto\n• Demanda de clientes por solução integrada",
        'pitch': "Plataforma SaaS de gestão empresarial integrada para PMEs, com módulos financeiro, comercial e RH em uma única solução.",
        'produto_servico': "• Plataforma modular em nuvem\n• Integração com bancos e marketplaces\n• Painéis de BI em tempo real\n• App mobile para gestores",
        'stakeholders': "• Diretoria Executiva (patrocinador)\n• Líderes de departamento\n• Equipe de TI\n• Clientes pilotos",
        'premissas': "• Equipe permanecerá alocada\n• Orçamento aprovado conforme planejado\n• Parceiros tecnológicos entregarão APIs no prazo",
        'riscos': "1. Atraso na aprovação [Prob: Média] [Impacto: Alto] - Mitigação: Plano B com VC\n2. Mudança regulatória [Prob: Baixa] [Impacto: Crítico]",
        'objetivos': "• Lançar MVP até 30/09/2024\n• 10 clientes pilotos até Nov/2024\n• ROI positivo em 18 meses",
        'requisitos': "[MUST] Integração com bancos\n[MUST] Segurança de dados GDPR\n[SHOULD] Interface multi-idioma",
        'equipe': "• GP: Ana Silva\n• Tech Lead: Carlos Souza\n• PO: Mariana Costa\n• 5 devs fullstack",
        'entregas': "1. Especificação técnica (M1)\n2. Módulo financeiro (M3)\n3. MVP completo (M6)",
        'cronograma': "• F1 (M1-2): Especificação\n• F2 (M3-5): Desenvolvimento\n• F3 (M6): Pilotagem\n• F4 (M7-9): Ajustes e escala",
        'beneficios': "• Redução de 30% em processos manuais\n• Ganho de produtividade de 25%\n• Tomada de decisão mais ágil",
        'restricoes': "• Orçamento: R$ 1.8M\n• Prazo: 9 meses\n• Equipe limitada a 8 pessoas",
        'custos': "• Desenvolvimento: R$ 1.2M\n• Infra: R$ 300k\n• Marketing: R$ 200k\n• Contingência: R$ 100k",
        'observacoes': "Parceria estratégica com FinTechXYZ para módulo financeiro"
    },
    "Projeto de Transformação Digital": {
        'justificativas': "• Processos obsoletos causando atrasos\n• Necessidade de digitalização para competitividade\n• Expectativa de clientes por serviços digitais",
        'pitch': "Modernização dos processos e sistemas da empresa para oferecer experiência digital integrada aos clientes.",
        'produto_servico': "• Portal do cliente\n• App mobile\n• BPM para automação de processos\n• API Gateway para integração",
        'stakeholders': "• CEO\n• Diretoria de Operações\n• Equipe de TI\n• Consultoria especializada",
        'premissas': "• Mudança cultural será apoiada pela liderança\n• Budget aprovado em 3 etapas\n• Equipe terá treinamento adequado",
        'riscos': "1. Resistência à mudança [Prob: Alta] [Impacto: Médio]\n2. Complexidade de integração [Prob: Média] [Impacto: Alto]",
        'objetivos': "• Reduzir tempo de atendimento em 40%\n• Digitalizar 80% dos processos em 12 meses\n• NPS acima de 70",
        'requisitos': "[MUST] Acessibilidade WCAG\n[MUST] Disponibilidade 99.9%\n[SHOULD] Chatbot integrado",
        'equipe': "• GP: João Mendes\n• Arquiteta: Paula Lima\n• 6 desenvolvedores\n• 2 analistas de negócio",
        'entregas': "1. Diagnóstico AS-IS\n2. Blueprint TO-BE\n3. MVP Portal\n4. Rollout completo",
        'cronograma': "• Fase 1: Análise (2 meses)\n• Fase 2: Desenvolvimento (5 meses)\n• Fase 3: Implantação (3 meses)",
        'beneficios': "• Melhoria na experiência do cliente\n• Redução de custos operacionais\n• Agilidade na lançamento de novos produtos",
        'restricoes': "• Não pode parar operação atual\n• Deve manter compatibilidade com sistemas legados\n• Orçamento faseado",
        'custos': "• Consultoria: R$ 500k\n• Desenvolvimento: R$ 1.5M\n• Infraestrutura: R$ 800k\n• Treinamento: R$ 200k",
        'observacoes': "Alinhar com projeto de Cultura Digital que acontece em paralelo"
    }
}

# Sidebar com informações básicas
with st.sidebar:
    st.image("https://tecvitoria.com.br/wp-content/uploads/2022/03/logo-tecvitoria-horizontal.png", width=200)
    st.markdown("### Informações Básicas")
    nome_projeto = st.text_input("Nome do Projeto*", placeholder="Nome oficial do projeto", help="O nome oficial do projeto como registrado na organização")
    responsavel = st.text_input("Responsável*", placeholder="Gerente do Projeto", help="Nome do gerente ou líder do projeto")
    data = st.date_input("Data*", datetime.date.today())
    versao = st.text_input("Versão", placeholder="1.0", help="Versão deste canvas")
    
    st.markdown("---")
    st.markdown("### Templates")
    selected_template = st.selectbox("Carregar template:", list(templates.keys()))
    
    if selected_template != "Selecione um template":
        if st.button("Aplicar Template"):
            st.session_state.template_data = templates[selected_template]
            st.success("Template aplicado com sucesso! Revise e adapte os campos conforme necessário.")
    
    st.markdown("---")
    st.markdown("### Ações")
    if st.button("Limpar Formulário"):
        for key in field_hints:
            st.session_state[key] = ""
        st.session_state['nome_projeto'] = ""
        st.session_state['responsavel'] = ""
        st.experimental_rerun()

# Inicializar session_state
for key in field_hints:
    if key not in st.session_state:
        st.session_state[key] = templates["Selecione um template"][key]
if 'nome_projeto' not in st.session_state:
    st.session_state['nome_projeto'] = ""
if 'responsavel' not in st.session_state:
    st.session_state['responsavel'] = ""

# Formulário principal
tab1, tab2 = st.tabs(["📝 Preencher Canvas", "🖼️ Visualizar Canvas"])

with tab1:
    st.markdown("### Preencha as seções do Project Model Canvas")
    
    # Seção 1
    with st.expander("🔍 Justificativas", expanded=True):
        st.text_area("Por que este projeto existe?", key='justificativas', height=150, 
                   help=field_hints['justificativas'])
    
    # Seção 2
    with st.expander("🎤 Pitch do Projeto"):
        st.text_area("Resumo executivo do projeto", key='pitch', height=120, 
                   help=field_hints['pitch'])
    
    # Seção 3
    with st.expander("📦 Produto/Serviço"):
        st.text_area("O que será entregue?", key='produto_servico', height=150, 
                   help=field_hints['produto_servico'])
    
    # Seção 4
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("👥 Stakeholders"):
            st.text_area("Partes interessadas", key='stakeholders', height=200, 
                       help=field_hints['stakeholders'])
    
    with col2:
        with st.expander("🔮 Premissas"):
            st.text_area("Suposições base", key='premissas', height=200, 
                       help=field_hints['premissas'])
    
    # Seção 5
    with st.expander("⚠️ Riscos"):
        st.text_area("Riscos e planos de mitigação", key='riscos', height=200, 
                   help=field_hints['riscos'])
    
    # Seção 6
    col3, col4 = st.columns(2)
    with col3:
        with st.expander("🎯 Objetivos"):
            st.text_area("Resultados esperados", key='objetivos', height=200, 
                       help=field_hints['objetivos'])
    
    with col4:
        with st.expander("📋 Requisitos"):
            st.text_area("Necessidades obrigatórias e desejáveis", key='requisitos', height=200, 
                       help=field_hints['requisitos'])
    
    # Seção 7
    with st.expander("👩‍💻 Equipe"):
        st.text_area("Responsáveis e papéis", key='equipe', height=150, 
                   help=field_hints['equipe'])
    
    # Seção 8
    col5, col6 = st.columns(2)
    with col5:
        with st.expander("📦 Entregas"):
            st.text_area("Principais marcos e entregáveis", key='entregas', height=200, 
                       help=field_hints['entregas'])
    
    with col6:
        with st.expander("📅 Cronograma"):
            st.text_area("Fases e prazos", key='cronograma', height=200, 
                       help=field_hints['cronograma'])
    
    # Seção 9
    with st.expander("💰 Custos"):
        st.text_area("Estimativas de custos", key='custos', height=150, 
                   help=field_hints['custos'])
    
    # Seção 10
    col7, col8 = st.columns(2)
    with col7:
        with st.expander("✨ Benefícios"):
            st.text_area("Benefícios esperados", key='beneficios', height=200, 
                       help=field_hints['beneficios'])
    
    with col8:
        with st.expander("🚧 Restrições"):
            st.text_area("Limitações do projeto", key='restricoes', height=200, 
                       help=field_hints['restricoes'])
    
    # Seção 11
    with st.expander("📝 Observações"):
        st.text_area("Outras informações relevantes", key='observacoes', height=150, 
                   help=field_hints['observacoes'])

with tab2:
    st.markdown("### Pré-visualização do Project Model Canvas")
    
    if st.session_state['nome_projeto'] or st.session_state['responsavel'] or any(st.session_state[key] for key in field_hints):
        # Preparar dados para o canvas
        canvas_data = {
            'nome_projeto': st.session_state['nome_projeto'],
            'responsavel': st.session_state['responsavel'],
            'data': data.strftime("%d/%m/%Y")
        }
        
        # Adicionar todos os campos do formulário
        for key in field_hints:
            canvas_data[key] = st.session_state[key]
        
        # Gerar imagem do canvas
        canvas_img = generate_canvas(canvas_data)
        
        # Mostrar preview
        st.image(canvas_img, caption="Project Model Canvas - TecVitória", use_column_width=True)
        
        # Botão para download
        img_bytes = io.BytesIO()
        canvas_img.save(img_bytes, format='PNG')
        img_bytes = img_bytes.getvalue()
        
        st.download_button(
            label="⬇️ Baixar Canvas (PNG)",
            data=img_bytes,
            file_name=f"project_model_canvas_{st.session_state['nome_projeto'].replace(' ', '_').lower()}.png",
            mime="image/png"
        )
        
        # Opção para PDF (seria necessário relatório em PDF)
        # st.download_button(
        #     label="⬇️ Baixar Relatório (PDF)",
        #     data=generate_pdf(canvas_data),  # Função hipotética
        #     file_name=f"project_model_canvas_{st.session_state['nome_projeto'].replace(' ', '_').lower()}.pdf",
        #     mime="application/pdf"
        # )
    else:
        st.warning("Preencha pelo menos alguns campos no formulário para visualizar o canvas.")

# Rodapé
st.markdown("---")
st.markdown("""
<div class="footer">
    <p>Project Model Canvas - TecVitória © 2024 | Desenvolvido para estruturar projetos de forma clara e visual</p>
    <p style="font-size:0.8rem;">Versão 2.0 | Atualizado em julho/2024</p>
</div>
""", unsafe_allow_html=True)
