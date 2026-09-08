def right_aligned_alphabet_triangle(n):
    for i in range(1,n+1):
        print(""*(n-i),end="")
        for j in range(i):
            print(chr(65+j),end="")
        print()    
right_aligned_alphabet_triangle(6)
