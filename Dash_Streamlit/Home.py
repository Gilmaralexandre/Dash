import streamlit as st


st.sidebar.markdown(
    'Dashboard')

st.markdown('# Bem-vindo ao Analisador de Vendas')

st.divider()

st.markdown(
    '''
    Esse projeto foi desenvolvido como projeto final do curso ***Python para Usuários de Excel***.

    Utilizaremos três principais bibliotecas para o seu desenvolvimento:

    - `pandas`: para manipulação de dados em tabelas
    - `plotly`: para geração de gráficos
    - `streamlit`: para criação desse webApp interativo que você se encontra nesse momento

    Os dados utilizados foram gerados pelo script 'gerador_de_vendas.py' que se encontra junto do código fonte do projeto. Os dados podem ser visualizados na aba de tabelas!

    .
    '''
)
