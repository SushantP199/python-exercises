def add(num1,num2):
    num1 = int(input("Enter your 1st number : "))
    num2 = int(input("Enter your 2nd number : "))
    return num1+num2

def sub(num1,num2):
    num1 = int(input("Enter your subtractor number : "))
    num2 = int(input("Enter your subtrahend number : "))
    return num1 - num2

def mul(num1,num2):
    num1 = int(input("Enter your multilplicand number : "))
    num2 = int(input("Enter your multiplyer number : "))
    return num1 * num2

def div_f(num1,num2):
    num1 = int(input("Enter your dividend number : "))
    num2 = int(input("Enter your divisor number : "))
    return num1 / num2

def div_i(num1,num2):
    num1 = int(input("Enter your dividend number : "))
    num2 = int(input("Enter your divisor number : "))
    return num1//num2

def mod(num1,num2):
    num1 = int(input("Enter your number : "))
    return num1%num2

def square(num1):
    num1 = int(input("Enter your perfect square number : "))
    return num1**2

def sqrt(num):
    n = 1
    for i in range(1,num):
        n=num/i;
        if(i==n):
            break
    return i

# simple calculator
ch=0
while ch<=6:
    print("***SIMPLE CALCULATOR***\n")
    print("1.ADD\n2.SUBTRACT\n3.MULTIPLICATION\n4.DIVISION\n5.(INTERGER)DIVISION\n5.MODULO\n6.SQUARE\n7.SQUARE ROOT\n0.Exit\n")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        print(f"ADDITION IS {add(num1, num2) }")
    elif ch == 2:
        print(f"SUBTRACTION IS {sub(num1, num2) }")
    elif ch == 3:
        print(mul(num1, num2))
    elif ch == 4:
        print(div_f(num1, num2))
    elif ch == 5:
        print(div_i(num1, num2))
    elif ch == 6:
        print(square(num1))
    elif ch == 7:
        print(sqrt(num1))
    elif ch == 0:
        break
    else:
        print("Enter choice between 1 and 7")

