# Copying content of a file into another.

from_file = input("File to copy: ")

to_file = input("File to write to: ")

print(f"Copying from {from_file} to {to_file}")

in_data = open(from_file)

out_data = open(to_file, 'w') # Opening file in write mode

data_to_copy = in_data.read()

print(f"The input file is {len(data_to_copy)} bytes long") # length method used to define length of the data.

out_data.write(data_to_copy)

in_data.close()

out_data.close()

print("All done.")