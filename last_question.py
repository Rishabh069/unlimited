#Create a list named "numbers" containing the numbers 1, 3,5, 7, and 9.
# 2. Access and print the second element of the list.
# 3. Modify the third element of the list to 10.
# 4. Add the number 12 to the end of the list.
# 5. Remove the number 5 from the list.
# 6. Create a new list named "sliced_list" that contains a slice of
# the original list from the second to the fourth element.
# 7. Create a new list named "combined_list" by concatenating
# the original list with the sliced_list.
# 8. Check if the number 8 is present in the combined_list and
# print the result.
# 9. Sort the combined_list in ascending order.
# 10. Print the final version of the combined_list

# list = [1,3,5,7,9]

# print(list[1])

# list[2] = 10
# print(list[2])

# list.append(12)
# print(list)

# list.remove(list[2])
# print(list)

# sliced_list =list[2:4]
# print(sliced_list)


# combined_list =list+sliced_list
# print(combined_list)

# list.sort(reverse=True)
# print(list)

# print(8 in list)

my_list =[1,2,3,4,5,]
my_list[0]=99
print(my_list)


my_tuple = (1,2,3,4,5)
my_tuple2 = (99,1,2,3,4,5)
print(my_tuple+my_tuple2)

print(len(my_tuple))

count_1 = my_tuple.count(1)
print(count_1)

new_tuple = sorted(my_tuple,reverse=True)
print(new_tuple)
print(tuple(new_tuple))










