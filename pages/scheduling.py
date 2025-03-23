import streamlit as st
import pandas as pd

st.title("Doctor Appointment Scheduling")

if "appointments" not in st.session_state:
    st.session_state.appointments = []

with st.form("appointment_form"):
    st.subheader("Book an Appointment")

    patient_name = st.text_input("Patient Name", placeholder="Enter full name")
    contact = st.text_input("Contact Number", placeholder="Enter phone or email")
    appointment_date = st.date_input("Select Date")
    time_slot = st.selectbox("Select Time Slot",
                             ["09:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "02:00 PM", "03:00 PM", "04:00 PM"])
    reason = st.text_area("Reason for Visit", placeholder="Briefly describe the reason for your visit")

    submit = st.form_submit_button("Schedule Appointment")

if st.session_state.appointments:
    st.subheader("Scheduled Appointments")
    df = pd.DataFrame(st.session_state.appointments)
    st.dataframe(df, use_container_width=True)

if submit:
    st.success("Appointment Created!")