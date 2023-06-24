def jos(n, k):
    if n == 1:
        return 0
    else:
        return (jos(n - 1, k) + k) % n

def myJos(n, k):
    return jos(n, k) + 1

print(myJos(5, 3))

# alternatively if there are 41 people then 41-32 =9 ,2*9+1 will win
# for 9 , 3 will Win 
# therom for 2**n always 0 will Win 
# another way 9 1001 change bin to 0011 ie make the first bit last one this will win    