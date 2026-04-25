from google import genai
import streamlit as st


client = genai.Client(api_key = "AIzaSyCJu7AnPfA0PaZr0YfhHT1jhKREIgGbRnw")

def ask_gemini(question):
    response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = question,
    )
    return response.text


st.title("Math Tutor")
st.write("Welcome to Math Tutor! Type 'exit' to quit.")

math_prompt = st.text_input("Enter a math problem (e.g., 'What is 5 plus 7?') :")
submit = st.button("Submit")

if submit:
    prompt = f"Answer the following question by acting as a Math Tutor and answering the prompt {math_prompt}"
    
    if math_prompt == "exit":
        st.write("Gemini AI: Keep practicing math!")

    else:
        ai_response = ask_gemini(prompt)
        print(f"Gemini AI : {ai_response}")
        st.write(ai_response)