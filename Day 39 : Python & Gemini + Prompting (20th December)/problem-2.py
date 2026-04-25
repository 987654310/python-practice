from google import genai

client = genai.Client(api_key = "AIzaSyCJu7AnPfA0PaZr0YfhHT1jhKREIgGbRnw")

def ask_gemini(question):
    response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = question,
    )
    return response.text
#------------------------------------
intructions = print("Welcome to Story Generator! Type 'exit' to quit.")

while True:
    
    story_prompt = input("Enter a story prompt : ")
   
    prompt = f'''Create a short story based on the following prompt: {story_prompt}'''
    
    if story_prompt == "exit":
        print("Happy storytelling!")
        break

    ai_response = ask_gemini(prompt)
    print(f"Gemini AI : {ai_response}")
