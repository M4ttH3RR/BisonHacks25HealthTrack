import streamlit as st
import os
import matplotlib.pyplot as plt
import pandas as pd

st.title("Julio Felez")

STATIC_PATH = os.path.join(os.getcwd(), 'static')

img_path = os.path.join(STATIC_PATH, "man1.jpg")
st.image(img_path, width=200)


st.write("**Age:** 25 years")
st.write("**Weight:** 160 lbs")
st.write("**Height:** 5'8''")

health_data = [
    {"Timestamp": "2025-03-15 12:00", "User_ID": "001", "Albuminuria": 60, "Serum Creatinine": 1.22, "Uric Acid": 6.7, "Risk Score": 4, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-15 18:00", "User_ID": "001", "Albuminuria": 65, "Serum Creatinine": 1.25, "Uric Acid": 6.8, "Risk Score": 4, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-20 08:00", "User_ID": "001", "Albuminuria": 70, "Serum Creatinine": 1.30, "Uric Acid": 6.9, "Risk Score": 5, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-20 12:00", "User_ID": "001", "Albuminuria": 75, "Serum Creatinine": 1.35, "Uric Acid": 7.0, "Risk Score": 5, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-20 18:00", "User_ID": "001", "Albuminuria": 80, "Serum Creatinine": 1.40, "Uric Acid": 7.2, "Risk Score": 6, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-22 08:00", "User_ID": "001", "Albuminuria": 85, "Serum Creatinine": 1.45, "Uric Acid": 7.4, "Risk Score": 6, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-22 12:00", "User_ID": "001", "Albuminuria": 90, "Serum Creatinine": 1.50, "Uric Acid": 7.5, "Risk Score": 7, "Risk Level": "High Risk - Alert Provider 🚨", "Alert": "Yes"},
]

df = pd.DataFrame(health_data)

st.dataframe(df)

data = {
    "Reading #": list(range(1, 8)),
    "Glucose Reading (mg/dL)": [119, 133, 126, 130, 134, 128, 131]
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