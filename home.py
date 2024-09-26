import streamlit as st

# Titre
st.title("Mon formulaire")

# Text
st.write("Ceci est un formulaire de contact")

# Champs de saisie
user_input = st.text_input("Tapez votre texte :")

st.write(user_input)
