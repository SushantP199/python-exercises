import math

print(abs(-7))
print(math.fabs(-13))

print(math.floor(21.22))
print(math.floor(-21.22))

print(math.ceil(19.2))
print(math.ceil(-19.2))

print(max([1,2,30,4,5,11]))
print(min([1,2,30,4,5,11]))

# SQRT
print(math.sqrt(9))

#square root of natural numbers
x=int(input("enter a number "))
x1=1
for i in range(1,x):
    x1=x/i;
    #if (x1*x1)==x:
    if x1==i:
        break;

print(f"square root of {x} is {x1}")