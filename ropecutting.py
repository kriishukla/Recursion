def ropecut(n,x,y,z):
    if n<0:
        return -1
    res=max(ropecut(n-x,x,y,z),ropecut(n-y,x,y,z),ropecut(n-z,x,y,z))
    return res+1
print(ropecut(23,11,1,12))