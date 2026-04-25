import streamlit as st

st.title("Product Rating App")
st.subheader("Submit your Rating")

average = 0
if "ratings" not in st.session_state:
    st.session_state["ratings"] = []
if "count" not in st.session_state:
    st.session_state["count"] = 0

rating = st.number_input("Enter your Rating", min_value=0.0, max_value=5.0, value = 0.0, step = 0.5)
st.write("Rating:", rating)

button_reset_result = st.button("Reset")
button_submit = st.button("Submit")

if button_submit:
    st.session_state["ratings"].append(rating)
    st.session_state["count"] = st.session_state["count"] + 1
    sum = 0
    for a in st.session_state["ratings"]:
        sum = sum + a
    average = sum/st.session_state["count"]

if button_reset_result:
    st.session_state["ratings"] = 0
    st.session_state["count"] = 0
    rating = 0.0

st.write("Total Number of Ratings:", st.session_state["count"])
st.write("Average of All Ratings", average)



#  ##################
# Directory
#ls
#cd Day tab 41 tab
# streamlit run Problem-3.py
