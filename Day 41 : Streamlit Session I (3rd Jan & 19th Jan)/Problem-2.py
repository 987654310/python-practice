import streamlit as st

st.title("Hello, Streamlit")
st.write("This is my first app")
a = 0
b = 0
a = st.number_input("Enter the value for A: ")
b = st.number_input("Enter the value for B: ")

operation = st.radio("Select an operation", ["Add", "Subtract", "Multiply", "Divide"])

if operation == "Add":
    st.write(f"Result:", a + b)

elif operation == "Subtract":
    st.write(f"Result:", a - b)

elif operation == "Multiply":
    st.write(f"Result:", a * b)

elif operation == "Divide":
    if b == 0:#b_int == 0 and operation == "Divide":
        st.write("Sorry, B cannot be divided by zero.")
    else:
        st.write(f"Result:", a / b)

