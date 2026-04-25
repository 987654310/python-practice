import requests
from google import genai
import streamlit as st

client = genai.Client(api_key="e09fcb6b9amsha9528a05d44ece1p13d596jsn433b7b02dec7")

def ask_gemini(question):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question,
    )
    return response.text


st.title("Movie Insight Application")
city = st.text_input("Enter the city name : ")

button = st.button("Generate Summary")

if button:
    url = "https://open-weather13.p.rapidapi.com/city"

    querystring = {"city":{city},"lang":"EN"}

    headers = {
        "x-rapidapi-key": "",
        "x-rapidapi-host": "open-weather13.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())


    # prompt = "Provide me the summary of this data "+ str(response.json())
    prompt = "Recommend me some clothes which I should wear in this weather "+ str(response.json())
    output = ask_gemini(prompt)
    st.write(output)