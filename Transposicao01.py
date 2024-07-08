# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 19:29:39 2024

@author: ASGUNZI
"""


import streamlit as st

from math import ceil

def cifraTransposicao(mensagem,nlinhas):
    #O texto é escrito por colunas, em n linhas, e a mensagem é transmitida por linhas
    
    mensagem = mensagem.replace(" ", "_") #Substitui espaço por underline
    tamanho = ceil(len(mensagem)/nlinhas)
    outstr =""    
    for i in range(nlinhas):
        linha= mensagem[i::nlinhas]
        
        #Completa com _ se não tiver informação 
        linha += "_" if len(linha)<tamanho else ""
        
        outstr += linha
    
    return outstr 
  

def decifraTransposicao(mensagem,nlinhas):
#Decifra código de transposicao. O texto é escrito por colunas, em n linhas, e a mensagem é transmitida por linhas    
    tamanho = int(len(mensagem)/nlinhas)
    
    outstr =""    
    
    for i in range(tamanho):
        linha= mensagem[i::tamanho]
        
        outstr += linha
    
    return outstr 

#-------------------------------------
#Sidebar menu
st.sidebar.title("Menu")

st.sidebar.markdown("[Home](https://asgunzi.neocities.org)")

st.sidebar.markdown("[Cifra de César](https://cesarsimples.streamlit.app/)")
st.sidebar.markdown("[Cifra Polialfabética](https://polialfa01py-bdaxz4f6ehzi38ehcg8ndp.streamlit.app/)")
st.sidebar.markdown("[Cifra Transposição](https://cifratransposicao.streamlit.app/)")
#-------------------------------------


st.image("https://ideiasesquecidas.com/wp-content/uploads/2024/07/forgottenmath.png")
st.title("Exemplo - Cifra de Transposição")

col1, col2, col3 = st.columns([1, 2, 2])

with col1:
    nlinhas = int( st.text_input("Núm de linhas: ", value = 5))


user_input = st.text_input("Entre texto a cifrar:")

# Check if the input is not empty
if user_input:
    # Cifrar mensagem
    msgCifrada = cifraTransposicao(user_input, nlinhas)
    
    # Display the reversed text
    st.write("Mensagem cifrada:")
    st.write(msgCifrada)
    
#Marca separatória
st.markdown("---")

user_input2 = st.text_input("Entre texto a decifrar:")

# Check if the input is not empty
if user_input2:
    # Decifrar mensagem

    msgDecifrada= decifraTransposicao(user_input2, nlinhas)
    
    # Display the reversed text
    st.write("Mensagem decifrada:")
    st.write(msgDecifrada)
    
    
