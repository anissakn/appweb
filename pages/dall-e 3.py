import streamlit as st

st.title("Dall-e 3")

# Champs de saisie
user_input = st.text_input("Veuillez entrer une description de l'image que vous souhaitez générer :")

st.write(user_input)

# sidebar
st.sidebar.text_input("Veuillez entrer la clé OpenIA")

# OpenAI pour générer des images
from openai import OpenAI


client = OpenAI(api_key=sk-6uxlenvrwsRO0NlIgqhrg2B-avWNwVlPV8MgbU-QSHT3BlbkFJSc_Lmu6ZS06yDsSmP4kvVEd42Ds95-CXp726oavJMA)




image = client.images.generate(
    model="dall-e-2",
    prompt=prompt,
    size="512x512",
    quality="standard",
    n=1,
)

image_url = image.data[0].url
print(image_url)
