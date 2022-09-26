superhero = (1,2,3,4)

print(superhero)

def getSquare(num):
    return num*num

result = map(getSquare, superhero)

resultMod = set(result)

print(resultMod)

s ={None} # define an empty set
print(type(s))

