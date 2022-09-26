num = int(input("Enter your number : "))

print(f"MULTIPLICATION TABLE OF {num}")
for i in range(1,11):
    #mul_table =num*i 
    print(num*i)
    #print(num,"x",i,"=",num*i)

"""
num = input("Enter your number : ")
O/P for num as input string
Enter your number : 5
MULTIPLICATION TABLE OF 5
5
55
555
5555
55555
555555
5555555
55555555
555555555
5555555555
"""
"""mul_table = []
for i in range(1,11):
    mul_table = mul_table+[num*i]
    print(mul_table[i-1])"""

"""
#FOR upto entered number multiplication
for i in range(1,11):
    for j in range(1,num+1):
        m = i*j
        if (len(str(m)) == 1):
            print("  ",m,end="\t")
        if (len(str(m)) == 2):
            print(" ",m,end="\t")
        if (len(str(m)) == 3):
           print("",m,end="\t")
        print("[",len(str(m)),"]",end="\t")
    print()
"""
