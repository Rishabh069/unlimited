# #WAP to find area of circle with radius 7.5, 8.97, 20.39, 100, 129, 139, 600, 1000, 5.6, 8.9, 12.7, 11.12, 12.13.
# radius = [7.5, 8.97, 20.39, 100, 129, 139, 600, 1000, 5.6, 8.9, 12.7, 11.12, 12.13]
# pie= 3.14
# for i in range(len(radius)):
#     print (f"The area of the circle with radius {radius[i]} is {pie*radius[i]**2}")


# for i in radius:
#     print (f"The area of the circle with radius [i] is {pie*i**2}")


# from copy import deepcopy
# list_a = [1,2,3,4,5]
# list_b = deepcopy(list_a) #yesma chai list_b = list_a garyo vane chai same to same auuxa 
# list_b[0]="ram"
# print ("list_b",list_b)
# print ("list_a",list_a)

# t_list = (1,2,3,4,5,6)
# for j,i in enumerate(t_list):
#     print (j,i)
# print(j,i)

# list = [1,2,3,4,5,6,2,3,4,5]
# print (set(list))
# print (list)

# a = [1,2,3,4,5,6,7,8,9,10]
# b = [4,5,67,8,9,10,11,12,13]
# c = [0,0,0,0,0,0,0,0,0,0,0]
# for i in range (0,10):
#     for j in range (0,10):
#         for k in range (0,10):
#             print (i,j,k)

a = [[1,1,1],[2,2,2,],[3,3,3]]
print (a)
for i in range (0,3):
    for j in range (0,3):
        a[i][j] =1+a[i][j]
print (a)

a= [[i+a[i][j] for j in range (3)] for i in range (0,3)]
list = [2,3,4,5,6]
a = (x**2 for x in list)
print (a)

number = 9 
if number < 0:
    print ("number is negative")
elif number == 0:
    print ("number is zero")
else:
    print ("number is odd")
    