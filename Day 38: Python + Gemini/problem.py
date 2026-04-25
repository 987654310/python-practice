from google import genai

client = genai.Client(api_key = "AIzaSyCJu7AnPfA0PaZr0YfhHT1jhKREIgGbRnw")

def ask_gemini(question):
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = question,
    )
    return response.text
#-----------------------------------------------------------------------------------------------------------

while True:
    word = input("Which word do you want to be explained in simple English? : ")
    print(f"User : Explain {word} to a beginner student in simple words. ")

    if word == "exit":
        print("Goodbye")
        break

    ai_response = ask_gemini(word)
    print(f"AI : {ai_response}")
    