# Para escrever comentários no código usamos o símbolo "#"
# Qualquer coisa escrita em uma linha após esse símbolo não será executada

# Antes do uso de uma biblioteca é necessário importá-la para o código
import streamlit as st
import requests

# Define uma variável para o endereço da API
url = r"https://economia.awesomeapi.com.br/last/"

# Lista de moedas
moedas = ["USD-BRL",
          "EUR-BRL",
          "BTC-BRL"]

# Define um título na tela
st.title("Aula 2: Exemplo 1")

# Variável que guarda temporariamente a moeda escolhida da lista de opções
moeda_escolhida = st.selectbox(label = "Escolha uma moeda", options=moedas)

# Faz a solicitação para a API informando a url e a moeda escolhida
response = requests.get(url+moeda_escolhida)

# Imprime o resultado da requisição
st.header("Resposta da requisição")
st.write(response)

# Imprime o conteúdo do resultado da requisição no formato JSON
st.header("Conteúdo da requisição formatado em JSON")
st.write(response.json())

