from google import genai

client = genai.Client(api_key = "AIzaSyCJu7AnPfA0PaZr0YfhHT1jhKREIgGbRnw")

def ask_gemini(question):
    response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = question,
    )
    return response.text
#------------------------------------
print("Welcome to Intelligent Personal Finance Manager! Type 'exit' to quit.")

income = input("Enter your monthly income after taxes : ")

# print("Enter your recurring monthly expenses (type 'done' when finished) : ")
# expense = input("Expense description : ")
# cost = input("Amount : ")
goal = input("Enter your savings goal for this month : ")
while True:
    #while income != "exit":
    print("Enter your recurring monthly expenses (type 'done' when finished) : ")
    expense = input("Expense description : ")
    if expense != "done":
        cost = input("Amount : ")
    if expense == "exit":
        print("Thank you for using Intelligent Personal Finance Manager! Remember, every dollar saved counts toward your goals.")
        exit(0)
    

    
    while expense == "done":
        
        print("Enter your daily expenses (type 'done' when finished) : ")
        
        daily_expenses = input("Expense description : ")
        category = input("Category : ")
        daily_expense_cost = input("Amount : ")
        if daily_expenses == "done":
            prompt = f'''Give an analysis on daily expenses: expense: {daily_expenses},{daily_expense_cost}, provide advice based on their monthly expenses:{expense}, {cost}, their goal: {goal}, and their monthly income: {income}. Finally, give an update on their progress '''

            ai_response = ask_gemini(prompt)
            print(f"Gemini AI : {ai_response}")
        
        while daily_expenses == "done":
            response = input("Would you like more detailed insights or advice? (yes/no). If done, type either 'exit', 'done', or 'no' : ")
            if response == "yes":
                prompt_2 = f'''Provide a more detailed analysis, with detailed insights, and more advice of the reaching their goal: {goal} with their monthly income: {income}, daily expenses:{daily_expenses},{daily_expense_cost}, monthly expenses:{expense}, {cost}, alongside a more detailked view of their progress'''
                ai_response = ask_gemini(prompt)
                print(f"Gemini AI : {ai_response}")

            if response == "exit":
                print("Thank you for using Intelligent Personal Finance Manager! Remember, every dollar saved counts toward your goals.")
                exit(0)
            if response == "no":
                print("Thank you for using Intelligent Personal Finance Manager! Remember, every dollar saved counts toward your goals.")
                exit(0)
            if response == "done":
                print("Thank you for using Intelligent Personal Finance Manager! Remember, every dollar saved counts toward your goals.")
                exit(0)