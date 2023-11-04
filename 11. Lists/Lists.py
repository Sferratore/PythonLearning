# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements by index
first_element = my_list[0]  # Access the first element (1)
last_element = my_list[-1]  # Access the last element (5)

# Slicing a list to create a new list
sub_list = my_list[1:4]  # Creates a new list with elements [2, 3, 4]

# Modifying elements
my_list[2] = 9  # Modifies the third element to be 9

# Adding elements to the end of the list
my_list.append(6)  # Appends 6 to the end of the list

# Extending a list with another list
extension = [7, 8]
my_list.extend(extension)  # Extends the list with [7, 8]

# Inserting an element at a specific position
my_list.insert(2, 10)  # Inserts 10 at index 2, shifting other elements

# Removing an element by value
my_list.remove(4)  # Removes the first occurrence of 4 from the list

# Removing an element by index
popped_element = my_list.pop(3)  # Removes and returns the element at index 3 (5 in this case)

# Finding the index of an element
index_of_3 = my_list.index(6)  # Returns the index of the first occurrence of 

# Checking if an element is in the list
contains_7 = 7 in my_list  # Returns True if 7 is in the list

# Finding the length of the list
list_length = len(my_list)

# Reversing the list in place
my_list.reverse()

# Sorting the list in ascending order
my_list.sort()

# Sorting the list in descending order
my_list.sort(reverse=True)

# Creating a copy of the list
list_copy = my_list.copy()

# Clearing all elements from the list
my_list.clear()

# Printing the list and its properties
print("Copy of the List:", list_copy)
print("Cleared List:", my_list)