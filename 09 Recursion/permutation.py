def fact(n):
    f = 1
    for i in range(2, n+1):
        f = f * i
    return f


def permutation(n, r):
    return ( fact(n) / fact(n-r) )


n = int(input("Enter number of items or inputs you have : "))
r = int(input("Enter number of permutation you have : "))

print(f"{n}P{r} = {int(permutation(n,r))}")

