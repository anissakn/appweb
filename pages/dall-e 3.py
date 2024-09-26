import streamlit as st

st.title("Dall-e 3")

# Champs de saisie
user_input = st.text_input("Veuillez entrer une description de l'image que vous souhaitez générer :")

st.write(user_input)

# sidebar
st.sidebar.text_input("Veuillez entrer la clé OpenIA")
