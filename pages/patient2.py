import streamlit as st
import os

st.title("John Lewis")

STATIC_PATH = os.path.join(os.getcwd(), 'static')

img_path = os.path.join(STATIC_PATH, "man2.jpg")
st.image(img_path, width=200)


st.write("**Age:** 31 years")
st.write("**Weight:** 182 lbs")
st.write("**Height:** 6'2''")

