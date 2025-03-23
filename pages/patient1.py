import streamlit as st
import os

st.title("Julio Felez")

STATIC_PATH = os.path.join(os.getcwd(), 'static')

img_path = os.path.join(STATIC_PATH, "man1.jpg")
st.image(img_path, width=200)


st.write("**Age:** 25 years")
st.write("**Weight:** 160 lbs")
st.write("**Height:** 5'8''")
