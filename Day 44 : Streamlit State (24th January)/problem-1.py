import streamlit as st

st.title("Voting App")
st.subheader("Vote for a candidate")

if "count_1" not in st.session_state:
    st.session_state["count_1"] = 0
if "count_2" not in st.session_state:
    st.session_state["count_2"] = 0

button_1_result = st.button("A")
button_2_result = st.button("B")
button_reset_result = st.button("Reset")

if button_1_result:
    button_1_result = st.session_state["count_1"] = st.session_state["count_1"] + 1
if button_2_result:
    button_2_result = st.session_state["count_2"] = st.session_state["count_2"] + 1
if button_reset_result:
    st.session_state["count_1"] = 0
    st.session_state["count_2"] = 0

st.write("Vote count for Candidate A: ", st.session_state["count_1"])
st.write("Vote count for Candidate B: ", st.session_state["count_2"])


#  ##################
# Directory
#ls
#cd Day tab 41 tab
# streamlit run Problem-3.py
