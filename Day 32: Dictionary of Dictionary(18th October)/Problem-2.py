customer_carts = {
    'amit_123': ['laptop', 'mouse', 'headphones'],
    'riya_456': ['dress', 'lipstick', 'lipstick', 'earrings'],
    'john_p': ['t-shirt', 'jeans', 'jeans'],
    'nina_m': [],
    'arun_dev': ['laptop', 'mouse', 'keyboard', 'laptop'],
    'sara_k': ['sofa', 'dining table', 'lamp'],
    'mike90': ['football', 'football', 'sports shoes'],
    'priya_s': ['saree', 'bangles', 'earrings', 'bangles'],
    'lee_wong': ['smartphone', 'charger', 'phone case', 'charger'],
    'emily_r': [],
    'tony_stark': ['arc reactor', 'iron suit', 'helmet', 'helmet'],
    'bruce_wayne': ['batmobile', 'grappling gun'],
    'clark_kent': ['glasses'],
    'diana_p': ['shield', 'sword', 'bracelets'],
    'steve_r': ['notebook', 'pen', 'sticky notes', 'highlighter'],
    'joker_x': ['playing cards', 'toy gun', 'hat'],
    'harley_q': ['hammer', 'lipstick', 'hat'],
    'flash_21': ['running shoes', 'energy drink'],
    'aquaman7': ['trident', 'water bottle'],
    'thor_odin': ['hammer', 'cape', 'hammer', 'armor'],
    'hulk_smash': ['protein powder', 'dumbbells', 't-shirt'],
    'natasha_r': ['black suit', 'gloves'],
    'vision_v': ['mind stone', 'cape'],
    'wanda_m': ['spell book', 'bracelet', 'necklace'],
    'peter_parker': ['camera', 'spider suit', 'web fluid', 'web fluid'],
    'rocket_raccoon': ['blaster', 'ammo kit', 'goggles'],
    'groot_g': ['plant pot', 'fertilizer'],
    'starlord_99': ['headphones', 'mix tape', 'helmet'],
    'gamora_g': ['sword', 'knife'],
    'drax_d': ['axe', 'protein bar'],
    'sam_w': ['drone', 'wings'],
    'bucky_b': ['metal arm oil', 'knife'],
    'shuri_w': ['vibranium tech', 'gloves', 'tool kit'],
    'okoye_o': ['spear', 'shield'],
    'tchalla_k': ['vibranium suit', 'ring'],
    'strange_s': ['magic cloak', 'spell book'],
    'loki_l': ['dagger', 'helmet', 'cape', 'scepter'],
    'hela_h': ['helmet', 'sword'],
    'thanos_t': ['infinity gauntlet', 'space stone', 'power stone'],
    'nick_fury': ['eye patch', 'pistol'],
    'agent_coulson': ['badge', 'car keys'],
    'wanda_vision': ['spell book', 'cape', 'bracelet']
}

empty_cart = []
for key, value in customer_carts.items():
    if len(value) == 0:
        empty_cart.append(key)

for a in empty_cart:
    del customer_carts[a]
print(customer_carts)  

print("-----------------------------------")
items_count = {}
for key, value in customer_carts.items():    
    b = value
    for a in value: 
        if a in items_count:
            items_count[a] = items_count[a] + 1
        else:
            items_count[a] = 1
print(items_count)
print("-----------------------------------")

cart_sizes = {}
items = []
for key, value in customer_carts.items():
    unique = []    
    for a in value:
        if a not in unique:
            unique.append(a)
    cart_sizes[key] = len(unique)
print(cart_sizes)
print("-----------------------------------")

for key, value in customer_carts.items():
    new_list = []
    for item in value:
        if item not in new_list:
            new_list.append(item)
    customer_carts[key] = new_list

print(customer_carts)


######################
#for key, value in customer_carts.items():
#     new_list = []
#     for item in value:
#         if item not in new_list:
#             new_list.append(item)
#     customer_carts[key] = new_list

# print(customer_carts)


