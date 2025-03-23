import streamlit as st
import os
import matplotlib.pyplot as plt

st.title("Julio Felez")

STATIC_PATH = os.path.join(os.getcwd(), 'static')

img_path = os.path.join(STATIC_PATH, "man1.jpg")
st.image(img_path, width=200)


st.write("**Age:** 25 years")
st.write("**Weight:** 160 lbs")
st.write("**Height:** 5'8''")

value = 83
fig, ax = plt.subplots(figsize=(1, 1))
wedges, _ = ax.pie(
    [value, 100 - value],
    colors=["#1f77b4", "#d3d3d3"],
    startangle=90,
)

ax.text(
    0, 0,
    f"{5}",
    ha="center",
    va="center",
    fontsize=7,
    fontweight="bold",
)

ax.axis("equal")

st.pyplot(fig)