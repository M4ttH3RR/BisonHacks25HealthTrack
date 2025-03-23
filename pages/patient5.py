import streamlit as st
import os
import matplotlib.pyplot as plt
import pandas as pd

st.title("Kofi Anderson")

STATIC_PATH = os.path.join(os.getcwd(), 'static')

img_path = os.path.join(STATIC_PATH, "man3.jpg")
st.image(img_path,width=200)


st.write("**Age:** 45 years")
st.write("**Weight:** 182 lbs")
st.write("**Height:** 6'2''")



df = pd.DataFrame(health_data)

st.dataframe(df)

data = {
    "Reading #": list(range(1, 15)),
    "Glucose Reading (mg/dL)": [106, 122, 125, 136, 144, 130, 124]
}

df = pd.DataFrame(data)

st.table(df)