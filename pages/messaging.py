import streamlit as st

# Title of the app
st.title("Doctor-Patient Messaging System")

# Initialize session state for messages if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

patient_name = st.text_input("Enter Patient's Name:")

# Input field for new messages
new_message = st.text_input("Type your message:")

# Send button logic
if st.button("Send Message"):
    if not patient_name.strip():
        st.warning("Please enter the Patient's name before sending.")
    elif not new_message.strip():
        st.warning("Please enter a message before sending.")
    else:
        # Add new message to chat history with Doctor and Patient's name
        st.session_state.messages.append(("Doctor", patient_name, new_message))


# Display chat history
st.write("### Chat History")
for msg in st.session_state.messages:
    sender, patient, text = msg
    if sender == "Doctor":
        st.markdown(f"**🧑‍⚕️ Doctor (to {patient}):** {text}")