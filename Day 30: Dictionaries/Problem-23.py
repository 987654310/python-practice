my_dict = {'x': 100, 'y': 200}
key_to_check = input('Enter a key: ')

if key_to_check not in my_dict:
    print(f"{key_to_check} does not exist in the dictionary")
else:
    print(f"{key_to_check} does exist in the dictionary")