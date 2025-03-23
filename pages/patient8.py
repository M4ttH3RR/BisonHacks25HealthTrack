import streamlit as st
import os
import matplotlib.pyplot as plt
import pandas as pd

st.title("Lei Keita")

STATIC_PATH = os.path.join(os.getcwd(), 'static')

img_path = os.path.join(STATIC_PATH, "woman4.jpg")
st.image(img_path, width=200)

st.write("**Age:** 23 years")
st.write("**Weight:** 164 lbs")
st.write("**Height:** 6'0''")


df = pd.DataFrame(health_data)

st.dataframe(df)

data = {
    "Reading #": list(range(1, 15)),
    "Glucose Reading (mg/dL)": [130, 147, 117, 133, 128, 140, 134]
}

df = pd.DataFrame(data)

st.table(df)