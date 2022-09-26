score=int(input("Enter your score "))

if score<60:
    print(f"Your score is {score} (< 60) hence not qualified the course" )
else:
    print(f"Congrats!!! your score is {score} and you qualified the course")

# Assignments

feedback=int(input("Give us your feedback for our restaurant either 0 or 5 =>"))

if feedback==0:
    print("Suggest us please what should we improve")
elif feedback==5:
    print("Thanks !!! Visit Again")
else:
    print("feedback  either 0 or 5")

# Rating system

print("A LCO PYTHON 3 COURSE GIVE UR RATING")
rating=int(input("Enter rating B/W 1 - 5 : "))

if rating==1:
    print("Sorry to hear about your experiences")
elif rating==2:
    print("We are trying to go better")
elif rating==3:
    print("Thanks!")
elif rating==4:
    print("We almost missed the perfect rating from you ...")
elif rating==5:
    print("Happy to know that you loved our services  !!!!!")
else :
    print("Please give rating B?W 1 - 5")