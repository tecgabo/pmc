# Importações necessárias
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import datetime
import textwrap
from fpdf import FPDF  # Para geração de PDF

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
TEXT_COLOR = "#333333"

# URL do novo logo da TecVitória (amarelo)
TECVITORIA_LOGO = "https://tecvitoria.com.br/wp-content/uploads/2025/04/logo-amarelo.webp"

# Templates atualizados
TEMPLATES = {
    "Selecione um template": {k: "" for k in [
        'justificativas', 'pitch', 'produto', 'stakeholders', 'premissas', 'riscos', 
        'objetivos', 'requisitos', 'equipe', 'entregas', 'cronograma', 'beneficios', 
        'restricoes', 'custos', 'observacoes']},
    
    "Projeto de Inovação": {
        'justificativas': "• Mercado em transformação digital\n• Concorrência lançou novo produto\n• Clientes pedindo solução integrada\n• Oportunidade de R$ 2M/ano",
        'pitch': "Desenvolvimento de plataforma integrada de gestão para PMEs, combinando ERP, CRM e BI em uma solução simples e acessível, com implementação em 6 meses.",
        'produto': "• Plataforma SaaS modular\n• Integração com bancos e marketplaces\n• Painel de indicadores em tempo real\n• App mobile para acompanhamento",
        'stakeholders': "• Diretoria Executiva (decisora)\n• Líderes de departamento (usuários)\n• Consultoria de TI (parceira)\n• Concorrente X (benchmark)",
        'premissas': "• Equipe permanecerá alocada\n• Orçamento aprovado até março\n• Não haverá mudanças regulatórias\n• Infraestrutura cloud disponível",
        'riscos': "• Atraso na aprovação [Prob: Média] [Impacto: Alto]\n• Resistência à mudança [Prob: Alta] [Impacto: Médio]\n• Falta na integração [Prob: Baixa] [Impacto: Alto]",
        'objetivos': "• Lançar MVP até 30/09/2024\n• 100 clientes em 6 meses pós-lançamento\n• ROI em 18 meses\n• NPS mínimo de 70",
        'requisitos': "[MUST] Integração com bancos\n[MUST] Segurança de dados\n[SHOULD] Multi-idioma\n[COULD] Chatbot de suporte",
        'equipe': "• GP: Ana Silva (100%)\n• Tech Lead: Carlos Souza (80%)\n• Devs: 3 (60% cada)\n• UX/UI: 1 (50%)",
        'entregas': "1. Especificação técnica\n2. Módulo financeiro\n3. Módulo vendas\n4. Painel BI\n5. Treinamentos",
        'cronograma': "• F1 (M1-2): Especificação\n• F2 (M3-5): Desenvolvimento\n• F3 (M6): Testes\n• F4 (M7): Go-live",
        'beneficios': "• Redução de 30% em processos manuais\n• Aumento de 15% na produtividade\n• Economia de R$ 500k/ano\n• Melhor experiência do cliente",
        'restricoes': "• Orçamento: R$ 1.8M\n• Prazo: 7 meses\n• Equipe limitada a 6 pessoas",
        'custos': "• Desenvolvimento: R$ 1.2M\n• Infra: R$ 300k\n• Marketing: R$ 200k\n• Reserva: R$ 100k",
        'observacoes': ""
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
        'custos': "• Instrutores: R$ 200k\n• Infraestrutura: R$ 120k\n• Material: R$ 80k\n• Eventos: R$ 50k",
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
    .template-card {{
        background-color: white;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid {SECONDARY_COLOR};
    }}
    .template-card h3 {{
        color: {PRIMARY_COLOR};
    }}
    .guide-section {{
        background-color: white;
        border-radius: 8px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
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
    img = Image.new('RGB', (2480, 3508), color=(255, 255, 255))  # A4 em 300dpi
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
    
    # Grid do canvas (15 seções)
    sections = [
        {"name": "Justificativas", "pos": (100, 350, 780, 650), "key": "justificativas"},
        {"name": "Pitch", "pos": (800, 350, 1480, 650), "key": "pitch"},
        {"name": "Produto/Serviço", "pos": (1500, 350, 2380, 650), "key": "produto"},
        {"name": "Stakeholders", "pos": (100, 700, 780, 1000), "key": "stakeholders"},
        {"name": "Premissas", "pos": (800, 700, 1480, 1000), "key": "premissas"},
        {"name": "Riscos", "pos": (1500, 700, 2380, 1000), "key": "riscos"},
        {"name": "Objetivos", "pos": (100, 1050, 780, 1350), "key": "objetivos"},
        {"name": "Requisitos", "pos": (800, 1050, 1480, 1350), "key": "requisitos"},
        {"name": "Equipe", "pos": (1500, 1050, 2380, 1350), "key": "equipe"},
        {"name": "Entregas", "pos": (100, 1400, 780, 1700), "key": "entregas"},
        {"name": "Cronograma", "pos": (800, 1400, 1480, 1700), "key": "cronograma"},
        {"name": "Benefícios", "pos": (1500, 1400, 2380, 1700), "key": "beneficios"},
        {"name": "Restrições", "pos": (100, 1750, 780, 2050), "key": "restricoes"},
        {"name": "Custos", "pos": (800, 1750, 1480, 2050), "key": "custos"},
        {"name": "Observações", "pos": (1500, 1750, 2380, 2050), "key": "observacoes"}
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
        
        # Adicionar conteúdo
        content = data.get(section["key"], "")
        if content:
            wrapped_text = textwrap.wrap(content, width=60)
            y_text = section["pos"][1] + 80
            for line in wrapped_text:
                d.text((section["pos"][0]+20, y_text), line, font=font_text, fill=TEXT_COLOR)
                y_text += 30
    
    return img

# Função para gerar PDF do guia
def generate_pdf_guide():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Cabeçalho
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Guia Completo do Project Model Canvas", ln=1, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="TecVitória - "+datetime.datetime.now().strftime("%d/%m/%Y"), ln=1, align='C')
    pdf.ln(10)
    
    # Seção 1
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="1. O que é o Project Model Canvas?", ln=1)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt="O Project Model Canvas é uma ferramenta visual para planejamento de projetos que organiza todos os elementos essenciais em um único quadro. Desenvolvido para ser mais ágil que documentos tradicionais, ele ajuda times a alinhar expectativas, identificar riscos e comunicar o projeto de forma clara.")
    pdf.ln(5)
    
    # Seção 2
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="2. Áreas do Canvas", ln=1)
    
    sections = [
        ("Justificativas", "Por que este projeto existe? Quais problemas resolve?"),
        ("Pitch", "Resumo executivo do projeto em 1-2 frases impactantes"),
        ("Produto/Serviço", "O que será entregue? Quais as características principais?"),
        ("Stakeholders", "Quem são as partes interessadas e qual seu nível de influência?"),
        ("Premissas", "Quais suposições estão sendo feitas para o projeto?"),
        ("Riscos", "Quais são os principais riscos e como mitigá-los?"),
        ("Objetivos", "Quais resultados concretos o projeto deve alcançar?"),
        ("Requisitos", "Quais são as necessidades obrigatórias e desejáveis?"),
        ("Equipe", "Quem são os responsáveis e quais seus papéis?"),
        ("Entregas", "Quais são os principais marcos e entregáveis?"),
        ("Cronograma", "Quais são as fases principais e prazos?"),
        ("Benefícios", "Quais vantagens o projeto trará?"),
        ("Restrições", "Quais são as limitações do projeto?"),
        ("Custos", "Quais são os principais investimentos necessários?"),
        ("Observações", "Outras informações relevantes")
    ]
    
    for i, (title, desc) in enumerate(sections):
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(200, 10, txt=f"2.{i+1} {title}", ln=1)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=desc)
        pdf.ln(3)
    
    # Seção 3
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="3. Dicas de Preenchimento", ln=1)
    pdf.set_font("Arial", size=12)
    tips = [
        "• Comece pelas Justificativas e Objetivos - eles guiarão todo o resto",
        "• Seja conciso - o Canvas deve ser um resumo, não um documento detalhado",
        "• Use marcadores para melhor organização visual",
        "• Priorize os riscos por probabilidade e impacto",
        "• Revise as premissas regularmente - elas podem mudar"
    ]
    for tip in tips:
        pdf.multi_cell(0, 10, txt=tip)
    
    # Gera o PDF em memória
    pdf_bytes = pdf.output(dest='S').encode('latin-1')
    return pdf_bytes

