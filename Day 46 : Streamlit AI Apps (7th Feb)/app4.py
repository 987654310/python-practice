from google import genai
import streamlit as st

client = genai.Client(api_key = "AIzaSyCJu7AnPfA0PaZr0YfhHT1jhKREIgGbRnw")

def ask_gemini(question):
    response = client.models.gene1rate_content(
    model = "gemini-2.5-flash",
    contents = question,
    )
    return response.text
#------------------------------------
st.title("Personal Finance Manager")
st.write("Welcome to Intelligent Personal Finance Manager! Type 'exit' to quit.")

exit = st.button("exit")
income = st.number_input("Enter your monthly income after taxes : ")
if exit:
    st.write("Thank you for using Intelligent Personal Finance Manager! Remember, every dollar saved counts toward your goals.")

# income = st.number_input("Enter your monthly income after taxes : ")
# print("Enter your recurring monthly expenses (type 'done' when finished) : ")
# expense = input("Expense description : ")
# cost = input("Amount : ")
# goal = st.number_input("Enter your savings goal for this month : ")
    #while income != "exit":
if 'monthly_expenses' not in st.session_state:
    st.session_state["monthly_expenses"] = []
if 'daily_expenses' not in st.session_state:
    st.session_state["daily_expenses"] = []

st.write("Enter your recurring monthly expenses (press 'done' when finished) : ")
done = st.button("done")

# with st.form("my_form"):
#     expense_done = st.text_input("Monthly Expense description : ")
#     cost_done = st.number_input("Amount : ", min_value = 0.0)
#     submitted = st.form_submit_button("Add")
# if done:
#     st.write("Enter your daily expenses (press 'done' when finished) : ")
# if expense_done and cost_done:
#     st.session_state.monthly_expenses.append({
#         "description": expense_done,
#         "cost": cost_done
#     })
    # a = st.session_state["monthly_expenses"].append(f"Monthly Expenses : Expense description : {expense_done}, Cost : {cost_done}")  
    # st.write(f"Session state:",st.session_state["monthly_expenses"])

#########################
while not done:
    with st.form(key = "monthly_form"):
        expense_des = st.text_input("Monthly Expense Description:")
        expense_cost = st.number_input("Amount:", min_value=0.0)
        submitted = st.form_submit_button("Add Expense")
        st.write("Monthly Expenses")
        st.write(st.session_state["monthly_expenses"])
        
        if submitted and expense_des:
            st.session_state["monthly_expenses"].append({
                "description": expense_des,
                "cost": expense_cost
            })  

        if done:
            goal = st.number_input("Enter your savings goal for this month : ")
            st.write("Enter your daily expenses (press 'done' when finished) : ")

        




##












# monthly_total = 0
# for expense in st.session_state["monthly_expenses"]:
#     monthly_total = monthly_total + st.session_state["monthly_expenses"]["cost"]
# daily_total = 0
# for expense in st.session_state["daily_expenses"]:
#     total_daily = total_daily + 




    ###expense_d = st.text_input("Daily Expense description : ")

        
    # daily_expenses = st.text_input("Expense description : ")
    # category = st.text_input("Category : ")
    # daily_expense_cost = st.number_input("Amount : ")
    # if daily_expenses == "done":
    #     prompt = f'''Give an analysis on daily expenses: expense: {daily_expenses},{daily_expense_cost}, provide advice based on their monthly expenses:{expense}, {cost}, their goal: {goal}, and their monthly income: {income}. Finally, give an update on their progress '''

    # ai_response = ask_gemini(prompt)
    # st.write(f"Gemini AI : {ai_response}")
        
    #     if daily_expenses == "done":
    #         response = st.text_input("Would you like more detailed insights or advice? (yes/no). If done, type either 'exit', 'done', or 'no' : ")
    #         if response == "yes":
    #             prompt_2 = f'''Provide a more detailed analysis, with detailed insights, and more advice of the reaching their goal: {goal} with their monthly income: {income}, daily expenses:{daily_expenses},{daily_expense_cost}, monthly expenses:{expense}, {cost}, alongside a more detailked view of their progress'''
    #             ai_response = ask_gemini(prompt)
    #             st.write(f"Gemini AI : {ai_response}")

    #         if response == "exit":
    #             st.write("Thank you for using Intelligent Personal Finance Manager! Remember, every dollar saved counts toward your goals.")

    #         if response == "no":
    #             st.write("Thank you for using Intelligent Personal Finance Manager! Remember, every dollar saved counts toward your goals.")
    #         if response == "done":
    #             st.write("Thank you for using Intelligent Personal Finance Manager! Remember, every dollar saved counts toward your goals.")
