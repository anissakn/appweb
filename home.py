import streamlit as st

# Titre
st.title("Mon formulaire")

# Text
st.write("Ceci est un formulaire de contact")

# Champs de saisie
user_input = st.text_input("Tapez votre texte :")

st.write(user_input)

# Image
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbMZFucLMvnC70v26VRtwnsv73EX8FpKxCqA&s")

# sidebar
st.sidebar.title("Anissa Kone")

# vidéo dans la sidebar
st.sidebar.video("https://www.youtube.com/watch?v=SALF5tOCHLo")

# select bar
student_grad = st.selectbox("Sélectionnez votre niveau d'étude", ["Bac+2", "Bac+3", "Bac+5"])

# select slider
age = st.select_slider("Quel est votre âge ?", range(0,99))

if age > 18:
  st.write("Vous êtes majeur !")
else:
  st.write("Vous êtes mineur !")
