import streamlit as st

st.text_input("Enter your first name:", key="first_name_input") # Unique key
st.text_input("Enter your last name:", key="last_name_input")   # Unique key

# You can now access the values in st.session_state using these keys
st.write("First Name:", st.session_state.first_name_input)
st.write("Last Name:", st.session_state.last_name_input)
