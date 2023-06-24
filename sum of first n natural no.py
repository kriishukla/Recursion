def sumofn(x):
    if x == 0:
        return 0
    sum = x + sumofn(x-1)
    return sum

print(sumofn(10))
# alt n(n+1)/2