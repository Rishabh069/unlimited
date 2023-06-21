# Write a program that prompts the user to enter their
# name and their favorite color. Then, create a message that
# combines their name and favorite color to form a personalized
# message. Finally, print the message on the console.

user_name =str(input("Enter your name",))
fav_color =str(input("what is your favorite color",))
print(f"Hi {user_name}")
print(f"Your favorite color is {fav_color}")

# Write a program that prompts the user to enter a
# sentence. Count and display the number of words in the
# sentence

user_set= str(input("Write the number of words"))
splitted = user_set.split(" ")
print(len(splitted))

# : Write a program that prompts the user to enter their
# full name (first name and last name). Convert the name to
# uppercase and display it in reverse order with a comma
# separating the last name and the first name.

full_name = str(input("write your first name and last name"))
f_name,l_name = full_name.split(" ")
upp_fname = f_name.upper()
upp_lname = l_name.upper()
print (f"{upp_lname},{upp_fname}")

# Question 4: Write a program that takes a sentence as input and
# replaces all occurrences of a specific word with another word.
# Prompt the user to enter the original sentence, the word to be
# replaced, and the replacement word. Display the modified
# sentence

sentence = str(input("Write your own sentence"))
replace = str(input("write what do u want to replace the word "))
replacement = str(input("write what do u want to replace the word with?"))
replaced = sentence.replace(replace, replacement)
print (replaced)








