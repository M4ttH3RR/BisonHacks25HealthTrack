import streamlit as st
import os

st.title("Haley Unandes")

STATIC_PATH = os.path.join(os.getcwd(), 'static')

img_path = os.path.join(STATIC_PATH, "women3.jpg")
st.image(img_path,width=200)

st.write("**Age:** 45 years")
st.write("**Weight:** 180 lbs")
st.write("**Height:** 5'8''")

