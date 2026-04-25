import streamlit as st

st.title("Balance Tracker")

if "amount" not in st.session_state:
    st.session_state["amount"] = 0
if "information" not in st.session_state:
    st.session_state["information"] = {
        "Amount": 0,
        "Option": "None"
        }

amount = st.number_input("Enter an Amount:", min_value=0)

# st.write("Amount:", amount)
change = st.radio("Select an Option", ["Income", "Expense"])
st.write("Option:", change)

reset = st.button("Reset")
submit = st.button("Submit")

# information = {
#         "Amount": 0,
#         "Option": "none"
#                         }

if submit:
    if change == "Income":
        st.session_state["amount"] = st.session_state["amount"] + amount
    if change == "Expense":
        st.session_state["amount"] = st.session_state["amount"] - amount
    st.session_state["information"] = {"Amount" : amount, "Option": change}
    # if button_reset_result:
    #     st.session_state["balance"] = 0
    #     information["Option"] = "none"
    #     information["Amount"] = 0






if reset:
    st.session_state["amount"] = 0
    # st.session_state["information"] = {
    #     "Amount": 0, 
    #     "Option": "None"
    #     }
st.subheader("Current Balance: ")
st.write(st.session_state["amount"])
st.subheader("Last Transaction: ")
st.write(st.session_state["information"])
# st.write(" Information from last transaction:") 
# st.write(f"Option: {information['Option']}")
# st.write(f"Amount: {information["Amount"]} ")

# st.write("Balance", st.session_state["balance"])

# for k, v in information.items():
#     st.write(f"Information from last transaction: Option {information['Option']} and Amount - {information["Amount"]}  ")


#  ##################
# Directory
#ls
#cd Day tab 41 tab
# streamlit run Problem-3.py
