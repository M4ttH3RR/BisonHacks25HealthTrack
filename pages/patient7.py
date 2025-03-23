import streamlit as st
import os

st.title("Jabari Adebayo")

STATIC_PATH = os.path.join(os.getcwd(), 'static')

img_path = os.path.join(STATIC_PATH, "man4.jpg")
st.image(img_path,width=200)


st.write("**Age:** 63 years")
st.write("**Weight:** 190 lbs")
st.write("**Height:** 5'8''")

