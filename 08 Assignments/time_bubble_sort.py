time = [66, 57, 54, 53, 64, 52, 59]
print("Shoshanna last week score list of trsck training is",time)

n=len(time)
for i in range(0,n):
    for j in range(0,n-i-1):
        if time[j]<time[j+1]:
            time[j],time[j+1] = time[j+1],time[j]

print("\nShoshanna last week sorted score list of trsck training is",time)
print("\nShoshanna best score is {} sec".format(time[0]))

""" O/P:
Shoshanna last week score list  of trsck training is [66, 57, 54, 53, 64, 52, 59]
Shoshanna best score is 66 sec
"""
