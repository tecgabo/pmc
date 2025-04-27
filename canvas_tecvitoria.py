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
SECONDARY_COLOR = "#FF6600"
ACCENT_COLOR = "#00CCCC"
BACKGROUND_COLOR = "#F5F5F5"

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
    .template-card:hover {{
        transform: translateY(-2px);
        transition: transform 0.2s;
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

# Templates atualizados e expandidos
TEMPLATES = {
    "Selecione um template": {k: "" for k in [
        'justificativas', 'pitch', 'produto', 'stakeholders', 'premissas', 'riscos', 
        'objetivos', 'requisitos', 'equipe', 'entregas', 'cronograma', 'beneficios', 
        'restricoes', 'custos']},
    
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
    },
    
    "Implementação de CRM": {
        'justificativas': "• Perda de oportunidades de vendas\n• Inconsistências no desempenho da equipe\n• Dificuldade na previsão de receitas\n• Necessidade de visibilidade do pipeline",
        'pitch': "Implementação de sistema CRM para gestão de vendas B2B, integrado às ferramentas existentes, em 4 meses.",
        'produto': "• Sistema CRM Salesforce implementado\n• Integração com ERP e e-mail\n• Dashboards de vendas\n• Relatórios automatizados",
        'stakeholders': "• Diretoria Comercial\n• Equipe de Vendas (30 usuários)\n• TI\n• Consultoria de implementação",
        'premissas': "• Adesão mínima de 80% da equipe\n• Dados históricos disponíveis\n• Infraestrutura adequada\n• Budget aprovado",
        'riscos': "• Resistência da equipe [Prob: Alta] [Impacto: Alto]\n• Problemas na migração de dados [Prob: Média] [Impacto: Alto]\n• Atrasos na integração [Prob: Média] [Impacto: Médio]",
        'objetivos': "• Implementar em 4 meses\n• 90% de adoção em 60 dias\n• Aumentar taxa de conversão em 20%\n• Reduzir ciclo de vendas em 15%",
        'requisitos': "[MUST] Integração com ERP\n[MUST] Treinamento da equipe\n[SHOULD] Mobile access\n[COULD] IA para previsão de vendas",
        'equipe': "• GP: João Mendes\n• Analista CRM: 2\n• Consultor Salesforce: 1\n• TI: 3 recursos parciais",
        'entregas': "1. CRM configurado\n2. Dados migrados\n3. Equipe treinada\n4. Relatórios customizados\n5. Go-live",
        'cronograma': "• M1: Configuração\n• M2: Migração\n• M3: Treinamento\n• M4: Go-live",
        'beneficios': "• Visibilidade do pipeline\n• Melhor gestão de oportunidades\n• Previsão de receita mais precisa\n• Redução de trabalho manual",
        'restricoes': "• Orçamento: R$ 350k\n• Não pode parar operação atual\n• Deve funcionar em mobile",
        'custos': "• Licenças Salesforce: R$ 180k\n• Consultoria: R$ 120k\n• Treinamento: R$ 50k"
    },
    
    "Projeto de Eficiência Energética": {
        'justificativas': "• Custos com energia aumentaram 40% em 2 anos\n• Oportunidade de redução de custos\n• Compromisso com sustentabilidade\n• Melhoria na imagem corporativa",
        'pitch': "Modernização do sistema de iluminação e climatização para reduzir consumo energético em 30% nas instalações corporativas.",
        'produto': "• Troca de 1.200 lâmpadas por LED\n• Sistema de climatização inteligente\n• Painéis solares no telhado\n• Monitoramento em tempo real",
        'stakeholders': "• Diretoria Financeira\n• Facilities\n• Sustentabilidade\n• Fornecedores de energia\n• Consultoria especializada",
        'premissas': "• Retorno em 3 anos\n• Manutenção da produtividade\n• Linha de financiamento aprovada\n• Espaço adequado para painéis",
        'riscos': "• Atraso na entrega dos materiais [Prob: Média] [Impacto: Alto]\n• Interrupção nas operações [Prob: Baixa] [Impacto: Crítico]\n• Retorno menor que o esperado [Prob: Baixa] [Impacto: Alto]",
        'objetivos': "• Reduzir consumo em 30% em 12 meses\n• ROI em 36 meses\n• Certificação LEED Silver\n• Zero interrupções nas operações",
        'requisitos': "[MUST] Manter níveis de iluminância\n[MUST] Integração com sistema existente\n[SHOULD] Controle individual por área\n[COULD] Geração de relatórios automáticos",
        'equipe': "• GP: Maria Oliveira\n• Engenheiro Elétrico: 1\n• Técnicos: 4\n• Consultor LEED: 1",
        'entregas': "1. Diagnóstico energético\n2. Projeto executivo\n3. Implantação completa\n4. Treinamento da equipe\n5. Relatório final",
        'cronograma': "• M1-2: Diagnóstico\n• M3-4: Projeto\n• M5-8: Implantação\n• M9: Ajustes",
        'beneficios': "• Economia anual de R$ 480k\n• Redução de pegada de carbono\n• Melhor ambiente de trabalho\n• Diferencial competitivo",
        'restricoes': "• Orçamento: R$ 1.2M\n• Não pode interferir nas operações\n• Prazo: 9 meses",
        'custos': "• Materiais: R$ 800k\n• Mão de obra: R$ 300k\n• Consultoria: R$ 100k"
    }
}

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
    st.image("https://tecvitoria.com.br/wp-content/uploads/2022/03/logo-tecvitoria-horizontal.png", width=200)
    st.markdown("### Informações Básicas")
    
    st.session_state.dados['nome_projeto'] = st.text_input(
        "Nome do Projeto*",
        value=st.session_state.dados['nome_projeto']
    )
    
    st.session_state.dados['responsavel'] = st.text_input(
        "Responsável*",
        value=st.session_state.dados['responsavel']
    )
    
    data_input = st.date_input(
        "Data*", 
        datetime.datetime.strptime(st.session_state.dados['data'], "%d/%m/%Y").date()
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
tab1, tab2, tab3 = st.tabs(["📝 Formulário", "🖼️ Visualizar Canvas", "📚 Templates"])

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

# Rodapé
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem;">
    <p>Project Model Canvas - TecVitória © 2024 | Versão 3.0</p>
    <p style="font-size: 0.8rem;">Ferramenta para estruturação de projetos</p>
</div>
""", unsafe_allow_html=True)
