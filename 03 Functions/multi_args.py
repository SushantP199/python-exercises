# def addition (n1,n2,n3=0,n4=0,n5=0):
#     "Addition of numbera"
#     sum = n1+n2+n3+n4+n5
#     return sum


# def addition(*num):
#     """Addition of numbera"""
#     """num is tuple """
#     sum = 0
#     for i in num:
#          sum = sum + i
#     return sum
#
# print(addition(2,3,4,5,6,7,8,8))
#

def subtraction (*num):
    price=100
    for i in num :
        price=price-i;
    return price

print( "Net price is %s " %str(subtraction(20,30,9)))

def subtraction (num,*NUM):
    print(num)
    print(NUM)
    return

subtraction(2,3,4)