# application
# other : printer, task scheduling algorithm

class Queue:

    def __init__(self, max):
        self.rear = -1
        self.front = -1
        self.max = max
        self.queue = []

    def insert(self, data):
        if self.rear == max - 1:
            print("Queue is overflow")
        elif self.rear == -1:
            self.rear = 0
            self.front = 0
        else:
            self.rear += 1
        self.queue.insert(self.rear, data)

    def delete(self):
        if self.front == -1:
            print("Queue is underflow")
            return -1
        else:
            if self.front > self.rear:
                print("Queue is underflow")
                return
            print("Deleted item = ", end=" ")
            temp = self.queue[self.front]
            self.front += 1
            return temp

    def peak(self):
        if self.rear != -1:
            print("Peak element = ", end=" ")
            return self.queue[self.front]

    def display(self):
        print("*** QUEUE ***")
        if self.rear != -1 :
            for i in range(self.front, self.rear + 1) or self.rear <= self.front:
                print(self.queue[i])


max = int(input("Enter maximum number element you want in queue = "))
q = Queue(max)
q.insert(5)
q.insert(1)
q.insert(3)
q.display()
print(q.peak())
print(q.delete())
print(q.delete())
print(q.delete())
print(q.delete())