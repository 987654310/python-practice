import streamlit as st

st.title("Hello, Streamlit")
st.write("This is my first app")

name = st.text_input("Enter your name")
age = st.slider("How old are you", 0, 120, 18)

st.write("Your Age is", age)

st.write (f"Hello {name} 👋,")
st.write(f"You'll turn {age + 1} next year.")
st.write(f"You've lived roughly {age * 365} days.")