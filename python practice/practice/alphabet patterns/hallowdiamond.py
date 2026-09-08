def hallow_dimond(n):
    width=2*n-1
    for i in range(n):
        for j in range(width):
            if i==0 or i==n-1:
                print("*",end="")
            elif j==i or j==width-1-i:
                print("*",end="")
            else:
                print("",end="")
        print()
    for i in range(n-2,-1,-1):
        for j in range(width):
            if i==0:
                print("*",end="")
            elif j==width-1-i:
                print("*",end="")
            else:
                print("",end="")
        print()
n=4      
hallow_dimond(n)
