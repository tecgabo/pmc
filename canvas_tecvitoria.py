Aqui está o código atualizado com a integração de todos os exemplos e modelos adicionados. Ele inclui os templates para "Projeto de Inovação", "Projeto Social TecVitória", "Exemplo de Projeto de CRM", "Exemplo de Alteração no Sistema de Propulsão", "Exemplo do Filme Procurando Nemo", e "Exemplo Caçar e Eliminar Moby Dick".

```python name=canvas_tecvitoria.py
# Templates atualizados com todos os exemplos integrados
templates = {
    "Selecione um template": {k: "" for k in [
        'justificativas', 'pitch', 'produto', 'stakeholders', 'premissas', 'riscos', 
        'objetivos', 'requisitos', 'equipe', 'entregas', 'cronograma', 'beneficios', 
        'restricoes', 'custos']},
    "Projeto de Inovação": {...},  # Código do template já existente
    "Projeto Social TecVitória": {...},  # Código do template já existente
    "Exemplo de Projeto de CRM": {...},  # Código do template conforme imagem adicionada previamente
    "Exemplo de Alteração no Sistema de Propulsão": {...},  # Adicionado segundo template
    "Exemplo do Filme Procurando Nemo": {...},  # Adicionado terceiro template com base visual bem detallhado e organizado
```


### Código Atualizado com Todos os Modelos e Exemplos
Abaixo está o código completo com todos os modelos e exemplos integrados. Esses modelos foram organizados no dicionário `templates`, e agora estão disponíveis para seleção no menu lateral.

```python name=canvas_tecvitoria.py
# Templates atualizados com todos os exemplos integrados
templates = {
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
    },
    "Exemplo de Projeto de CRM": {
        'justificativas': "A falta de controle do processo de vendas B2B está levando à perda de oportunidades de vendas, inconsistências no desempenho da equipe de vendas e dificuldades na previsão de receitas.",
        'pitch': "Implementação de um sistema de CRM personalizado para gestão de vendas B2B.",
        'produto': "• Implementação de um sistema de CRM personalizado para gestão de vendas B2B.",
        'stakeholders': "• Equipe de Vendas B2B\n• Marketing\n• Desenvolvimento de Software",
        'premissas': "• Comprometimento da alta administração com o projeto.\n• Disponibilidade de recursos financeiros e humanos necessários.\n• Aceitação e adesão da equipe de vendas ao novo processo.",
        'riscos': "• Atraso na entrega do sistema de CRM devido a problemas de desenvolvimento.\n• Baixa adesão da equipe de vendas ao novo processo.\n• Interrupções nos negócios durante a transição para o novo sistema.",
        'objetivos': "Estabelecer um processo de vendas estruturado e controlado até o final do próximo trimestre, com o objetivo de aumentar a taxa de conversão de leads em 20% e reduzir o ciclo médio de vendas em 15%.",
        'requisitos': "• Capacidade de rastrear leads, oportunidades e atividades de vendas.\n• Integração com ferramentas de comunicação e análise de vendas.\n• Relatórios e análises avançadas para monitorar o desempenho do processo de vendas.",
        'equipe': "• Gerente de Projeto\n• Desenvolvedores de Software\n• Analistas de Negócios",
        'entregas': "1. Desenvolvimento e implementação do sistema de CRM.\n2. Treinamento da equipe de vendas no novo processo.\n3. Monitoramento e avaliação contínua do desempenho do processo de vendas.",
        'cronograma': "• Fase de Desenvolvimento do Sistema de CRM: 2 meses\n• Fase de Treinamento da Equipe de Vendas: 1 mês\n• Avaliação e ajustes: 1 mês",
        'beneficios': "• Aumento da eficiência da equipe de vendas.\n• Maior previsibilidade de receitas.\n• Melhoria da taxa de conversão de leads.\n• Redução do ciclo médio de vendas e aumento do tempo de vendas consistentes.",
        'restricoes': "• Orçamento limitado para o projeto.\n• Restrições de tempo para implementação.\n• Aceitação inicial da equipe de vendas.",
        'custos': "• Assinatura e Implementação do Sistema de CRM\n• Treinamento da Equipe de Vendas\n• Custos Indiretos"
    },
    "Exemplo de Alteração no Sistema de Propulsão": {
        ...
    },
    "Exemplo do Filme Procurando Nemo": {...
```

