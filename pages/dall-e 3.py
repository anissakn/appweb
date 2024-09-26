import streamlit as st

st.title("Dall-e 3")

# Champs de saisie
user_input = st.text_input("Donnez votre nom et prénom :")

st.write(user_input)
