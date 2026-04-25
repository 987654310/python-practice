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

url = "https://real-time-amazon-data.p.rapidapi.com/product-details"

querystring = {"asin":"B07ZPKBL9V","country":"US"}

headers = {
	"x-rapidapi-key": "711b83bc7cmsh21d4397b0cc43b6p16127cjsn7bffffd466b8",
	"x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

st.header("Product Comparison App")
product = st.text_input("Enter the name of a product : ")

st.button("Done")

prompt = {f"Using the data from this: {str(response.json())} extract at least 3 - 5 {product}s and get the name, price, brand, rating, features, and provide your recomendations on what is best overall option and then provide which one is the best budget friendly option :"}

if st.button:
    output = ask_gemini(prompt)
    st.write(output)