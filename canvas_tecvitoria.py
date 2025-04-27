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
    .stTextArea textarea {{
        min-height: 120px;
        font-size: 14px;
        border-radius: 4px;
        border: 1px solid #ddd;
    }}
    /* Cabeçalho */
    .header {{
        background: linear-gradient(135deg, {PRIMARY_COLOR} 0%, {SECONDARY_COLOR} 100%);
        color: white;
        padding: 2rem;
        margin-bottom: 2rem;
        border-radius: 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }}
    .header h1 {{
        color: white;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        font-weight: 700;
    }}
    .header p {{
        margin-bottom: 0;
        font-size: 1.1rem;
        opacity: 0.9;
    }}
    .logo {{
        margin-bottom: 1rem;
    }}
    /* Seções */
    .section-title {{
        font-size: 1.3rem;
        font-weight: 600;
        color: {PRIMARY_COLOR};
        margin-bottom: 0.8rem;
        padding-bottom: 0.3rem;
        border-bottom: 2px solid {SECONDARY_COLOR};
    }}
    /* Botões */
    .stButton>button {{
        background-color: {SECONDARY_COLOR};
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 4px;
        padding: 0.7rem 1.8rem;
        transition: all 0.3s;
        font-size: 1rem;
    }}
    .stButton>button:hover {{
        background-color: {PRIMARY_COLOR};
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }}
    /* Dicas */
    .tooltip {{
        color: #666;
        font-size: 0.9rem;
        margin-bottom: 0.8rem;
        background-color: #f9f9f9;
        padding: 0.8rem;
        border-radius: 4px;
        border-left: 4px solid {ACCENT_COLOR};
    }}
    /* Canvas */
    .canvas-container {{
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 1.5rem;
        background-color: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }}
    /* Abas */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
        padding: 0 1rem;
    }}
    .stTabs [data-baseweb="tab"] {{
        background: #f0f0f0;
        border-radius: 4px 4px 0 0;
        padding: 10px 20px;
        margin-right: 0;
        font-weight: 600;
        transition: all 0.3s;
    }}
    .stTabs [aria-selected="true"] {{
        background: {PRIMARY_COLOR};
        color: white;
    }}
    /* Sidebar */
    [data-testid="stSidebar"] {{
        background-color: #fff;
        border-right: 1px solid #eee;
    }}
    /* Cards */
    .card {{
        background: white;
        border-radius: 8px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        border-left: 4px solid {SECONDARY_COLOR};
    }}
</style>
""", unsafe_allow_html=True)

# Cabeçalho personalizado no estilo TecVitória
st.markdown(f"""
<div class="header">
    <div style="display: flex; align-items: center; justify-content: space-between;">
        <div>
            <div class="logo">
                <img src="https://tecvitoria.com.br/wp-content/uploads/2022/03/logo-tecvitoria-horizontal-branco.png" alt="TecVitória" style="height: 50px;">
            </div>
            <h1>Project Model Canvas</h1>
            <p>Siga o modelo da primeira incubadora do Espírito Santo para estruturar seu projeto</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Função para gerar o canvas
