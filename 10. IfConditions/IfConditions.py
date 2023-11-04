#Show use of if, else and elif.

cats = input("Insert number of cats: ")
dogs = input("Insert number of dogs: ")

if cats > dogs:    #Checks a condition
    print("Meow!")
elif cats < dogs: # If first condition is not met, then checks another condition
    print("Woof!")
else:  #If the two conditions are not met, does defined actions.
    print("There is the same number of cats as dogs!")