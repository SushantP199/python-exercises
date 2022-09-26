# Euclid's method


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


a, b = input("Enter any two numbers : ").split()

print("GCD of {} and {} => {}".format(a, b, gcd(int(a),int(b))))
