def find_even():
    sum = 0
    for i in range(2,51):
        if i%2 == 0:
            sum += i
    print ("sum is",sum)
find_even()
