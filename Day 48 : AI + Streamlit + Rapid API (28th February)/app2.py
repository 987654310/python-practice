
from google import genai
import streamlit as st

client = genai.Client(api_key="AIzaSyANkBJSVJNGq_2gwYXsHylu4IHh06QRbCY")

def ask_gemini(question):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question,
    )
    return response.text



import requests

# url = "https://open-weather13.p.rapidapi.com/fivedaysforcast"

# querystring = {"latitude":"40.730610","longitude":"-73.935242","lang":"EN"}

st.title("Clothes Recommender according to weather App")

# city = input("Enter City : ")
city = st.text_input("Enter The City Name : ")

url = "https://open-weather13.p.rapidapi.com/city"

querystring = {"city":city,"lang":"EN"}

headers = {
	"x-rapidapi-key": "7a36c76496msh9d0ed8da1c8471bp13b13fjsnb56d8fa77e31",
	"x-rapidapi-host": "open-weather13.p.rapidapi.com"
}

button = st.button("Generate Summary")

if button:
    response = requests.get(url, headers=headers, params=querystring)

    # print(response.json())

    # prompt = "Summarize this weather data : "+ str(response.json())

    prompt = "I am providing you the weather data, Recommend me what kind of clothes I can wear : "+ str(response.json())


    output = ask_gemini(prompt)

    print(output)

    st.write(output)











# ------------------------------------------------------

# import requests

# url = "https://imdb236.p.rapidapi.com/api/imdb/tt0816692"

# headers = {
# 	"x-rapidapi-key": "7a36c76496msh9d0ed8da1c8471bp13b13fjsnb56d8fa77e31",
# 	"x-rapidapi-host": "imdb236.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)

# print(response.json())

# prompt = "summarize this data "+ str(response.json())
# output = ask_gemini(prompt)
# print(output)