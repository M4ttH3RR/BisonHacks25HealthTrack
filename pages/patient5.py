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

health_data = [
    {"Timestamp": "2025-03-01 08:00", "User_ID": "005", "Albuminuria": 30, "Serum Creatinine": 0.90, "Uric Acid": 5.4, "Risk Score": 2, "Risk Level": "Low Risk", "Alert": "No"},
    {"Timestamp": "2025-03-01 12:00", "User_ID": "005", "Albuminuria": 38, "Serum Creatinine": 0.96, "Uric Acid": 5.7, "Risk Score": 2, "Risk Level": "Low Risk", "Alert": "No"},
    {"Timestamp": "2025-03-01 18:00", "User_ID": "005", "Albuminuria": 42, "Serum Creatinine": 0.98, "Uric Acid": 5.9, "Risk Score": 2, "Risk Level": "Low Risk", "Alert": "No"},
    {"Timestamp": "2025-03-08 08:00", "User_ID": "005", "Albuminuria": 45, "Serum Creatinine": 1.00, "Uric Acid": 6.0, "Risk Score": 2, "Risk Level": "Low Risk", "Alert": "No"},
    {"Timestamp": "2025-03-08 12:00", "User_ID": "005", "Albuminuria": 50, "Serum Creatinine": 1.02, "Uric Acid": 6.1, "Risk Score": 2, "Risk Level": "Low Risk", "Alert": "No"},
    {"Timestamp": "2025-03-08 18:00", "User_ID": "005", "Albuminuria": 55, "Serum Creatinine": 1.05, "Uric Acid": 6.3, "Risk Score": 2, "Risk Level": "Low Risk", "Alert": "No"},
    {"Timestamp": "2025-03-15 08:00", "User_ID": "005", "Albuminuria": 60, "Serum Creatinine": 1.08, "Uric Acid": 6.5, "Risk Score": 2, "Risk Level": "Low Risk", "Alert": "No"},
]

df = pd.DataFrame(health_data)

st.dataframe(df)

data = {
    "Reading #": list(range(1, 8)),
    "Glucose Reading (mg/dL)": [106, 122, 125, 136, 144, 130, 124]
}

df = pd.DataFrame(data)

st.table(df)


value = 29
fig, ax = plt.subplots(figsize=(3, 3), dpi=150)
wedges, _ = ax.pie(
    [value, 100 - value],
    colors = ["#008000", "#d3d3d3"],
    startangle=90,
    radius=0.05
)

ax.text(
    0, 0,
    f"{2}",
    ha="center",
    va="center",
    fontsize=10,
    fontweight="bold",
)

ax.axis("equal")

st.pyplot(fig)