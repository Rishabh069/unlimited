def check_prime(a):
    for i in range(2,int(a/2)+1):
        if a%i == 0:
            return False
    return True
if check_prime(77):
    print("PRIMEEEEEE")
else:
    print("NOT PRIMEEEE")


#WAP to give the multiplication table of 5, 10, 17
