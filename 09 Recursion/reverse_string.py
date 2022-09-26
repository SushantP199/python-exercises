def reverse(string):
    return string[::-1]

def reverse_2(string):
    str = ""
    for i in string:
        str = i + str
    return str

print(reverse_2('squad'))