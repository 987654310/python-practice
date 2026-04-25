from google import genai
import streamlit as st


client = genai.Client(api_key = "AIzaSyCJu7AnPfA0PaZr0YfhHT1jhKREIgGbRnw")

def ask_gemini(question):
    response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = question,
    )
    return response.text


st.title("Simple Story Generator")
st.write("Welcome to Story Generator! Type 'exit' to quit.")

story_prompt = st.text_input("Enter a story prompt :")
submit = st.button("Submit")

if submit:
    prompt = f"Create a short story based on the following prompt: {story_prompt}"
    
    if story_prompt == "exit":
        st.write("Thank You, and Goodbye!")

    else:
        ai_response = ask_gemini(prompt)
        print(f"Gemini AI : {ai_response}")
        st.write(ai_response)