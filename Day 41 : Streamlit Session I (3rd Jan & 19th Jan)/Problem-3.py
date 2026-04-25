import streamlit as st
st.title("Hello, Streamlit")
st.write("This is my first app")

a = 0
b = 0
a = st.number_input("Enter your weight in kg: ")
b = st.number_input("Enter your height in cm: ")

if a and b:
    # b_2 = b/100
    # b_2 = b_2 * b_2
    # bmi = a / b_2
    #bmi = a / (b** 2)
    height_meter = b / 100  
    bmi = a / (height_meter**2)
    st.write("Your BMI is:",bmi)
    whole = bmi//1
    diff = bmi - whole
    bmi_round = 0
    
#############Thousandth


    # diff_hundredth = (diff * 100)//1
    # diff_thousandth = (diff * 1000)// 1
    # thousandth_place = diff_thousandth - diff_hundredth

    # if thousandth_place >= 0.005:
    #     diff_dec = 0.010 - thousandth_place
    #     bmi_round = bmi + diff_dec
    # else:
        
    #     bmi_round = bmi - diff_dec

###########
# b = b(int)
# a = a(int)


# height_meter = b / 100  
# height_meter = height_meter(int)
# bmi = a / (height_meter**2)
# print("Your BMI is:",bmi)
# whole = bmi//1
# diff = bmi - whole
# bmi_round = 0
    
# if a and b:

    diff_hundredth = (diff * 100)//1
    diff_hund = diff_hundredth * 10
    diff_thousandth = (diff * 1000)// 1
    thousandth_place = diff_thousandth - diff_hund
    t = thousandth_place/1000
    if t >= 0.005:
        
        diff_dec = 0.010 - t
        bmi_r = bmi + diff_dec
        bmi_round = ((bmi_r * 100)//1)/100
    else:
        diff_dec = 0.010 - t
        bmi_round = ((bmi * 100)//1)/100
        
    # st.write(f"Diff-hundreth = {diff_hund}, Diff-thousand = {diff_thousandth}") 

    # st.write(f"Diff dec = {diff_dec}, Thousandth_place = {thousandth_place}, {t}")
    # st.write(f"BMI Round = {bmi_round}")
###########

    ##Hundredth
    # diff_tenth = (diff * 10)//1
    # diff_hundredth = (diff * 100)// 1
    # hundredth_place = diff_hundredth - diff_tenth

    # ##tenth
    # if diff >= 0.5:
    #     diff_dec = 1 - diff
    #     bmi_round = bmi + diff_dec
    # else:
    #     bmi_round = bmi - diff
    #######


    #bmi_rounded = ((bmi * 100) + 0.5)/100#
    st.write("BMI Rounded =", bmi_round)

    if bmi_round < 18.5:
        st.write("Category: Underweight")
    elif bmi_round >= 18.5 and bmi_round <= 24.9:
        st.write("Category: Normal")
    elif bmi_round >= 25 and bmi_round <= 29.9:
        st.write("Category: Overweight")
    elif bmi_round >= 30:
        st.write("Category: Obese")
            
  
   
   
   
   # whole = ((bmi * 100) + 0.5)//100


# if result <18.5:
#     st.write(f"Category: Underweight")

# else:
#     st.write(f"Category: weight")
# elif operation == "Multiply":
#     st.write(f"Result:", a * b)

# elif operation == "Divide":
#     if b == 0:#b_int == 0 and operation == "Divide":
#         st.write("Sorry, B cannot be divided by zero.")
#     else:
#         st.write(f"Result:", a / b)
#
#
# 
# 
# 
#  ##################
# Directory
#ls
#cd Day tab 41 tab
# streamlit run Problem-3.py
