from google import genai
import streamlit as st

client = genai.Client(api_key="AIzaSyAihTmYq1opwaE9n2Wk9iqqRXV7W1yKLiE")

def ask_gemini(question):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question,
    )
    return response.text

######################################

import requests

url = "https://travel-advisor.p.rapidapi.com/locations/v2/auto-complete"

querystring = {"query":"eiffel tower","lang":"en_US","units":"km"}

headers = {
	"x-rapidapi-key": "711b83bc7cmsh21d4397b0cc43b6p16127cjsn7bffffd466b8",
	"x-rapidapi-host": "travel-advisor.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

#print(response.json())

####

st.header("Travel Itinerary App")

place = st.text_input("Enter the name of the place you will be visiting : ")

days = st.text_input("Enter the number of days you will be staying there : ")

st.button("Done")

prompt = {f"Using this input {place}, create an itinerary for {days} days including places, restaurants, and more using data from this: {str(response.json())} "}
if st.button:
    output = ask_gemini(prompt)
    st.write(output)

