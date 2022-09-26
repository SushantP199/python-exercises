def power(base, exp):
    if exp == 1:
        return base
    else:
    # if exp != 1:
        return (base * power(base, exp -1))


base = int(input("Enter a base value : "))
exp = int(input("Enter a power value : "))

print(f"{base}^{exp} = {power(base,exp)}")

