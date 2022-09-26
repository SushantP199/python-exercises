# application : In recursio
# Expression Evaluation
# Expression Conversion
#     i. Infix to Postfix
#     ii. Infix to Prefix
#     iii. Postfix to Infix
#     iv. Prefix to Infix
# Backtracking
# Memory Management


class Stack:

    def __init__(self, max):
        self.top = -1
        self.max = max
        self.stack = []

    def push(self, data):
        if self.top == self.max - 1:
            print("Stack is overflow")
        else:
            self.top += 1
            self.stack.insert(self.top, data)

    def pop(self):
        if self.top == -1:
            print("Stack is underflow")
        else:
            temp = self.stack[self.top]
            self.top -= 1
            return print(f"popped data item is {temp}")

    def multi_push(self):
        n = int(input("Enter number of elements you want to push"))
        while n > 0:
            data = int(input("Enter data = "))
            self.push(data)
            n -= 1

    def multi_pop(self):
        n = int(input("Enter number of elements you want to pop"))
        while n > 0:
            self.pop()
            n -= 1

    def display(self):
        print("*** STACK ***")
        if self.top != -1:
            i = self.top
            while i > -1:
                print(self.stack[i])
                i -= 1


max=int(input("Enter maximum number of elem you want in stack = "))
s = Stack(max)
s.push(3)
s.push(1)
s.push(9)
s.display()
s.pop()
s.pop()
s.pop()
s.pop()
s.multi_push()
s.display()
s.multi_pop()
