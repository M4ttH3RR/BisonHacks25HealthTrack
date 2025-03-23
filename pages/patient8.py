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

health_data = [
    {"Timestamp": "2025-03-01 08:00", "User_ID": "008", "Albuminuria": 35, "Serum Creatinine": 1.00, "Uric Acid": 5.6, "Risk Score": 3, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-01 12:00", "User_ID": "008", "Albuminuria": 38, "Serum Creatinine": 1.05, "Uric Acid": 5.8, "Risk Score": 3, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-01 18:00", "User_ID": "008", "Albuminuria": 42, "Serum Creatinine": 1.08, "Uric Acid": 6.1, "Risk Score": 3, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-08 08:00", "User_ID": "008", "Albuminuria": 47, "Serum Creatinine": 1.12, "Uric Acid": 6.3, "Risk Score": 4, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-08 12:00", "User_ID": "008", "Albuminuria": 50, "Serum Creatinine": 1.15, "Uric Acid": 6.5, "Risk Score": 5, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-08 18:00", "User_ID": "008", "Albuminuria": 60, "Serum Creatinine": 1.22, "Uric Acid": 6.8, "Risk Score": 6, "Risk Level": "High Risk - Alert Provider 🚨", "Alert": "Yes"},
    {"Timestamp": "2025-03-15 08:00", "User_ID": "008", "Albuminuria": 70, "Serum Creatinine": 1.30, "Uric Acid": 7.1, "Risk Score": 7, "Risk Level": "High Risk - Alert Provider 🚨", "Alert": "Yes"},
]

df = pd.DataFrame(health_data)

st.dataframe(df)

data = {
    "Reading #": list(range(1, 8)),
    "Glucose Reading (mg/dL)": [130, 147, 117, 133, 128, 140, 134]
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