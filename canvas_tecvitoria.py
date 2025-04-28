# Adicione esta nova aba ao final do código, junto com as outras abas (tab1, tab2, tab3)

tab4 = st.tabs(["📚 Guia do Canvas"])

with tab4:
    st.markdown("""
    ## 🎯 O que é o Project Model Canvas?
    
    O **Project Model Canvas** é uma ferramenta visual para planejamento de projetos que organiza todos os elementos essenciais em um único quadro. 
    Desenvolvido para ser mais ágil que documentos tradicionais, ele ajuda times a:
    
    - Alinhar expectativas
    - Identificar riscos e oportunidades
    - Comunicar o projeto de forma clara
    - Manter o foco nos objetivos estratégicos
    
    *"Um quadro vale mais que mil planilhas"* - Adaptado do princípio da Gestão Visual
    """)
    
    st.image("https://miro.medium.com/v2/resize:fit:1400/format:webp/1*QYw4YcKQ5Z-5X5Q5Q5Q5Qw.png", 
             caption="Exemplo de Project Model Canvas preenchido", width=600)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🧩 Detalhamento das Áreas do Canvas
    
    Cada seção do canvas tem um propósito específico na gestão do projeto:
    """)
    
    with st.expander("1️⃣ **Justificativas**", expanded=False):
        st.markdown("""
        **O que incluir:**
        - Problema ou oportunidade que o projeto aborda
        - Razões estratégicas para sua execução
        - Dados e fatos que sustentam a necessidade
        
        **Exemplo prático:**  
        *"Taxa de 30% de evasão no curso online devido à falta de engajamento, com potencial aumento de receita de R$ 500k/ano se resolvido"*
        """)
    
    with st.expander("2️⃣ **Pitch do Projeto**", expanded=False):
        st.markdown("""
        **Como elaborar:**
        - Frase impactante que resume o projeto
        - Seguir a estrutura:  
          *"Solução X para público Y que resulta em Z"*
        
        **Dica:** Imagine que você tem apenas 30 segundos para explicar seu projeto ao CEO.
        """)
    
    with st.expander("3️⃣ **Produto/Serviço**", expanded=False):
        st.markdown("""
        **Elementos essenciais:**
        - Principais funcionalidades/características
        - Tecnologias envolvidas
        - Diferenciais competitivos
        
        **Evite:** Listar todos os detalhes técnicos (guarde para documentos específicos)
        """)
    
    with st.expander("4️⃣ **Stakeholders**", expanded=False):
        st.markdown("""
        **Classificação útil:**
        ```mermaid
        graph LR
        A[Stakeholders] --> B[Tomadores de decisão]
        A --> C[Influenciadores]
        A --> D[Executores]
        A --> E[Beneficiários]
        A --> F[Afetados]
        ```
        **Priorize:** Mapeie poder x interesse usando matriz RACI
        """)
    
    with st.expander("5️⃣ **Premissas**", expanded=False):
        st.markdown("""
        **Boas práticas:**
        - Liste apenas premissas críticas (5-7 no máximo)
        - Classifique por:  
          ✅ Confirmadas  
          ⚠️ A validar  
          ❌ Arriscadas
        
        **Exemplo válido:**  
        *"A equipe de desenvolvimento permanecerá alocada pelo menos 50% do tempo"*
        """)
    
    with st.expander("6️⃣ **Riscos**", expanded=False):
        st.markdown("""
        **Matriz de avaliação:**
        | Probabilidade | Impacto Baixo | Impacto Médio | Impacto Alto |
        |---------------|---------------|---------------|--------------|
        | Alta          | Monitorar     | Mitigar       | Evitar       |
        | Média         | Aceitar       | Mitigar       | Mitigar      |
        | Baixa         | Aceitar       | Monitorar     | Transferir   |
        
        **Formato sugerido:**  
        *"Descrição do risco [Prob: Alta/Média/Baixa] [Impacto: Crítico/Alto/Médio/Baixo] - Ação de mitigação"*
        """)
    
    with st.expander("7️⃣ **Objetivos**", expanded=False):
        st.markdown("""
        **Use critérios SMART:**
        - **S**pecífico  
        - **M**ensurável  
        - **A**tingível  
        - **R**elevante  
        - **T**emporal
        
        **Exemplo bom:**  
        *"Reduzir tempo de processamento de pedidos de 48h para 24h até Q3/2024"*
        """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 📌 Modelo de Referência
    
    | Seção            | Pergunta-Chave                  | Boas Práticas                      |
    |------------------|---------------------------------|------------------------------------|
    | Justificativas   | Por que fazer este projeto?     | Use dados concretos               |
    | Pitch           | Como explicar em 30 segundos?   | Foco no benefício principal       |
    | Produto         | O que estamos entregando?       | Detalhe apenas features chave     |
    | Stakeholders    | Quem precisa ser envolvido?     | Classifique por influência        |
    """)
    
    st.download_button(
        label="📥 Baixar Guia Completo (PDF)",
        data=generate_pdf_guide(),  # Função hipotética para gerar PDF
        file_name="guia_project_canvas.pdf",
        mime="application/pdf"
    )