def generate_canvas(data):
    """Gera a imagem do canvas com as informações fornecidas"""
    # Cria uma imagem em branco (formato A3 horizontal)
    img = Image.new('RGB', (1754, 1240), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    
    try:
        # Tenta carregar fontes (pode não funcionar no Replit)
        font_title = ImageFont.truetype("arialbd.ttf", 36)
        font_subtitle = ImageFont.truetype("arialbd.ttf", 28)
        font_text = ImageFont.truetype("arial.ttf", 20)
        font_small = ImageFont.truetype("arial.ttf", 16)
    except:
        # Fallback para fontes padrão
        font_title = ImageFont.load_default()
        font_subtitle = ImageFont.load_default()
        font_text = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Cores TecVitória
    color_primary = (0, 51, 102)  # #003366
    color_secondary = (255, 102, 0)  # #FF6600
    color_accent = (0, 204, 204)  # #00CCCC
    
    # Logo TecVitória (simulado com texto)
    d.text((50, 50), "TECVITÓRIA", font=font_title, fill=color_primary)
    d.text((300, 60), "Project Model Canvas", font=font_subtitle, fill=color_secondary)
    d.line([(50, 100), (1700, 100)], fill=color_primary, width=3)
    
    # Grid do canvas (12 seções conforme modelo MOA)
    sections = [
        # Linha 1
        {"title": "JUSTIFICATIVAS", "position": (50, 120, 400, 300), "content": data['justificativas'], 
         "color": color_primary},
        {"title": "PITCH", "position": (410, 120, 850, 300), "content": data['pitch'], 
         "color": color_secondary},
        {"title": "PRODUTO", "position": (860, 120, 1200, 300), "content": data['produto'], 
         "color": color_primary},
        {"title": "STAKEHOLDERS", "position": (1210, 120, 1700, 300), "content": data['stakeholders'], 
         "color": color_secondary},
        
        # Linha 2
        {"title": "PREMISSAS", "position": (50, 320, 400, 500), "content": data['premissas'], 
         "color": color_secondary},
        {"title": "RISCOS", "position": (410, 320, 850, 500), "content": data['riscos'], 
         "color": color_primary},
        {"title": "OBJETIVOS SMART", "position": (860, 320, 1200, 500), "content": data['objetivos'], 
         "color": color_secondary},
        {"title": "REQUISITOS", "position": (1210, 320, 1700, 500), "content": data['requisitos'], 
         "color": color_primary},
        
        # Linha 3
        {"title": "EQUIPE", "position": (50, 520, 400, 700), "content": data['equipe'], 
         "color": color_primary},
        {"title": "ENTREGAS", "position": (410, 520, 850, 700), "content": data['entregas'], 
         "color": color_secondary},
        {"title": "CRONOGRAMA", "position": (860, 520, 1200, 700), "content": data['cronograma'], 
         "color": color_primary},
        {"title": "BENEFÍCIOS", "position": (1210, 520, 1700, 700), "content": data['beneficios'], 
         "color": color_secondary},
        
        # Linha 4
        {"title": "RESTRIÇÕES", "position": (50, 720, 850, 900), "content": data['restricoes'], 
         "color": color_secondary},
        {"title": "CUSTOS", "position": (860, 720, 1700, 900), "content": data['custos'], 
         "color": color_primary},
        
        # Rodapé
        {"title": "INFO", "position": (50, 920, 1700, 1190), "content": f"Projeto: {data['nome_projeto']}\nResponsável: {data['responsavel']}\nData: {data['data']}", 
         "color": color_accent}
    ]
    
    # Desenha cada seção
    for section in sections:
        x0, y0, x1, y1 = section['position']
        
        # Borda da seção
        d.rectangle([x0, y0, x1, y1], outline=color_primary, width=1)
        
        # Fundo do título
        d.rectangle([x0, y0, x1, y0+50], fill=section['color'])
        
        # Título
        d.text((x0+15, y0+10), section['title'], font=font_subtitle, fill='white')
        
        # Conteúdo
        if section['content']:
            lines = section['content'].split('\n')
            for i, line in enumerate(lines[:12]):  # Limita a 12 linhas por seção
                if line.strip():
                    d.text((x0+15, y0+60 + (i*22)), line, font=font_text, fill=TEXT_COLOR)
    
    return img

# Dicas detalhadas para cada campo
field_hints = {
    'justificativas': """Preencha com:
• Contexto histórico do projeto
• Problemas identificados
• Necessidades não atendidas
• Dados quantitativos que justificam o projeto""",
    
    'pitch': """Apresentação resumida do projeto (1-2 parágrafos):
• Qual problema resolve?
• Para quem?
• Qual a solução proposta?
• Diferenciais principais""",
    
    'produto': """Descreva:
• O que será entregue (produto, serviço ou resultado)
• Características principais
• Forma de entrega""",
    
    'stakeholders': """Liste:
• Partes interessadas externas
• Fatores externos que podem impactar
• Influenciadores chave""",
    
    'premissas': """Suposições consideradas verdadeiras:
• Fatores não controláveis pelo projeto
• Condições necessárias para o sucesso""",
    
    'riscos': """Identifique:
• Eventos incertos com impacto no projeto
• Probabilidade x consequência
• Planos de mitigação""",
    
    'objetivos': """Objetivos SMART:
• Específicos: Claramente definidos
• Mensuráveis: Com indicadores
• Atingíveis: Dentro das capacidades
• Relevantes: Alinhados à estratégia
• Temporizáveis: Com prazo definido""",
    
    'requisitos': """Critérios essenciais (MoSCoW):
• Must have: Imprescindíveis
• Should have: Importantes mas não críticos
• Could have: Desejáveis
• Won't have: Excluídos deste projeto""",
    
    'equipe': """Membros responsáveis:
• Nome/Função
• Principais responsabilidades
• Alocação (% de tempo)""",
    
    'entregas': """Componentes tangíveis:
• Processos
• Projetos
• Treinamentos
• Artefatos""",
    
    'cronograma': """Dividido em 4 períodos:
• Fase 1: [datas] - [entregas]
• Fase 2: [datas] - [entregas]
• Marcos principais""",
    
    'beneficios': """Ganhos esperados:
• Financeiros
• Estratégicos
• Operacionais
• Qualitativos""",
    
    'restricoes': """Limitações:
• Recursos
• Prazos
• Escopo
• Tecnologia""",
    
    'custos': """Orçamento detalhado:
• Dividido por entregas/fases
• Custos diretos e indiretos
• Reserva para contingências"""
}

# Templates pré-definidos
templates = {
    "Selecione um template": {k: "" for k in field_hints},
    "Projeto de Inovação": {
        'justificativas': "• Mercado em transformação digital\n• Concorrência lançou novo produto\n• Clientes pedindo solução integrada\n• Oportunidade de R$ 2M/ano",
        'pitch': "Desenvolvimento de plataforma integrada de gestão para PMEs, combinando ERP, CRM e BI em uma solução simples e acessível, com implementação em 6 meses.",
        'produto': "• Plataforma SaaS modular\n• Integração com bancos e marketplaces\n• Painel de indicadores em tempo real\n• App mobile para acompanhamento",
        'stakeholders': "• Diretoria Executiva (decisora)\n• Líderes de departamento (usuários)\n• Consultoria de TI (parceira)\n• Concorrente X (benchmark)",
        'premissas': "• Equipe permanecerá alocada\n• Orçamento aprovado até março\n• Não haverá mudanças regulatórias\n• Infraestrutura cloud disponível",
        'riscos': "• Atraso na aprovação [Prob: Média] [Impacto: Alto]\n• Resistência à mudança [Prob: Alta] [Impacto: Médio]\n• Falha na integração [Prob: Baixa] [Impacto: Alto]",
        'objetivos': "• Lançar MVP até 30/09/2024\n• 100 clientes em 6 meses pós-lançamento\n• ROI em 18 meses\n• NPS mínimo de 70",
        'requisitos': "[MUST] Integração com bancos\n[MUST] Segurança de dados\n[SHOULD] Multi-idioma\n[COULD] Chatbot de suporte",
        'equipe': "• GP: Ana Silva (100%)\n• Tech Lead: Carlos Souza (80%)\n• Devs: 3 (60% cada)\n• UX/UI: 1 (50%)",
        'entregas': "1. Especificação técnica\n2. Módulo financeiro\n3. Módulo vendas\n4. Painel BI\n5. Treinamentos",
        'cronograma': "• F1 (M1-2): Especificação\n• F2 (M3-5): Desenvolvimento\n• F3 (M6): Testes\n• F4 (M7): Go-live",
        'beneficios': "• Redução de 30% em processos manuais\n• Aumento de 15% na produtividade\n• Economia de R$ 500k/ano\n• Melhor experiência do cliente",
        'restricoes': "• Orçamento: R$ 1.8M\n• Prazo: 7 meses\n• Equipe limitada a 6 pessoas",
        'custos': "• Desenvolvimento: R$ 1.2M\n• Infra: R$ 300k\n• Marketing: R$ 200k\n• Reserva: R$ 100k"
    },
    "Projeto Social TecVitória": {
        'justificativas': "• 25% dos jovens da região desempregados\n• Falta de qualificação em tecnologia\n• Parcerias com empresas precisando de mão de obra\n• Oportunidade de impacto social",
        'pitch': "Programa de capacitação em tecnologia para 120 jovens de baixa renda, com mentoria profissional e garantia de entrevistas nas empresas parceiras, em 8 meses.",
        'produto': "• Curso de programação web (400h)\n• Mentoria profissional semanal\n• Feira de oportunidades\n• Certificação reconhecida",
        'stakeholders': "• Secretaria Municipal de Trabalho\n• 10 empresas parceiras\n• ONGs locais\n• Comunidade\n• Famílias dos alunos",
        'premissas': "• Espaço físico disponível\n• 60% dos alunos completarão o curso\n• Empresas contratarão pelo menos 30% dos formados\n• Verba aprovada até março",
        'riscos': "• Evasão de alunos [Prob: Alta] [Impacto: Alto]\n• Falta de empresas parceiras [Prob: Média] [Impacto: Alto]\n• Infraestrutura inadequada [Prob: Baixa] [Impacto: Médio]",
        'objetivos': "• Formar 120 jovens em 8 meses\n• 60 entrevistas realizadas\n• 40% empregados em 3 meses\n• Satisfação de 85% dos alunos",
        'requisitos': "[MUST] Laboratório com 30 computadores\n[MUST] Professores qualificados\n[SHOULD] Material didático próprio\n[COULD] Plataforma EAD complementar",
        'equipe': "• Coordenador Pedagógico\n• 4 Instrutores\n• Assistente Social\n• Psicóloga (20h/semana)",
        'entregas': "1. Programa do curso\n2. Aulas teóricas e práticas\n3. Mentorias individuais\n4. Feira de empregos\n5. Certificação",
        'cronograma': "• M1: Captação alunos\n• M2-7: Aulas e mentorias\n• M8: Feira e encerramento",
        'beneficios': "• 48 jovens empregados\n• Renda para famílias carentes\n• Mão de obra qualificada local\n• Reconhecimento da marca",
        'restricoes': "• Orçamento: R$ 450k\n• Espaço para 30 alunos/turma\n• 8 meses de duração",
        'custos': "• Instrutores: R$ 200k\n• Infraestrutura: R$ 120k\n• Material: R$ 80k\n• Eventos: R$ 50k"
    }
}

# Sidebar com informações básicas
with st.sidebar:
    st.image("https://tecvitoria.com.br/wp-content/uploads/2022/03/logo-tecvitoria-horizontal.png", width=200)
    st.markdown("### Informações do Projeto")
    
    nome_projeto = st.text_input("Nome do Projeto", key="nome_projeto", placeholder="Digite o nome do projeto")
    responsavel = st.text_input("Responsável", key="responsavel", placeholder="Nome do gerente de projeto")
    data = st.date_input("Data", datetime.date.today(), key="data")
    
    st.markdown("---")
    st.markdown("### Templates")
    selected_template = st.selectbox("Selecione um template:", list(templates.keys()), key="template_select")
    
    if selected_template != "Selecione um template":
        if st.button("Carregar Template", key="load_template"):
            for key in st.session_state:
                if key in templates[selected_template]:
                    st.session_state[key] = templates[selected_template][key]
            st.success(f"Template '{selected_template}' carregado!")
    
    st.markdown("---")
    st.markdown("**Dicas de preenchimento:**")
    st.markdown("1. Seja claro e objetivo")
    st.markdown("2. Use tópicos curtos")
    st.markdown("3. Revise antes de gerar")
    st.markdown("---")
    st.markdown("**Sobre a TecVitória:**")
    st.markdown("Primeira incubadora do Espírito Santo, fundada em 1995, com mais de 150 projetos incubados e 80 empresas graduadas.")

# Formulário principal com abas
tab1, tab2 = st.tabs(["📝 Formulário Completo", "🖼️ Visualizar Canvas"])

with tab1:
    with st.form("canvas_form"):
        # Seção 1 - Por quê?
        st.markdown("## 1. Por quê? (Justificativa e Objetivos)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="card"><div class="section-title">JUSTIFICATIVAS</div>', unsafe_allow_html=True)
            st.markdown('<div class="tooltip">'+field_hints['justificativas']+'</div>', unsafe_allow_html=True)
            justificativas = st.text_area("", key="justificativas", height=200,
                                        placeholder="Contexto, problemas e necessidades...", label_visibility="collapsed")
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown('<div class="card"><div class="section-title">PITCH</div>', unsafe_allow_html=True)
            st.markdown('<div class="tooltip">'+field_hints['pitch']+'</div>', unsafe_allow_html=True)
            pitch = st.text_area("", key="pitch", height=150,
                               placeholder="Apresentação resumida do projeto...", label_visibility="collapsed")
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="card"><div class="section-title">OBJETIVOS SMART</div>', unsafe_allow_html=True)
            st.markdown('<div class="tooltip">'+field_hints['objetivos']+'</div>', unsafe_allow_html=True)
            objetivos = st.text_area("", key="objetivos", height=150,
                                   placeholder="Específicos, Mensuráveis, Atingíveis...", label_visibility="collapsed")
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown('<div class="card"><div class="section-title">BENEFÍCIOS</div>', unsafe_allow_html=True)
            st.markdown('<div class="tooltip">'+field_hints['beneficios']+'</div>', unsafe_allow_html=True)
            beneficios = st.text_area("", key="beneficios", height=200,
                                    placeholder="Ganhos esperados com o projeto...", label_visibility="collapsed")
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Seção 2 - O quê?
        st.markdown("## 2. O quê? (Produto e Requisitos)")
        
        col3, col4 = st.columns(2)
        
        with col3:
            st.markdown('<div class="card"><div class="section-title">PRODUTO</div>', unsafe_allow_html=True)
            st.markdown('<div class="tooltip">'+field_hints['produto']+'</div>', unsafe_allow_html=True)
            produto = st.text_area("", key="produto", height=200,
                                 placeholder="O que será entregue ao final...", label_visibility="collapsed")
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col4:
            st.markdown('<div class="card"><div class="section-title">REQUISITOS</div>', unsafe_allow_html=True)
            st.markdown('<div class="tooltip">'+field_hints['requisitos']+'</div>', unsafe_allow_html=True)
            requisitos = st.text_area("", key="requisitos", height=200,
                                    placeholder="Critérios essenciais (MoSCoW)...", label_visibility="collapsed")
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Seção 3 - Quem?
        st.markdown("## 3. Quem? (Stakeholders e Equipe)")
        
        col5, col6 = st.columns(2)
        
        with col5:
            st.markdown('<div class="card"><div class="section-title">STAKEHOLDERS</div>', unsafe_allow_html=True)
            st.markdown('<div class="tooltip">'+field_hints['stakeholders']+'</div>', unsafe_allow_html=True)
            stakeholders = st.text_area("", key="stakeholders", height=200,
                                      placeholder="Partes interessadas externas...", label_visibility="collapsed")
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col6:
            st.markdown('<div class="card"><div class="section-title">EQUIPE</div>', unsafe_allow_html=True)
            st.markdown('<div class="tooltip">'+field_hints['equipe']+'</div>', unsafe_allow_html=True)
            equipe = st.text_area("", key="equipe", height=200,
                                placeholder="Membros e responsabilidades...", label_visibility="collapsed")
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Seção 4 - Como?
        st.markdown("## 4. Como? (Premissas, Entregas e Restrições)")
        
        col7, col8, col9 = st.columns([1,1,1])
        
        with col7:
            st.markdown('<div class="card"><div class="section-title">PREMISSAS</div>', unsafe_allow_html=True)
            st.markdown('<div class="tooltip">'+field_hints['premissas']+'</div>', unsafe_allow_html=True)
            premissas = st.text_area("", key="premissas", height=200,
                                   placeholder="Suposições consideradas...", label_visibility="collapsed")
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col8:
            st.markdown('<div class="card"><div class="section-title">ENTREGAS</div>', unsafe_allow_html=True)
            st.markdown('<div class="tooltip">'+field_hints['entregas']+'</div>', unsafe_allow_html=True)
            entregas = st.text_area("", key="entregas", height=200,
                                  placeholder="Componentes tangíveis...", label_visibility="collapsed")
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col9:
            st.markdown('<div class="card"><div class="section-title">RESTRIÇÕES</div>', unsafe_allow_html=True)
            st.markdown('<div class="tooltip">'+field_hints['restricoes']+'</div>', unsafe_allow_html=True)
            restricoes = st.text_area("", key="restricoes", height=200,
                                    placeholder="Limitações do projeto...", label_visibility="collapsed")
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Seção 5 - Quando/Quanto?
        st.markdown("## 5. Quando/Quanto? (Cronograma, Riscos e Custos)")
        
        col10, col11, col12 = st.columns([1,1,1])
        
        with col10:
            st.markdown('<div class="card"><div class="section-title">CRONOGRAMA</div>', unsafe_allow_html=True)
            st.markdown('<div class="tooltip">'+field_hints['cronograma']+'</div>', unsafe_allow_html=True)
            cronograma = st.text_area("", key="cronograma", height=200,
                                    placeholder="Dividido em 4 períodos...", label_visibility="collapsed")
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col11:
            st.markdown('<div class="card"><div class="section-title">RISCOS</div>', unsafe_allow_html=True)
            st.markdown('<div class="tooltip">'+field_hints['riscos']+'</div>', unsafe_allow_html=True)
            riscos = st.text_area("", key="riscos", height=200,
                                placeholder="Eventos incertos com impacto...", label_visibility="collapsed")
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col12:
            st.markdown('<div class="card"><div class="section-title">CUSTOS</div>', unsafe_allow_html=True)
            st.markdown('<div class="tooltip">'+field_hints['custos']+'</div>', unsafe_allow_html=True)
            custos = st.text_area("", key="custos", height=200,
                                placeholder="Orçamento detalhado...", label_visibility="collapsed")
            st.markdown("</div>", unsafe_allow_html=True)
        
        submitted = st.form_submit_button("✨ Gerar Project Model Canvas", use_container_width=True)

with tab2:
    if submitted:
        data = {
            'justificativas': justificativas,
            'pitch': pitch,
            'produto': produto,
            'stakeholders': stakeholders,
            'premissas': premissas,
            'riscos': riscos,
            'objetivos': objetivos,
            'requisitos': requisitos,
            'equipe': equipe,
            'entregas': entregas,
            'cronograma': cronograma,
            'beneficios': beneficios,
            'restricoes': restricoes,
            'custos': custos,
            'data': data.strftime("%d/%m/%Y"),
            'nome_projeto': nome_projeto,
            'responsavel': responsavel
        }
        
        with st.spinner('Gerando seu Project Model Canvas no padrão TecVitória...'):
            canvas_img = generate_canvas(data)
            
            # Mostrar preview
            st.success("✅ Canvas gerado com sucesso!")
            st.image(canvas_img, caption="Project Model Canvas - TecVitória", use_column_width=True)
            
            # Preparar para download
            img_bytes = io.BytesIO()
            canvas_img.save(img_bytes, format='PNG')
            
            # Botões de download
            st.markdown("### Exportar Canvas")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.download_button(
                    label="⬇️ Baixar PNG (Imagem)",
                    data=img_bytes.getvalue(),
                    file_name=f"canvas_tecvitoria_{nome_projeto.replace(' ', '_')}.png",
                    mime="image/png"
                )
            
            with col2:
                img_bytes_pdf = io.BytesIO()
                canvas_img.save(img_bytes_pdf, format='PDF')
                st.download_button(
                    label="⬇️ Baixar PDF (Documento)",
                    data=img_bytes_pdf.getvalue(),
                    file_name=f"canvas_tecvitoria_{nome_projeto.replace(' ', '_')}.pdf",
                    mime="application/pdf"
                )
            
            with col3:
                text_content = f"""PROJECT MODEL CANVAS - TECVITÓRIA
================================

PROJETO: {nome_projeto}
RESPONSÁVEL: {responsavel}
DATA: {data.strftime("%d/%m/%Y")}

1. POR QUÊ?
----------
JUSTIFICATIVAS:
{justificativas}

PITCH:
{pitch}

OBJETIVOS SMART:
{objetivos}

BENEFÍCIOS:
{beneficios}

2. O QUÊ?
---------
PRODUTO:
{produto}

REQUISITOS:
{requisitos}

3. QUEM?
--------
STAKEHOLDERS:
{stakeholders}

EQUIPE:
{equipe}

4. COMO?
--------
PREMISSAS:
{premissas}

ENTREGAS:
{entregas}

RESTRIÇÕES:
{restricoes}

5. QUANDO/QUANTO?
-----------------
CRONOGRAMA:
{cronograma}

RISCOS:
{riscos}

CUSTOS:
{custos}

"""
                st.download_button(
                    label="⬇️ Baixar TXT (Texto)",
                    data=text_content,
                    file_name=f"canvas_tecvitoria_{nome_projeto.replace(' ', '_')}.txt",
                    mime="text/plain"
                )
    else:
        st.info("Preencha o formulário na aba 'Formulário Completo' e clique em 'Gerar Project Model Canvas' para visualizar o resultado.")
        st.image("https://tecvitoria.com.br/wp-content/uploads/2022/03/logo-tecvitoria-horizontal.png", width=300)
        st.markdown("""
        ### Sobre o Project Model Canvas da TecVitória:
        
        Esta ferramenta foi desenvolvida para ajudar empreendedores e gestores a estruturar seus projetos de forma clara e visual, seguindo a metodologia da primeira incubadora do Espírito Santo.
        
        **Como usar:**
        1. Preencha todas as seções do formulário
        2. Revise as informações
        3. Gere o canvas
        4. Exporte nos formatos disponíveis
        
        Dúvidas? Visite [tecvitoria.com.br](https://tecvitoria.com.br) ou entre em contato pelo email contato@tecvitoria.com.br
        """)

# Rodapé
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9rem;">
    <p>Project Model Canvas - Desenvolvido pela TecVitória | Primeira incubadora do Espírito Santo</p>
    <p>© 2024 TecVitória - Todos os direitos reservados</p>
</div>
""", unsafe_allow_html=True)
