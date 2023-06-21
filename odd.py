def find_odd(a,b):
    sum = 0
    for i in range(a,b):
        if i%2!=0:
            sum += i
    print("sum is",sum)
find_odd(2,51)
