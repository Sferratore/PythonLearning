# Creating a dictionary. A dictionary is a data structure that contains name-value pairs
my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Accessing values by keys
name = my_dict['name']  # Access the value associated with the 'name' key
age = my_dict['age']  # Access the value associated with the 'age' key

# Modifying values
my_dict['age'] = 31  # Update the value associated with the 'age' key

# Adding new key-value pairs
my_dict['country'] = 'USA'  # Add a new key 'country' with the value 'USA'

# Removing a key-value pair
del my_dict['city']  # Delete the key 'city' and its associated value

# Checking if a key is in the dictionary
has_name = 'name' in my_dict  # Returns True if 'name' is a key in the dictionary

# Getting the keys and values as lists
keys = list(my_dict.keys())  # Get a list of keys: ['name', 'age', 'country']
values = list(my_dict.values())  # Get a list of values: ['Alice', 31, 'USA']

# Getting key-value pairs as tuples
items = list(my_dict.items())  # Get a list of key-value pairs: [('name', 'Alice'), ('age', 31), ('country', 'USA')]

# Creating a copy of the dictionary
dict_copy = my_dict.copy()

# Clearing all key-value pairs from the dictionary
my_dict.clear()

# Printing the dictionary and its properties
print("Original Dictionary:", dict_copy)
print("Modified Dictionary:", my_dict)