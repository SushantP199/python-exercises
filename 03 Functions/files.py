def main():
    file = open("lco.txt","a")
    for i in range(20):
        file.write(f"This is line {i+1}\n")
    file.close()

    # TODO read file
    file = open ("lco.txt","r")
    if file.mode == 'r':
        filecontent = file.read()
        print(filecontent)
    file.close()

    # TODO exception
    try:
        file = open("lco.txt", "r")
    except IOError:
        print("File does not exist")
    else :
        print("Success in reading...")
    finally:
        print("Your are transacted in finally")





if __name__== "__main__":
    main()

# print("before import")
# import math
#
# print("before functionA")
# def functionA():
#     print("Function A")
#
# print("before functionB")
# def functionB():
#     print("Function B {}".format(math.sqrt(100)))
#
# print("before __name__ guard")
# if __name__ == '__main__':
#     functionA()
#     functionB()
# print("after __name__ guard")