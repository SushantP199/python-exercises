def character_count(string):
    string = str(string)
    l=[]
    if string == "":
        print("string should contains at least one character")
        character_count(input("Enter a string : "))
    else:
        for i in range(0,len(string)):
            char = string[i]
            if char not in string[i-1:0:-1]:
                count = 0
                for c in string:
                    if c == char:
                        count += 1
                print(f"character count of {char}:={count}")

character_count(input("Enter a string : "))




















