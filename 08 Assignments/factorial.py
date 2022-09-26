number = int(input("Enter your number : "))

# easy and hard and excellence
#fact = 1
# medium
fact = number

if fact < 1 :
    print("We don't calculate factorial for negative number")
elif number == 0 :
    print("Factotial is 1")
else:
    # easy
    # for i in range(1,number+1):
    #     fact=fact*i
    # print(f"The factorial is {fact}")
    # medium
    # for i in range(number,1,-1):
    #     fact=fact*(i-1)
    # print(f"The factorial is {fact}")
    # hard
    # i=1
    # while i<=numb)er :
    #     fact = fact * i
    #     i -= -1
    # print(f"The factorial is {fact}")
    #excellence
    while (number > 1):
        fact *= (number := number-1)
    print(f"The factorial is {fact}")
    