def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


rbc = 5000000
wbc = 8000

ratio_factor = gcd(rbc, wbc)

print(f"WBC : RBC = {int(wbc/ratio_factor)} : {int(rbc/ratio_factor)}")
