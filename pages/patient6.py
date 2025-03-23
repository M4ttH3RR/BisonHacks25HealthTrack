import streamlit as st
import os
import matplotlib.pyplot as plt
import pandas as pd

st.title("Haley Unandes")

STATIC_PATH = os.path.join(os.getcwd(), 'static')

img_path = os.path.join(STATIC_PATH, "women3.jpg")
st.image(img_path,width=200)

st.write("**Age:** 45 years")
st.write("**Weight:** 180 lbs")
st.write("**Height:** 5'8''")



df = pd.DataFrame(health_data)

st.dataframe(df)

data = {
    "Reading #": list(range(1, 15)),
    "Glucose Reading (mg/dL)": [133, 135, 132, 127, 123, 141, 118]
}

df = pd.DataFrame(data)

st.table(df)