# Inicializar session_state
if 'dados' not in st.session_state:
    st.session_state.dados = {k: "" for k in TEMPLATES["Selecione um template"].keys()}
    st.session_state.dados.update({
        'nome_projeto': '',
        'responsavel': '',
        'data': datetime.date.today().strftime("%d/%m/%Y"),
        'observacoes': ''
    })

# Sidebar
with st.sidebar:
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
        list(TEMPLATES.keys()),
        index=0
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

# Página principal
tab1, tab2, tab3, tab4 = st.tabs(["📝 Formulário", "🖼️ Visualizar Canvas", "📚 Templates", "ℹ️ Guia do Canvas"])

with tab1:
    cols = st.columns(2)
    
    with cols[0]:
        st.markdown("### Seções Essenciais")
        st.session_state.dados['justificativas'] = st.text_area(
            "Justificativas*",
            value=st.session_state.dados['justificativas'],
            height=150,
            help="Por que este projeto existe? Quais problemas resolve?"
        )
        
        st.session_state.dados['pitch'] = st.text_area(
            "Pitch do Projeto*",
            value=st.session_state.dados['pitch'],
            height=120,
            help="Resuma seu projeto em 1-2 frases impactantes"
        )
        
        st.session_state.dados['objetivos'] = st.text_area(
            "Objetivos*",
            value=st.session_state.dados['objetivos'],
            height=150,
            help="O que o projeto deve alcançar? (SMART)"
        )
        
        st.session_state.dados['produto'] = st.text_area(
            "Produto/Serviço*",
            value=st.session_state.dados['produto'],
            height=150,
            help="O que será entregue? Quais as principais características?"
        )
    
    with cols[1]:
        st.markdown("### Detalhes do Projeto")
        st.session_state.dados['stakeholders'] = st.text_area(
            "Stakeholders",
            value=st.session_state.dados['stakeholders'],
            height=120,
            help="Quem são as partes interessadas?"
        )
        
        st.session_state.dados['requisitos'] = st.text_area(
            "Requisitos",
            value=st.session_state.dados['requisitos'],
            height=120,
            help="O que é essencial (MUST) e o que é desejável (SHOULD)?"
        )
        
        st.session_state.dados['entregas'] = st.text_area(
            "Entregas",
            value=st.session_state.dados['entregas'],
            height=120,
            help="Principais marcos e entregáveis"
        )
        
        st.session_state.dados['cronograma'] = st.text_area(
            "Cronograma",
            value=st.session_state.dados['cronograma'],
            height=120,
            help="Fases e prazos principais"
        )
    
    st.markdown("### Outras Informações")
    cols2 = st.columns(2)
    
    with cols2[0]:
        st.session_state.dados['premissas'] = st.text_area(
            "Premissas",
            value=st.session_state.dados['premissas'],
            height=120
        )
        
        st.session_state.dados['riscos'] = st.text_area(
            "Riscos",
            value=st.session_state.dados['riscos'],
            height=120
        )
        
        st.session_state.dados['restricoes'] = st.text_area(
            "Restrições",
            value=st.session_state.dados['restricoes'],
            height=120
        )
    
    with cols2[1]:
        st.session_state.dados['equipe'] = st.text_area(
            "Equipe",
            value=st.session_state.dados['equipe'],
            height=120
        )
        
        st.session_state.dados['beneficios'] = st.text_area(
            "Benefícios",
            value=st.session_state.dados['beneficios'],
            height=120
        )
        
        st.session_state.dados['custos'] = st.text_area(
            "Custos",
            value=st.session_state.dados['custos'],
            height=120
        )
    
    st.session_state.dados['observacoes'] = st.text_area(
        "Observações Adicionais",
        value=st.session_state.dados['observacoes'],
        height=100
    )

