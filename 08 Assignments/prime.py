n = int(input("Enter you number : "))

if n > 1 :
    for i in range(2,n):
        if (n%i==0):
            print(f"{n} is not a prime number")
            break
        else:
            print("%d number is prime number" %int(n))
            break