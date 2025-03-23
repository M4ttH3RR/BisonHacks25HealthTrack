import streamlit as st
import os
import matplotlib.pyplot as plt
import pandas as pd

st.title("John Lewis")

STATIC_PATH = os.path.join(os.getcwd(), 'static')

img_path = os.path.join(STATIC_PATH, "man2.jpg")
st.image(img_path, width=200)


st.write("**Age:** 31 years")
st.write("**Weight:** 182 lbs")
st.write("**Height:** 6'2''")


health_data = [
    # Patient 001
    {"Timestamp": "2025-03-01 08:00", "User_ID": "002", "Albuminuria": 28, "Serum Creatinine": 0.85, "Uric Acid": 5.2, "Risk Score": 1, "Risk Level": "Low Risk", "Alert": "No"},
    {"Timestamp": "2025-03-01 12:00", "User_ID": "002", "Albuminuria": 34, "Serum Creatinine": 0.98, "Uric Acid": 5.7, "Risk Score": 1, "Risk Level": "Low Risk", "Alert": "No"},
    {"Timestamp": "2025-03-01 18:00", "User_ID": "002", "Albuminuria": 31, "Serum Creatinine": 0.93, "Uric Acid": 5.5, "Risk Score": 1, "Risk Level": "Low Risk", "Alert": "No"},
    {"Timestamp": "2025-03-08 08:00", "User_ID": "002", "Albuminuria": 42, "Serum Creatinine": 1.04, "Uric Acid": 6.0, "Risk Score": 2, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-08 12:00", "User_ID": "002", "Albuminuria": 47, "Serum Creatinine": 1.08, "Uric Acid": 6.2, "Risk Score": 2, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-08 18:00", "User_ID": "002", "Albuminuria": 49, "Serum Creatinine": 1.12, "Uric Acid": 6.4, "Risk Score": 3, "Risk Level": "Moderate Risk", "Alert": "No"},
    {"Timestamp": "2025-03-15 08:00", "User_ID": "002", "Albuminuria": 55, "Serum Creatinine": 1.19, "Uric Acid": 6.6, "Risk Score": 3, "Risk Level": "Moderate Risk", "Alert": "No"},
    ]

df = pd.DataFrame(health_data)

st.dataframe(df)

data = {
    "Reading #": list(range(1, 15)),
    "Glucose Reading (mg/dL)": [114, 138, 113, 116, 134, 121, 119]
}

df = pd.DataFrame(data)

st.table(df)