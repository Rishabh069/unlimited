#Define a tuple named my_tuple with the following elements: 10,20, 'a', 'b', True.
my_tuple = (10,20, "a", "b", True)
print(my_tuple)

#Write the code to access and print the third element of the tuple my_tuple.
print(my_tuple[2])

# Concatenate two tuples: tuple1 with elements (1, 2, 3) and tuple2 with elements ('x', 'y', 'z'). Store the result in a new tuple called concatenated_tuple.
tuple1 = (1,2,3)
tuple2 = ("x", "y", "z")
concatenated_tuple = tuple1 + tuple2
print (concatenated_tuple)

# Write a Python code snippet to repeat the tuple my_tuple three times and store the result in a new tuple named repeated_tuple.
print (tuple1 *3)

#Determine the length of the tuple concatenated_tuple using a built-in function and print the result.
print (len(tuple1))

# Perform slicing on the tuple my_tuple to extract a new tuple with elements 'a', 'b', and True. Store the result in a variable called sliced_tuple
print (my_tuple[2:4])