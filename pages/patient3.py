import streamlit as st
import os


st.title("Aaliyah Johnson")


STATIC_PATH = os.path.join(os.getcwd(), 'static')


img_path = os.path.join(STATIC_PATH, "woman1.jpg")
st.image(img_path, width=200)


st.write("**Age:** 56 years")
st.write("**Weight:** 189 lbs")
st.write("**Height:** 5'6''")

