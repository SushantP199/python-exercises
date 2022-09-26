
lower_range = int(input("Enter lower range : "))
upper_range = int(input("Enter upper range : "))

print("Prime number between %d and %d" %(lower_range,upper_range) )
for number in range (lower_range,upper_range+1):
    if number > 1 :
        for i in range (2,number) :
            if number%i == 0 :
                break
            else:
                print(number)
                break


