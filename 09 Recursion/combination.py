def fact(n):
    res = 1
    for i in range(2, n + 1):
        res = res * i
    return res


def combination(n, r):
    return ( fact(n) / ( fact(r) * fact(n - r) ) )


n = int(input("Enter total number of items : "))
r = int(input("Enter number of items of combinations you want : "))

print(f"{n}C{r} = {int(combination(n,r))}")