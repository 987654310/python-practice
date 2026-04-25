import streamlit as st
st.title("Hello, Streamlit")
st.write("This is my first app")

accept = st.checkbox("I agree to the terms")
st.write("Accepted?", accept)

m = st.number_input("Enter your grade for Math: ", min_value=0, max_value=120)
s = st.number_input("Enter your grade for Science: ", min_value=0, max_value=120)
h = st.number_input("Enter your grade for History: ", min_value=0, max_value=120)
hi = st.number_input("Enter your grade for Hindi: ", min_value=0, max_value=120)
e = st.number_input("Enter your grade for English: ", min_value=0, max_value=120)

list = [m, s, h, hi, e]

st.write("Total: ",sum(list) )
st.write("Highest: ",max(list) )
st.write("Lowest: ",min(list) )

st.write("Average: ",sum(list)/len(list) )

if min(list) >= 35 and sum(list)/len(list) >= 40:
    st.write("Pass")
else:
    st.write("Fail")

show_report = st.checkbox("Show detailed Report")


if show_report:
    # st.write(f"Total = Math: {m} + Science: {s} + History: {h} + Hindi {hi} + English {e} = Sum: {sum(list)}")
    # st.write(f"Average: {sum(list)/len(list)} = Sum: {sum(list)} / Num of Subjects: 5 ")
    st.write(f"Math: {m}, Science: {s}, History: {h}, Hindi {hi}, English {e}")
    st.write("Passing Grade: 35 or above, Passing Average: 40 or above")

