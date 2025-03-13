import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import altair as alt
import matplotlib.pyplot as plt


st.set_page_config(page_title="Dashboard Profissional", page_icon=":bar_chart:", layout="wide")


st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #1e3a5f, #2a4f71);  /* Azul mais escuro */
        color: white;
    }
    h1, h2 {
        font-family: 'Helvetica', sans-serif;
        color: #FF5733;
    }
    .stButton>button {
        background-color: #E67E22;
        color: white;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)


def load_data():
    np.random.seed(0)
    data = {
        'Nome': ['Ana', 'Lucas', 'Maria', 'João', 'Carlos', 'Fernanda', 'Rafael', 'Beatriz', 'Vinícius', 'Patrícia'],
        'Idade': np.random.randint(20, 50, 10),
        'Salário': np.random.randint(3000, 10000, 10),
        'Experiência': np.random.randint(1, 15, 10),
        'Seção': ['Vendas', 'Marketing', 'TI', 'Vendas', 'TI', 'Marketing', 'Vendas', 'TI', 'Marketing', 'Vendas'],
    }
    df = pd.DataFrame(data)
    return df


df = load_data()


def home():
    st.title("Dashboard Profissional - Kaio Meireles")
    st.header("Objetivo Profissional")
    st.write("""
        Ter uma carreira sólida no ramo de TI, viver de home office e trabalhar de casa pro resto da vida. 
        Ficar longe dos perigos noturnos. <3
    """)
    st.subheader("Minha Foto")
    st.image("Image.jpg", caption="Kaio Meireles", use_container_width=True) 
    st.header("Objetivo Profissional")
    st.write("""
        Sou Kaio Meireles, um estudante de Engenharia de Software apaixonado por TI e pela inovação constante que o campo oferece. 
        Meu objetivo é construir uma carreira sólida no setor, com foco em home office, permitindo-me trabalhar remotamente e buscar a liberdade de horários, sem abrir mão da qualidade de vida e da segurança.
        
        Neste dashboard, você encontrará uma visão detalhada da minha trajetória acadêmica e profissional, minhas habilidades técnicas e interpessoais, além de uma análise de dados aplicada a um contexto profissional.
        
        O conteúdo está estruturado da seguinte maneira:
        - **Home**: Introdução ao meu perfil profissional e objetivos de carreira.
        - **Formação e Experiência**: Detalhes sobre a minha jornada educacional e experiência prática.
        - **Skills**: Habilidades técnicas e soft skills que me permitem entregar resultados de forma eficaz e eficiente.
        - **Análise de Dados**: Uma análise aprofundada de dados, aplicando distribuições probabilísticas para resolver problemas práticos e fornecer insights valiosos.
        
        Explore as seções para saber mais sobre o meu perfil e veja como a análise de dados pode ser uma ferramenta poderosa na solução de problemas complexos no mercado de TI!
    """)

def formacao_experiencia():
    st.header("Formação e Experiência")
    st.write("Formação Acadêmica:")
    st.write("- Engenharia de Software (2º ano, FIAP)")
    st.write("- Curso de Portaria (EMFORVIGIL)")
    st.write("Experiência Profissional:")
    st.write("- Motorista de PetShop por 2 meses")
    st.write("- 2 anos com Audiovisual (VMix, OBS, etc.)")
    st.write("- 1 ano e 1 mês em Marketing, focado no ramo ótico (Sites, Edição de Vídeo, Cardápios, Tabelas, etc.)")
    st.write("Certificações:")
    st.write("- Não possui certificações específicas no momento")


def skills():
    st.header("Skills")
    st.write("Tecnologias e Ferramentas:")
    st.write("- VSCode, PyCharm, BrModelo")
    st.write("- Básico em ferramentas de desenvolvimento e edição que vejo na faculdade")
    st.write("Soft Skills (sugestão):")
    st.write("- Comunicação eficaz")
    st.write("- Trabalho em equipe")
    st.write("- Criatividade e resolução de problemas")
    st.write("- Adaptabilidade ao ambiente remoto e home office")
    st.write("- Organização e gestão de tempo")


def analise_dados():
    st.header("Análise de Dados")

    
    st.subheader("Visão geral dos dados")
    st.write(df)

    
    st.subheader("Estatísticas Descritivas")
    st.write(df.describe())

    
    st.subheader("Correlação entre variáveis")
    corr = df[['Idade', 'Salário', 'Experiência']].corr()
    st.write(corr)

    
    fig, ax = plt.subplots()  
    sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, ax=ax)  
    st.pyplot(fig)  

    
    st.subheader("Distribuição do Salário")
    fig = px.histogram(df, x="Salário", nbins=10, title="Distribuição do Salário")
    st.plotly_chart(fig)

   

    
    st.subheader("Distribuição Normal - Salário")
    mean = np.mean(df['Salário'])
    std_dev = np.std(df['Salário'])
    st.write(f"Média do Salário: {mean:.2f}, Desvio Padrão: {std_dev:.2f}")
    fig, ax = plt.subplots()  
    sns.histplot(df['Salário'], kde=True, ax=ax)  
    st.pyplot(fig)  

    
    st.subheader("Distribuição Poisson - Experiência")
    lambda_exp = np.mean(df['Experiência'])
    st.write(f"Lámbda para Experiência: {lambda_exp:.2f}")
    x = np.arange(0, 20)
    poisson_dist = np.random.poisson(lam=lambda_exp, size=1000)
    fig, ax = plt.subplots()  
    ax.hist(poisson_dist, bins=30, density=True, alpha=0.6, color='g')
    st.pyplot(fig)  

    
    st.subheader("Análise Interativa de Salário por Seção")
    chart = alt.Chart(df).mark_bar().encode(
        x='Seção:N',
        y='mean(Salário):Q',
        color='Seção:N'
    ).properties(title="Média de Salário por Seção")
    st.altair_chart(chart, use_container_width=True)


def filtro_interativo():
    st.sidebar.header("Filtros Interativos")
    
    section = st.sidebar.radio(
        "Escolha a Seção para exibir:",
        ('Home', 'Formação e Experiência', 'Skills', 'Análise de Dados')
    )
    
    if section == 'Home':
        home()
    elif section == 'Formação e Experiência':
        formacao_experiencia()
    elif section == 'Skills':
        skills()
    elif section == 'Análise de Dados':
        analise_dados()


def foto_logo():
    st.sidebar.header("Foto e Logo")
    st.sidebar.write("Espaço para logo e foto")
    st.sidebar.image("km.svg", caption="Sua Foto Aqui", use_container_width=True)  
    st.sidebar.write("Espaço para logo da empresa ou pessoal")  


def rodape():
    st.markdown("""
        <footer style="text-align: center; font-size: 12px; color: gray;">
        Desenvolvido por Kaio Meireles - Dashboard Profissional
        </footer>
    """, unsafe_allow_html=True)


def main():
    filtro_interativo()
    foto_logo() 
    rodape()

if __name__ == "__main__":
    main()
