def max(a, b):
    return a if a > b else b

def lcm(a, b):
    i = max(a, b)
    if ( (i % a == 0) and (i % b == 0) ):
        return i
    elif a > b:
        return lcm(a + i, b)
    else:
        return lcm(a, b + i)

# a, b = input("Enter any two number of lcm you want : ").split()
a, b = 12, 8

print(f"LCM of {a} and {b} => {lcm(int(a), int(b))}")