with tab2:
    if st.session_state.dados['nome_projeto']:
        st.markdown(f"### Pré-visualização: {st.session_state.dados['nome_projeto']}")
        
        canvas_img = generate_canvas(st.session_state.dados)
        st.image(canvas_img, caption="Project Model Canvas", use_column_width=True)
        
        # Botão para download
        img_bytes = io.BytesIO()
        canvas_img.save(img_bytes, format='PNG')
        img_bytes = img_bytes.getvalue()
        
        st.download_button(
            label="⬇️ Baixar Canvas (PNG)",
            data=img_bytes,
            file_name=f"canvas_{st.session_state.dados['nome_projeto'].replace(' ', '_').lower()}.png",
            mime="image/png"
        )
    else:
        st.warning("Preencha pelo menos o nome do projeto para visualizar o canvas.")

with tab3:
    st.markdown("""
    ## Biblioteca de Templates
    
    Explore modelos prontos para diferentes tipos de projetos. Clique em "Aplicar Template" na barra lateral para usar.
    """)
    
    for template_name, template_data in list(TEMPLATES.items())[1:]:
        with st.expander(f"📌 {template_name}", expanded=False):
            st.markdown(f"""
            <div class="template-card">
                <h3>{template_name}</h3>
                <p><strong>Pitch:</strong> {template_data['pitch'].split('\n')[0]}</p>
                <p><strong>Objetivo Principal:</strong> {template_data['objetivos'].split('\n')[0]}</p>
                <p><strong>Duração:</strong> {template_data['cronograma'].split('\n')[0]}</p>
            </div>
            """, unsafe_allow_html=True)
            
            cols = st.columns(2)
            with cols[0]:
                st.markdown("**Justificativas**")
                st.text(template_data['justificativas'])
                
                st.markdown("**Produto/Serviço**")
                st.text(template_data['produto'])
                
                st.markdown("**Stakeholders**")
                st.text(template_data['stakeholders'])
                
                st.markdown("**Premissas**")
                st.text(template_data['premissas'])
                
                st.markdown("**Riscos**")
                st.text(template_data['riscos'])
            
            with cols[1]:
                st.markdown("**Objetivos**")
                st.text(template_data['objetivos'])
                
                st.markdown("**Requisitos**")
                st.text(template_data['requisitos'])
                
                st.markdown("**Entregas**")
                st.text(template_data['entregas'])
                
                st.markdown("**Benefícios**")
                st.text(template_data['beneficios'])
                
                st.markdown("**Restrições**")
                st.text(template_data['restricoes'])

