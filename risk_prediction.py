import requests
import json
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# -------------------------------------------------------------------
# SECTION 1: DATA PROCESSING & FEATURE ENGINEERING
# -------------------------------------------------------------------

def classify_albuminuria(albuminuria):
    """Classifies albuminuria levels into Normal, Micro, or Macro."""
    if albuminuria < 30:
        return "Normal"
    elif 30 <= albuminuria <= 300:
        return "Microalbuminuria"
    else:
        return "Macroalbuminuria"


def preprocess_data(df):
    """Processes dataset by cleaning timestamps, classifying albuminuria, and handling missing values."""
    # Convert timestamps to datetime format
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")

    # Classify albuminuria into categories
    df["Albuminuria Category"] = df["Albuminuria (mg/day)"].apply(classify_albuminuria)

    # Convert "Alert" column to binary (1 for "Yes", 0 for "No")
    df["Alert"] = (df["Alert"] == "Yes").astype(int)

    # Handle missing values by filling with median values
    df.fillna(df.median(numeric_only=True), inplace=True)

    return df


# Load dataset
df = pd.DataFrame([
    ["2025-03-01 08:00", "001", 25, 0.85, 95, 5.2, "No"],
    ["2025-03-01 12:00", "001", 35, 1.12, 58, 6.3, "Yes"],
    ["2025-03-01 18:00", "001", 28, 0.92, 90, 5.8, "No"],
    ["2025-04-02 08:00", "001", 42, 1.15, 55, 6.1, "Yes"],
    ["2025-04-02 12:00", "001", 30, 0.97, 85, 5.5, "No"],
    ["2025-05-02 18:00", "001", 50, 1.20, 48, 6.5, "Yes"],
    ["2025-05-03 08:00", "001", 20, 0.72, 98, 5.4, "No"],
    ["2025-06-03 12:00", "001", 60, 1.25, 45, 6.7, "Yes"],
    ["2025-06-03 18:00", "001", 22, 0.80, 92, 5.1, "No"]
], columns=["Timestamp", "User_ID", "Albuminuria (mg/day)", "Serum Creatinine (mg/dL)", "eGFR (mL/min/1.73 m²)",
            "Uric Acid (mg/dL)", "Alert"])

df = preprocess_data(df)


# -------------------------------------------------------------------
# MACHINE LEARNING MODEL
# -------------------------------------------------------------------

def train_risk_model(df):
    """Trains a logistic regression model to predict DKD risk based on past alerts."""
    X = df[["Albuminuria (mg/day)", "Serum Creatinine (mg/dL)", "eGFR (mL/min/1.73 m²)", "Uric Acid (mg/dL)"]]
    y = df["Alert"]  # Use real alert labels for training

    global scaler  # Store scaler globally for later use
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)

    print(f"✅ Model Accuracy: {model.score(X_test, y_test):.2f}")
    return model, scaler


model, scaler = train_risk_model(df)


# -------------------------------------------------------------------
# RISK PREDICTION & ALERT SYSTEM
# -------------------------------------------------------------------

def predict_risk(model, scaler, albuminuria, creatinine, eGFR, uric_acid):
    """Predicts DKD risk and handles missing data safely."""
    # Handle missing values
    if any(pd.isnull([albuminuria, creatinine, eGFR, uric_acid])):
        return 0, "Unknown (Missing Data)"

    input_data = pd.DataFrame([[albuminuria, creatinine, eGFR, uric_acid]],
                              columns=["Albuminuria (mg/day)", "Serum Creatinine (mg/dL)", "eGFR (mL/min/1.73 m²)",
                                       "Uric Acid (mg/dL)"])
    X_scaled = scaler.transform(input_data)
    risk_probability = model.predict_proba(X_scaled)[:, 1][0]

    risk_category = "High Risk" if risk_probability >= 0.7 else "Low Risk"
    return risk_probability, risk_category


# Example patient
patient_risk, patient_category = predict_risk(model, scaler, 50, 1.3, 45, 7.5)
print(f"📊 Predicted Risk: {patient_risk:.2f} ({patient_category})")


# -------------------------------------------------------------------
# DATA TRANSMISSION TO PROVIDERS
# -------------------------------------------------------------------

def send_alert(data, api_url, api_key):
    """Sends high-risk patient data to healthcare providers via API."""
    headers = {'Content-Type': 'application/json', 'X-API-Key': api_key}

    try:
        response = requests.post(api_url, json=data, headers=headers)
        if response.status_code == 200:
            print("✅ Data successfully sent!")
        else:
            print(f"❌ Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"⚠️ Connection Error: {e}")


# Send alert if risk is high
if patient_risk >= 0.7:
    alert_data = {
        "User_ID": "001",
        "Albuminuria": 50,
        "Serum Creatinine": 1.3,
        "eGFR": 45,
        "Uric Acid": 7.5,
        "Risk Probability": patient_risk
    }
    send_alert(alert_data, "https://your-api.com/alerts", "YOUR_API_KEY")
else:
    print("🟢 No alert sent. Risk below threshold.")
