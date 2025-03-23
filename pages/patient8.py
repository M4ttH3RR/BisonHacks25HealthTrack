import streamlit as st
import os

# Set page title
st.title("John Doe")

# Define the path to the static folder
STATIC_PATH = os.path.join(os.getcwd(), 'static')

# Display patient picture
img_path = os.path.join(STATIC_PATH, "woman4.jpg")
st.image(img_path, caption="John Doe", width=200)

# Display patient details
st.write("**Name:** John Doe")
st.write("**Age:** 45 years")
st.write("**Weight:** 180 lbs")

# Home button to navigate back to the main page
if st.button("Home"):
    st.switch_page("app.py")