with tab4:
    st.markdown("""
    <div class="guide-section">
        <h2>🎯 O que é o Project Model Canvas?</h2>
        <p>O <strong>Project Model Canvas</strong> é uma ferramenta visual para planejamento de projetos que organiza todos os elementos essenciais em um único quadro.</p>
        <p>Desenvolvido para ser mais ágil que documentos tradicionais, ele ajuda times a:</p>
        <ul>
            <li>Alinhar expectativas entre stakeholders</li>
            <li>Identificar riscos e oportunidades</li>
            <li>Comunicar o projeto de forma clara e objetiva</li>
            <li>Manter o foco nos objetivos estratégicos</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="guide-section">
        <h2>🧩 Áreas do Canvas</h2>
        <p>Cada seção do canvas tem um propósito específico na gestão do projeto:</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("1️⃣ Justificativas", expanded=False):
        st.markdown("""
        **O que incluir:**
        - Problema ou oportunidade que o projeto aborda
        - Razões estratégicas para sua execução
        - Dados e fatos que sustentam a necessidade
        
        **Exemplo prático:**  
        *"Taxa de 30% de evasão no curso online devido à falta de engajamento, com potencial aumento de receita de R$ 500k/ano se resolvido"*
        """)
    
    with st.expander("2️⃣ Pitch do Projeto", expanded=False):
        st.markdown("""
        **Como elaborar:**
        - Frase impactante que resume o projeto
        - Seguir a estrutura:  
          *"Solução X para público Y que resulta em Z"*
        
        **Dica:** Imagine que você tem apenas 30 segundos para explicar seu projeto ao CEO.
        """)
    
    with st.expander("3️⃣ Produto/Serviço", expanded=False):
        st.markdown("""
        **Elementos essenciais:**
        - Principais funcionalidades/características
        - Tecnologias envolvidas
        - Diferenciais competitivos
        
        **Evite:** Listar todos os detalhes técnicos (guarde para documentos específicos)
        """)
    
    # Adicione os outros expanders conforme necessário...
    
    st.markdown("""
    <div class="guide-section">
        <h2>📌 Modelo de Referência</h2>
        <p>Guia rápido para preenchimento:</p>
        
        <table style="width:100%">
            <tr>
                <th>Seção</th>
                <th>Pergunta-Chave</th>
                <th>Boas Práticas</th>
            </tr>
            <tr>
                <td>Justificativas</td>
                <td>Por que fazer este projeto?</td>
                <td>Use dados concretos</td>
            </tr>
            <tr>
                <td>Pitch</td>
                <td>Como explicar em 30 segundos?</td>
                <td>Foco no benefício principal</td>
            </tr>
            <tr>
                <td>Produto</td>
                <td>O que estamos entregando?</td>
                <td>Detalhe apenas features chave</td>
            </tr>
            <tr>
                <td>Stakeholders</td>
                <td>Quem precisa ser envolvido?</td>
                <td>Classifique por influência</td>
            </tr>
        </table>
    </div>
    """, unsafe_allow_html=True)
    
    # Botão para download do PDF
    st.download_button(
        label="📥 Baixar Guia Completo (PDF)",
        data=generate_pdf_guide(),
        file_name="guia_project_canvas_tecvitoria.pdf",
        mime="application/pdf"
    )

# Rodapé
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem;">
    <p>Project Model Canvas - TecVitória © 2024 | Versão 4.0</p>
    <p style="font-size: 0.8rem;">Ferramenta completa para estruturação de projetos</p>
</div>
""", unsafe_allow_html=True)
