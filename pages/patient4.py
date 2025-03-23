import streamlit as st
import os

st.title("Zia Abiodun")

STATIC_PATH = os.path.join(os.getcwd(), 'static')

img_path = os.path.join(STATIC_PATH, "woman2.jpg")
st.image(img_path, width=200)


st.write("**Age:** 23 years")
st.write("**Weight:** 140 lbs")
st.write("**Height:** 5'5''")
