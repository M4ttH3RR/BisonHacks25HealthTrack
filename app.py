import streamlit as st
import os



st.set_page_config(page_title="home", layout="wide")
st.title("Dr. Mike")



STATIC_PATH = os.path.join(os.getcwd(), 'static')


st.markdown("""
    <style>
        .schedule-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: #107HFF;
            color: Grey;
            padding: 15px;
            border-radius: 10px;
            text-decoration: none;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            width: 200px;
            height: 200px;
            margin: 20px auto;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        }
        .schedule-btn:hover {
            background-color: #0056b3;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<a href="/scheduling" class="schedule-btn">Schedule</a>', unsafe_allow_html=True)

st.markdown('<a href="/messaging" class="schedule-btn">Message Patient</a>', unsafe_allow_html=True)

if not st.session_state.get('alert_shown', False):
    st.session_state.alert_shown = True
    st.warning("🚨 High Risk Alert for Zia Abiodun!")
