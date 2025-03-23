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

health_data = [
    {"Timestamp": "2025-03-01 08:00", "User_ID": "007", "Albuminuria": 32, "Serum Creatinine": 0.95, "Uric Acid": 5.5, "Risk Score": 2, "Risk Level": "Low Risk", "Alert": "No"},
    {"Timestamp": "2025-03-01 12:00", "User_ID": "007", "Albuminuria": 35, "Serum Creatinine": 1.00, "Uric Acid": 5.7, "Risk Score": 2, "Risk Level": "Low Risk", "Alert": "No"},
    {"Timestamp": "2025-03-01 18:00", "User_ID": "007", "Albuminuria": 38, "Serum Creatinine": 1.05, "Uric Acid": 5.9, "Risk Score": 2, "Risk Level": "Low Risk", "Alert": "No"},
    {"Timestamp": "2025-03-08 08:00", "User_ID": "007", "Albuminuria": 43, "Serum Creatinine": 1.12, "Uric Acid": 6.1, "Risk Score": 3, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-08 12:00", "User_ID": "007", "Albuminuria": 46, "Serum Creatinine": 1.15, "Uric Acid": 6.3, "Risk Score": 4, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-08 18:00", "User_ID": "007", "Albuminuria": 50, "Serum Creatinine": 1.18, "Uric Acid": 6.5, "Risk Score": 5, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-15 08:00", "User_ID": "007", "Albuminuria": 65, "Serum Creatinine": 1.28, "Uric Acid": 6.9, "Risk Score": 6, "Risk Level": "High Risk - Alert Provider 🚨", "Alert": "Yes"},
]

df = pd.DataFrame(health_data)

st.dataframe(df)

data = {
    "Reading #": list(range(1, 8)),
    "Glucose Reading (mg/dL)": [112, 138, 114, 121, 137, 124, 127]
}

df = pd.DataFrame(data)

st.table(df)

value = 86
fig, ax = plt.subplots(figsize=(3, 3), dpi=150)
wedges, _ = ax.pie(
    [value, 100 - value],
    colors = ["#FF0000", "#d3d3d3"],
    startangle=90,
    radius=0.05
)

ax.text(
    0, 0,
    f"{6}",
    ha="center",
    va="center",
    fontsize=10,
    fontweight="bold",
)

ax.axis("equal")

st.pyplot(fig)