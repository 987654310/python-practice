customer_carts = {
    'amit_123': ['laptop', 'mouse', 'headphones'],
    'riya_456': ['dress', 'lipstick', 'lipstick'],
    'john_p': ['t-shirt', 'jeans'],
    'nina_m': [],
    'arun_dev': ['laptop', 'mouse', 'keyboard', 'laptop']
}


orders = {
    'ORD101': {'customer_name': 'amit_123', 'total_amount': 55000.0, 'status': 'delivered'},
    'ORD102': {'customer_name': 'riya_456', 'total_amount': 340.0, 'status': 'pending'},
    'ORD103': {'customer_name': 'john_p', 'total_amount': 899.0, 'status': 'cancelled'},
    'ORD104': {'customer_name': 'nina_m', 'total_amount': 0.0, 'status': 'cancelled'}
}

#####
items_summary = {}

##########
# unsucessful_with_items = []

# for key,value in customer_carts.items():
#     has_ordered = False
#     for a,b in orders.items():
#         if b["customer_name"] == key and b["status"] != "cancelled":
#             has_ordered = True
    
#     if has_ordered == False and len(value) > 0:
#             unsucessful_with_items.append(key)
# print("--------------------------------")
# print(f"Unsuccessful Customers with Items: {unsucessful_with_items}")
print("--------------------------------")

##########
items_count = {}
for key, value in customer_carts.items():    
    if len(value) > 0:
        #items = value['items']
        for a in value: 
            if a in items_count:
                items_count[a] = items_count[a] + 1
            else:
                items_count[a] = 1

print(f"Count of Items: {items_count}")
print("--------------------------------")       

##########
unique_dict = {}
for key, value in customer_carts.items():
    unique = [] 
    for a in value:
        if a not in unique:
            unique.append(a)
    #     if a not in new_list:
    #         new_list.append(a)
    # customer_carts[key] = new_list
    # #
    # for b in value:
    #     if b not in unique:
    #         unique.append(b)
    unique_dict[key] = len(unique)
#print(customer_carts)

print(f"Num_Unique Items: {unique_dict}")
print("--------------------------------")   

##########
unsucessful_with_items = []
summary = []

for key, value in unique_dict.items():

    has_ordered = False
    for a,b in orders.items():
        if b["customer_name"] == key and b["status"] != "cancelled":
            has_ordered = True

    sum_d = {
            "items in cart": value,
            "has ordered": has_ordered
        }
    summary.append(sum_d)



    if has_ordered == False and len(customer_carts[key]) > 0:
            unsucessful_with_items.append(key)

print(summary)
print("--------------------------------")
print(f"Unsuccessful Customers with Items: {unsucessful_with_items}")

########################

cancelled_orders = []
for key, value in orders.items():    
    if value["status"] == "cancelled":
        cancelled_orders.append(key)

for a in cancelled_orders:
    del orders[a]


# for key, value in customer_carts.items():
#print(orders)