from sys import argv # Import argument vector from system library. Argument vector is an array that contains the extra arguments inserted into the execution command.

filename = argv[1] # Assigning the name of the file to "filename", which is the second argument. The first argument is always the name of the program.

file = open(filename) # Opening the file with the filename.

print(f"Here's the content of your file {filename}: \n")

print(file.read())

file.close() # Closing the file stream.


#You can also use input instead of command line arguments

filename = input("Write the name of the file you want to read: ")

file = open(filename)

print(f"Here's the content of your file {filename}: \n")

print(file.read())

file.close() # Closing the file stream.