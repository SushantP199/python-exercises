def factorial(n):
    if n == 1 :
        # return 1 not better or programmatic
        return n
    else:
        return n * factorial(n - 1)


number = int(input("Enter your number of which factorial you want to calculate : "))

if number < 0:
    print("Factorial of negative number does not exist")
elif number == 0:
    print("Factorial of 0! = 1")
else:
    print(f"Factorial of {number}! = {factorial(number)}")
