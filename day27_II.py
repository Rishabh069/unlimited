# # WAP to show multiplication table of first 20 prime numbers using nested for loop
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number%i == 0:
            return False
    return True
    

count = 0
number = 1
prime_list = []
while count <20:
    if is_prime(number):
        prime_list.append(number)
        count = count + 1
    number = number + 1
print(prime_list)
for l in prime_list:
    for j in range(1,11):
        print(f"{l}*{j}={l*j}")
        
list=[]
for j in range(20,30):
    prime=True
    for i in range(2,j):
        if j%i == 0:
            prime=False
            break
    if prime == 1:
        list.append(j)
print(list)

# #WAP to find a simple intrest 
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (in percentage): "))
time = float(input("Enter the time period (in years): "))
intrest = principal*time*rate/100
print(intrest)


#WAP to find peremeter of a recetangular ground
length = float(input("Length:"))
breath = float(input("Breath:"))
parameter = 2*(length+breath)
print(parameter)


#WAP to find volume of irregular body 
#how to find volume of irregular body
#WAP to calculate volume of a cube
length = float(input("Length:"))
volume = length**3
print(volume)

#WAP to find square root of a number
import math
num = float(input("Number:"))
sqr = math.sqrt(num)
print(sqr)

#WAP to find error percentage 
approximate_value = float(input("Enter the approximate value: "))
exact_value = float(input("Enter the exact value: "))
absolute_error = abs(approximate_value - exact_value)
error_percentage = (absolute_error / exact_value) * 100
print("Error Percentage:", error_percentage, "%")

#take a string as input from user and check whether  the string is Rishabh_karki or not 
full_name = str(input("write your first name and last name"))
if full_name == "Rishabh_karki":
    print("The string is equal to 'Rishabh_karki'.")
else:
    print("The string is not equal to 'Rishabh_karki'.")









