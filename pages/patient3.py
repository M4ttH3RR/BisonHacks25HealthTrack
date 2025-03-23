import streamlit as st
import os
import matplotlib.pyplot as plt
import pandas as pd

st.title("Aaliyah Johnson")


STATIC_PATH = os.path.join(os.getcwd(), 'static')


img_path = os.path.join(STATIC_PATH, "woman1.jpg")
st.image(img_path, width=200)


st.write("**Age:** 56 years")
st.write("**Weight:** 189 lbs")
st.write("**Height:** 5'6''")

health_data = [{"Timestamp": "2025-03-01 08:00", "User_ID": "002", "Albuminuria": 30, "Serum Creatinine": 0.87, "Uric Acid": 5.3, "Risk Score": 1, "Risk Level": "Low Risk", "Alert": "No"},
    {"Timestamp": "2025-03-01 12:00", "User_ID": "003", "Albuminuria": 35, "Serum Creatinine": 0.99, "Uric Acid": 5.6, "Risk Score": 1, "Risk Level": "Low Risk", "Alert": "No"},
    {"Timestamp": "2025-03-01 18:00", "User_ID": "003", "Albuminuria": 40, "Serum Creatinine": 1.02, "Uric Acid": 5.9, "Risk Score": 2, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-08 08:00", "User_ID": "003", "Albuminuria": 50, "Serum Creatinine": 1.15, "Uric Acid": 6.3, "Risk Score": 3, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-08 12:00", "User_ID": "003", "Albuminuria": 55, "Serum Creatinine": 1.20, "Uric Acid": 6.5, "Risk Score": 3, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-08 18:00", "User_ID": "003", "Albuminuria": 60, "Serum Creatinine": 1.28, "Uric Acid": 6.9, "Risk Score": 4, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-15 08:00", "User_ID": "003", "Albuminuria": 95, "Serum Creatinine": 1.65, "Uric Acid": 8.2, "Risk Score": 7, "Risk Level": "High Risk - Alert Provider 🚨", "Alert": "Yes"},
]

df = pd.DataFrame(health_data)

st.dataframe(df)

data = {
    "Reading #": list(range(1, 15)),
    "Glucose Reading (mg/dL)": [121, 132, 125, 125, 135, 143, 118]
}

df = pd.DataFrame(data)

st.table(df)