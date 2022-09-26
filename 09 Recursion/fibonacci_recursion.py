def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


count = int(input("Upto what number fibonacci series you want : "))
# count=6
if count <= 0:
    print("Please enter more than 0 ")
else:
    # sum = 0
    for i in range(count):
        print(fibonacci(i), end=" ")
        # last_value = fibonacci(i)
        # sum = sum + fibonacci(i)
    # print(last_value)
    # print(sum)

# print(fibonacci(6)) could not give value at position 7 i.e.(n+1) instead of 6 i.e. (n)
