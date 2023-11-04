#Shows various types of loops

# Print numbers from 1 to 5 using a while loop
num = 1
while num <= 5:
    print(num)
    num += 1

# Simulate a do-while loop to get user input until 'quit' is entered
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break

# Using a for loop with a counter
for i in range(5):  # This will iterate from 0 to 4
    print(i)

# Iterate through a list with a for loop without counter
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)