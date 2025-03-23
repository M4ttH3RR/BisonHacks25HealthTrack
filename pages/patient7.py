import streamlit as st
import os
import matplotlib.pyplot as plt
import pandas as pd

st.title("Jabari Adebayo")

STATIC_PATH = os.path.join(os.getcwd(), 'static')

img_path = os.path.join(STATIC_PATH, "man4.jpg")
st.image(img_path,width=200)


st.write("**Age:** 63 years")
st.write("**Weight:** 190 lbs")
st.write("**Height:** 5'8''")



df = pd.DataFrame(health_data)

st.dataframe(df)

data = {
    "Reading #": list(range(1, 15)),
    "Glucose Reading (mg/dL)": [112, 138, 114, 121, 137, 124, 127]
}

df = pd.DataFrame(data)

st.table(df)