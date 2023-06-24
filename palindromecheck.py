def check_palin(string, start, end):
    if start >= end:
        return True
    if string[start] == string[end]:
        return check_palin(string, start + 1, end - 1)
    else:
        return False

if check_palin("12321", 0, 4):
    print("True")
else:
    print("False")
