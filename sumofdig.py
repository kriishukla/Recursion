def sumofdig(x):
    if x==0:
        return 0
    return x%10 + sumofdig(x//10)
print(sumofdig(12321))