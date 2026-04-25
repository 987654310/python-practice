inventory = {}
sale = []

from datetime import datetime

now = datetime.now()
now_s = str(now)

#####1
def add_snack(inventory):
    snack_id = input("Enter Snack Id : ")
    name = input("Enter Snack name : ")
    price = input("Enter Price : ")
    inventory[snack_id] = {
        "name":name,
        "price":int(price),
        "availability": True
    }
    print(f"{name} added to inventory!")


#####2
def remove_snack(inventory):
    snack = input("Enter Snack ID to Remove : ")
    if snack in inventory:
        del inventory[snack]
        print(f"{snack} Removed from Inventory!")
    else:
        print("Error: Snack Not Found in Inventory")


#####3
def update_availability(inventory):
    id_of_snack = input("Enter Snack ID : ")
    if id_of_snack in inventory:
        set_availability = input("Set Availability to (Yes/No) : ")
        if set_availability == "Yes" or set_availability == "yes" :
            inventory[id_of_snack]["availability"] = True
        
        
        elif set_availability == "No" or set_availability == "no" :
            inventory[id_of_snack]["availability"] = False
        else:
            print("Error")
    else:
        print("Error: Snack ID Not Found in Inventory")

#####4
snack_id_sold_history = {}
def record_sale(inventory):
    snack_id_sold = input("Enter snack ID sold : ")
    v = inventory[snack_id_sold]["price"]
    i = inventory[snack_id_sold]["name"]
    if snack_id_sold in inventory:
        
        snack_id_sold_history[i] = {
            "price" : v,
            "time" : now_s 
        }
        
    elif snack_id_sold not in inventory:
        print(f"Error: Snack ID {snack_id_sold} not found!")

    elif inventory[snack_id_sold]["availability"] == False:
        print(f"Error: {inventory[snack_id_sold]["name"]} is unavailable!")
        
    print(snack_id_sold_history)

######6    
def print_sale(snack_id_history):
    print(f"Sales History: {snack_id_history}")


    
   
    # if snack_id_sold in inventory:
    #     [] = snack_id_sold
    #     record_sale[] = inventory[]["price"]
    # elif snack_id_sold not in inventory:
    #         print("Error: Vada Pav is unavailable!")    











menu = """
1. Add Snack
2. Remove Snack
3. Update availability
4. Record sale
5. View inventory
6. View sales
7. Exit
"""

while True:
    choice = input("Enter Choice : ")
    if choice == "1":
        add_snack(inventory)
    elif choice == "2":
        remove_snack(inventory)
    elif choice == "3":
        update_availability(inventory)
    elif choice == "4":
        record_sale(inventory)

    # ....record_sale

    # ....
    elif choice == "5":
        print(inventory)
    # elif choice == "6":
    #     print_sale(inventory)

    elif choice == "7":
        print("Thank You and Bye!")
        break

    else:
        print("Invalid Choice")

