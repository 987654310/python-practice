orders = {
    'ORD101': {
        'customer_name': 'Amit Sharma',
        'items': ['Laptop', 'Mouse'],
        'total_amount': 55000.0,
        'status': 'delivered'
    },
    'ORD102': {
        'customer_name': 'Riya Mehta',
        'items': ['Shampoo', 'Toothpaste'],
        'total_amount': 340.0,
        'status': 'pending'
    },
    'ORD103': {
        'customer_name': 'John Paul',
        'items': ['T-shirt'],
        'total_amount': 899.0,
        'status': 'cancelled'
    },
    'ORD104': {
        'customer_name': 'Neha Singh',
        'items': ['Mobile Phone', 'Earphones'],
        'total_amount': 18999.0,
        'status': 'delivered'
    },
    'ORD105': {
        'customer_name': 'Vikram Rao',
        'items': ['Books', 'Notebook', 'Pen'],
        'total_amount': 780.0,
        'status': 'shipped'
    },
    'ORD106': {
        'customer_name': 'Sara Khan',
        'items': ['Handbag'],
        'total_amount': 2499.0,
        'status': 'pending'
    },
    'ORD107': {
        'customer_name': 'David Miller',
        'items': ['Headphones', 'Charger'],
        'total_amount': 3200.0,
        'status': 'delivered'
    }
}


for key,value in orders.items():
    if value["status"] == "delivered":
        print(f"Delivered Order: {key}, {value["customer_name"]}")
print("----------------------------")

for key,value in orders.items():
    if value["status"] == "pending":
        print(f"Pending Order: {key}, {value["customer_name"]}")
print("----------------------------")


total_revenue = 0

for key,value in orders.items():
    y = value["total_amount"]
    total_revenue = total_revenue + y
print(total_revenue)
print("-------------------------------")


items_count = {}

for key,value in orders.items():
    if value["status"] != "cancelled":
        items = value["items"]
        
        for a in items: 
            if a in items_count:
                items_count[a] = items_count[a] + 1
            else:
                items_count[a] = 1

print(items_count)

#l = len(orders) 
#for a in range(0,l + 1):     
cancelled_orders = []
for keys,values in orders.items():    
    if values["status"] == "cancelled":
        cancelled_orders.append(keys)
#         orders.pop(keys
# print(orders)
# cancelled_orders = ["ORD103"]

for a in cancelled_orders:
    del orders[a]
print(orders)

#for key,value in items.items():
   # print(key)
    #print(value)
    #if key in orders['ORD102']:
     #   value = value + 1
     