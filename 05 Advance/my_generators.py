import random

heros = ["Batman","Hulk","Thor"]

for h in heros:
    print(h)

# print(list(range(6)))

# Generator method which creates iterator
def magic():
    for i in range(4):
        # return random.randint(1, 20)
        yield random.randint(1, 20) # To create

for number in magic():
    print(f"Values is {number}")
