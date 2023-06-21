
#write a program to find the datatypes and take the random input 
#can you perform the addition of string and integer ?
#write a program to find the ascii value of characters of your name 
#WAP to perform the addition of first 20 numbers 
#WAP to show use case of boolean datatypes
#WAP to take input from the user and render hello "afno name"
#WAP to convert string to integer, float lai integer 





#write a program to find the datatypes and take the random input 
import random

def get_data_type(value):
    return type(value).__name__

def generate_random_input():
    data_type = random.choice([int, float, str, bool, list, tuple, dict])

    if data_type == int:
        return random.randint(-100, 100)
    elif data_type == float:
        return random.uniform(-100, 100)
    elif data_type == str:
        return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5))
    elif data_type == bool:
        return random.choice([True, False])
    elif data_type == list:
        return random.sample(range(10), random.randint(1, 5))
    elif data_type == tuple:
        return tuple(random.sample(range(10), random.randint(1, 5)))
    elif data_type == dict:
        return {i: random.randint(1, 10) for i in random.sample('abcdefg', random.randint(1, 5))}

value = generate_random_input()
data_type = get_data_type(value)

print("The data type of the input is:", data_type)