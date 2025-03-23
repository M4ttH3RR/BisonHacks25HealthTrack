import serial
import time
from flask import Flask, request, jsonify, render_template
import streamlit as st
import os

app = Flask(__name__)

st.set_page_config(page_title="home", layout="wide")
st.title("Dr. Mike")
st.write("Patient List")

STATIC_PATH = os.path.join(os.getcwd(), 'static')



