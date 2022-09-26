def pattern_print(n):
    space = n//2 - 1
    pattern = 2
    for i in range(0,n//2):
        c=2
        while(c>0):
            for j in range(0,space):
                print(' ',end=" ")
            for k in range(0,pattern):
                print('*',end=" ")
            c -= 1
            print()
        space -= 1
        pattern +=2

n=int(input("Enter length of double sided staircase pattern : "))
pattern_print(n)


# var = value if (True) else value
