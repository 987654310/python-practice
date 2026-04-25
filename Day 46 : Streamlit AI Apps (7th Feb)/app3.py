from google import genai
import streamlit as st


client = genai.Client(api_key = "AIzaSyCJu7AnPfA0PaZr0YfhHT1jhKREIgGbRnw")

def ask_gemini(question):
    response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = question,
    )
    return response.text


st.title("Fun Fact Generator")
st.write("Welcome to Fun Fact Generator! Type 'exit' to quit.")

prompt = st.text_input("Enter a topic for a fun fact: ")
submit = st.button("Submit")

if submit:
    ai_prompt = f"Create a fun fact using the following topic: {prompt}"
    
    if prompt == "exit":
        st.write("Goodbye!")

    else:
        ai_response = ask_gemini(ai_prompt)
        print(f"Gemini AI : {ai_response}")
        st.write(ai_response)