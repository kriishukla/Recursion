def countSubsets(arr, n, total):
    if n == 0:
        return 1 if total == 0 else 0
    
    return countSubsets(arr, n - 1, total) + countSubsets(arr, n - 1, total - arr[n - 1])

n = 3
arr = [10, 20, 15]
sum = 25

print(countSubsets(arr, n, sum))
