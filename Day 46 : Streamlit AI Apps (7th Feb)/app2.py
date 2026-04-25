from google import genai
import streamlit as st


client = genai.Client(api_key = "AIzaSyCJu7AnPfA0PaZr0YfhHT1jhKREIgGbRnw")

def ask_gemini(question):
    response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = question,
    )
    return response.text


st.title("Language Translator")
st.write("Welcome to Translator! Type 'exit' to quit.")

prompt = st.text_input("Enter a sentence in English: ")
submit = st.button("Submit")

if submit:
    ai_prompt = f"Translate the following prompt into German: {prompt}"
    
    if prompt == "exit":
        st.write("Goodbye!")

    else:
        ai_response = ask_gemini(ai_prompt)
        print(f"Gemini AI : {ai_response}")
        st.write(ai_response)