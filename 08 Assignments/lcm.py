def max(a, b):
    return a if a > b else b

def lcm(a, b):
    m = max(a,b)
    for i in range(m, m*10, m):
        if ( (i % a == 0) and (i % b == 0) ):
            l = i
            break
    return l

a, b = input("Enter any two number of lcm you want : ").split()

print(f"LCM of {a} and {b} => {lcm(int(a), int(b))}")

