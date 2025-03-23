import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import time
import streamlit as st

# -------------------------------------------------------------------
# DATA PROCESSING & FEATURE ENGINEERING
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


# -------------------------------------------------------------------
# MAIN EXECUTION
# -------------------------------------------------------------------
def main():
    # Load the dataset from your CSV file
    df = pd.read_csv('biomarket_dataset.csv')

    # Preprocess the data
    df = preprocess_data(df)

    # Train the model on the dataset
    model, scaler = train_risk_model(df)

    # Initialize session state for tracking the last update time
    if "last_update" not in st.session_state:
        st.session_state.last_update = time.time()

    # Simulated data string: "2025-03-23 08:00 003 30 1.25 6.7"
    data_string = "2025-03-23 08:00 003 30 1.25 6.7"
    list_values = data_string.split()

    # Extract values from the string
    timestamp, user_id, albuminuria, creatinine, eGFR, uric_acid = list_values
    albuminuria, creatinine, eGFR, uric_acid = float(albuminuria), float(creatinine), float(eGFR), float(uric_acid)

    # Predict risk for the patient using received data
    patient_risk, patient_category = predict_risk(model, scaler, albuminuria, creatinine, eGFR, uric_acid)
    print(f"📊 Predicted Risk for {user_id}: {patient_risk:.2f} ({patient_category})")

    # Display Streamlit popup or notification based on risk
    if patient_risk >= 0.7:
        # Use JavaScript to show pop-up for high risk
        st.markdown(f"""
        <script type="text/javascript">
            alert("🚨 High Risk Alert for User {user_id}!\\nRisk Probability: {patient_risk:.2f}\\nRisk Category: {patient_category}");
        </script>
        """, unsafe_allow_html=True)
    else:
        # Use Streamlit success notification
        st.success(f"✅ Low Risk for User {user_id}\nRisk Probability: {patient_risk:.2f}\nRisk Category: {patient_category}")

    # Check if 30 seconds have passed since the last update
    if time.time() - st.session_state.last_update >= 4:
        st.session_state.last_update = time.time()  # Update the last update time

# Run the main function
if __name__ == "__main__":
    main()