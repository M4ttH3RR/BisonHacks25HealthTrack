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

health_data = [
    {"Timestamp": "2025-03-01 08:00", "User_ID": "006", "Albuminuria": 30, "Serum Creatinine": 0.85, "Uric Acid": 5.2, "Risk Score": 2, "Risk Level": "Low Risk", "Alert": "No"},
    {"Timestamp": "2025-03-01 12:00", "User_ID": "006", "Albuminuria": 34, "Serum Creatinine": 0.90, "Uric Acid": 5.5, "Risk Score": 2, "Risk Level": "Low Risk", "Alert": "No"},
    {"Timestamp": "2025-03-01 18:00", "User_ID": "006", "Albuminuria": 37, "Serum Creatinine": 0.92, "Uric Acid": 5.6, "Risk Score": 2, "Risk Level": "Low Risk", "Alert": "No"},
    {"Timestamp": "2025-03-08 08:00", "User_ID": "006", "Albuminuria": 40, "Serum Creatinine": 0.94, "Uric Acid": 5.8, "Risk Score": 2, "Risk Level": "Low Risk", "Alert": "No"},
    {"Timestamp": "2025-03-08 12:00", "User_ID": "006", "Albuminuria": 45, "Serum Creatinine": 0.97, "Uric Acid": 6.0, "Risk Score": 2, "Risk Level": "Low Risk", "Alert": "No"},
    {"Timestamp": "2025-03-08 18:00", "User_ID": "006", "Albuminuria": 48, "Serum Creatinine": 1.00, "Uric Acid": 6.1, "Risk Score": 2, "Risk Level": "Low Risk", "Alert": "No"},
    {"Timestamp": "2025-03-15 08:00", "User_ID": "006", "Albuminuria": 52, "Serum Creatinine": 1.03, "Uric Acid": 6.3, "Risk Score": 2, "Risk Level": "Low Risk", "Alert": "No"},
    {"Timestamp": "2025-03-15 12:00", "User_ID": "006", "Albuminuria": 58, "Serum Creatinine": 1.10, "Uric Acid": 6.5, "Risk Score": 4, "Risk Level": "Moderate Risk", "Alert": "No"},
]

df = pd.DataFrame(health_data)

st.dataframe(df)

data = {
    "Reading #": list(range(1, 8)),
    "Glucose Reading (mg/dL)": [133, 135, 132, 127, 123, 141, 118]
}

df = pd.DataFrame(data)

st.table(df)

value = 57
fig, ax = plt.subplots(figsize=(3, 3), dpi=150)
wedges, _ = ax.pie(
    [value, 100 - value],
    colors = ["#FFFF00", "#d3d3d3"],
    startangle=90,
    radius=0.05
)

ax.text(
    0, 0,
    f"{4}",
    ha="center",
    va="center",
    fontsize=10,
    fontweight="bold",
)

ax.axis("equal")

st.pyplot(fig)