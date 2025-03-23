import streamlit as st
import os
import matplotlib.pyplot as plt
import pandas as pd

st.title("Zia Abiodun")

STATIC_PATH = os.path.join(os.getcwd(), 'static')

img_path = os.path.join(STATIC_PATH, "woman2.jpg")
st.image(img_path, width=200)


st.write("**Age:** 23 years")
st.write("**Weight:** 140 lbs")
st.write("**Height:** 5'5''")

health_data = [  {"Timestamp": "2025-03-01 08:00", "User_ID": "002", "Albuminuria": 30, "Serum Creatinine": 0.90, "Uric Acid": 5.4, "Risk Score": 2, "Risk Level": "Low Risk", "Alert": "No"},
    {"Timestamp": "2025-03-01 12:00", "User_ID": "002", "Albuminuria": 38, "Serum Creatinine": 1.00, "Uric Acid": 5.8, "Risk Score": 3, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-01 18:00", "User_ID": "002", "Albuminuria": 42, "Serum Creatinine": 1.08, "Uric Acid": 6.1, "Risk Score": 3, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-08 08:00", "User_ID": "002", "Albuminuria": 52, "Serum Creatinine": 1.18, "Uric Acid": 6.6, "Risk Score": 4, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-08 12:00", "User_ID": "002", "Albuminuria": 60, "Serum Creatinine": 1.22, "Uric Acid": 6.9, "Risk Score": 5, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-08 18:00", "User_ID": "002", "Albuminuria": 68, "Serum Creatinine": 1.30, "Uric Acid": 7.4, "Risk Score": 6, "Risk Level": "High Risk - Alert Provider 🚨", "Alert": "Yes"},
    {"Timestamp": "2025-03-15 08:00", "User_ID": "002", "Albuminuria": 80, "Serum Creatinine": 1.45, "Uric Acid": 7.8, "Risk Score": 7, "Risk Level": "High Risk - Alert Provider 🚨", "Alert": "Yes"},
]

df = pd.DataFrame(health_data)

st.dataframe(df)


data = {
    "Reading #": list(range(1, 8)),
    "Glucose Reading (mg/dL)": [121, 118, 118, 141, 137, 113, 130]
}

df = pd.DataFrame(data)

st.table(df)

value = 100
fig, ax = plt.subplots(figsize=(3, 3), dpi=150)
wedges, _ = ax.pie(
    [value, 100 - value],
    colors = ["#FF0000", "#d3d3d3"],
    startangle=90,
    radius=0.05
)

ax.text(
    0, 0,
    f"{7}",
    ha="center",
    va="center",
    fontsize=10,
    fontweight="bold",
)

ax.axis("equal")

st.pyplot(fig)