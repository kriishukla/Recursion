def printSub(str, curr, index):
    if index == len(str):
        print(curr, end=" ")
        return

    printSub(str, curr, index + 1)
    printSub(str, curr + str[index], index + 1)

str = "ABC"
printSub(str, "", 0)
    