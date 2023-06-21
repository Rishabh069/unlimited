def check_prime(a):
    for i in range(2,a):
        if a%i == 0:
            return False
        return True
if check_prime(10):
    print ("prime")
else:
    print ("not prime")

    
