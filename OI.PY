# Análise de Dados
def analise_dados():
    st.header("Análise de Dados")

    # Apresentação dos dados e tipos de variáveis
    st.subheader("Visão geral dos dados")
    st.write(df)

    # Explicações sobre os tipos de variáveis
    st.subheader("Tipos de Variáveis")

    st.write("""
    **Qualitativas (ou Categóricas)**:
    - São variáveis que representam categorias ou atributos.
    - **Exemplos**: Seção (como 'Vendas', 'Marketing', 'TI'), Nome.
    - **Tratamento**: Usamos gráficos como **gráficos de barras** ou **gráficos de pizza** para representar essas variáveis.

    **Quantitativas (ou Numéricas)**:
    - São variáveis que representam uma quantidade ou medida numérica.
    - **Exemplos**: Idade, Salário, Experiência.
    - **Tratamento**: Para essas variáveis, utilizamos gráficos como **histogramas**, **boxplots**, ou **gráficos de dispersão**.

    **Qualitativas Ordinais**:
    - São variáveis qualitativas que possuem uma ordem ou hierarquia, mas a diferença entre as categorias não é mensurável.
    - **Exemplos**: Nível de escolaridade (Fundamental, Médio, Superior), avaliação de um produto (Ruim, Regular, Bom, Excelente).
    - **Tratamento**: Assim como as qualitativas, representadas por gráficos de barras, mas com a ênfase na ordem das categorias.

    **Quantitativas Discretas**:
    - São variáveis quantitativas que assumem valores inteiros e contáveis.
    - **Exemplos**: Número de filhos, número de carros em uma garagem.
    - **Tratamento**: Usamos gráficos como **histogramas** ou **gráficos de barras** para representar essas variáveis.

    **Quantitativas Contínuas**:
    - São variáveis que podem assumir qualquer valor dentro de um intervalo e podem ser medidas com alta precisão.
    - **Exemplos**: Altura, peso, temperatura.
    - **Tratamento**: Para essas variáveis, usamos gráficos como **histogramas**, **boxplots** e **gráficos de linha** para ilustrar sua distribuição.
    """)

    # Análise Descritiva
    st.subheader("Estatísticas Descritivas")
    st.write(df.describe())

    # Análise de Dispersão e Correlação
    st.subheader("Correlação entre variáveis")
    corr = df[['Idade', 'Salário', 'Experiência']].corr()
    st.write(corr)

    # Gráfico de correlação
    fig, ax = plt.subplots()  # Criando a figura e os eixos
    sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, ax=ax)  # Passando ax para o gráfico
    st.pyplot(fig)  # Agora, chamamos st.pyplot(fig) passando explicitamente a figura

    # Análise de Distribuições
    st.subheader("Distribuição do Salário")
    fig = px.histogram(df, x="Salário", nbins=10, title="Distribuição do Salário")
    st.plotly_chart(fig)

    # Aplicação de Distribuições Probabilísticas

    # Distribuição Normal (Salário)
    st.subheader("Distribuição Normal - Salário")
    mean = np.mean(df['Salário'])
    std_dev = np.std(df['Salário'])
    st.write(f"Média do Salário: {mean:.2f}, Desvio Padrão: {std_dev:.2f}")
    fig, ax = plt.subplots()  # Criando a figura e os eixos
    sns.histplot(df['Salário'], kde=True, ax=ax)  # Passando ax para o gráfico
    st.pyplot(fig)  # Passando a figura explicitamente

    # Distribuição Poisson (Experiência)
    st.subheader("Distribuição Poisson - Experiência")
    lambda_exp = np.mean(df['Experiência'])
    st.write(f"Lámbda para Experiência: {lambda_exp:.2f}")
    x = np.arange(0, 20)
    poisson_dist = np.random.poisson(lam=lambda_exp, size=1000)
    fig, ax = plt.subplots()  # Criando a figura e os eixos
    ax.hist(poisson_dist, bins=30, density=True, alpha=0.6, color='g')
    st.pyplot(fig)  # Passando a figura explicitamente

    # Gráfico Interativo com Altair
    st.subheader("Análise Interativa de Salário por Seção")
    chart = alt.Chart(df).mark_bar().encode(
        x='Seção:N',
        y='mean(Salário):Q',
        color='Seção:N'
    ).properties(title="Média de Salário por Seção")
    st.altair_chart(chart, use_container_width=True)
