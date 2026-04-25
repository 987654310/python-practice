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
import json


url = "https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/history"

querystring = {"symbol":"AAPL","interval":"5m","diffandsplits":"false"}

headers = {
	"x-rapidapi-key": "e09fcb6b9amsha9528a05d44ece1p13d596jsn433b7b02dec7",
	"x-rapidapi-host": "yahoo-finance15.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers, params=querystring)

#print(response.json())

st.header("Stock Analysis App")
company = st.text_input("Enter a company name or a company stock symbol : ")

st.button("Done")

prompt = {f"Using this input {company}(company name or stock symbol), create a list with information including the company name, stock symbol, curremt price, day high, day low, and an overview/ explaination using the data from this: {str(response.json())} Example: Company: Apple Inc. Example: Stock Symbol: AAPL, Current Price: $185.20, Day High: $187.10, Day Low: $183.90, Apple stock is currently stable with minor fluctuations today. This indicates normal market movement and long-term investor confidence."}

if st.button:
    output = ask_gemini(prompt)
    st.write(output)