def min(a, b):
    return a if a < b else b


def gcd(a, b):
    for i in range(1, min(a, b)+1):
        if ( (a % i == 0) and (b % i == 0) ):
            g = i
    return g


a, b = input("Enter any two number of gcd you want : ").split()

print(f"GCD of {a} and {b} => {gcd(int(a),int(b))}")

lcm = (int(a) * int(b) ) / gcd(int(a),int(b))
print(f"LCM of {a} and {b} => {int(lcm)}")