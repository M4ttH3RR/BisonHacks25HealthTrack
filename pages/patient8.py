import streamlit as st
import os

st.title("Lei Keita")

STATIC_PATH = os.path.join(os.getcwd(), 'static')

img_path = os.path.join(STATIC_PATH, "woman4.jpg")
st.image(img_path, width=200)

st.write("**Age:** 23 years")
st.write("**Weight:** 164 lbs")
st.write("**Height:** 6'0''")

