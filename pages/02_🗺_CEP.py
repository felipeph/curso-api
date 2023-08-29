# Importa a biblioteca do streamlit para renderizar a página
import streamlit as st

# Importa a biblioteca requests para fazer consulta à API
import requests

# Variável que define a URL de consulta da API
url = r'https://cep.awesomeapi.com.br/json/'

# Variável que guarda o valor digitado pelo usuário na caixa de entrada
cep = st.text_input("Número do CEP")

# Variável que guarda o resultado da solicitação da API
result = requests.get(url+cep)

# Exibe o resultado da requisição
st.header("Resultado da requisição")
st.write(result)

# Exibe o conteúdo do resultado da requisição
st.header("Conteúdo da requisição em formato JSON")
st.write(result.json())