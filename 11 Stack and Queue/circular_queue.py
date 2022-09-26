#   34, 35, 46, 67, 78, 89, 23, 34
#   0,   1,  2,  3,  4,  5,  6,  7
#        R   F
#
#   ( rear + 1 ) % size == front
#   2 % 8 == 2
#       2 == 2


class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return
        elif self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Queue is underflow")
            return
        elif self.front == self.rear:
            temp = self.queue[self.rear]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.rear]
            self.front = (self.front + 1) % self.size
            return temp

    def display(self):
        print("*** CIRCULAR QUEUE ***")
        if self.front != -1:
            if self.front <= self.rear:
                for i in range(self.front, self.rear + 1):
                    print(self.queue[i])
            else:
                for i in range(self.front, self.size):
                    print(self.queue[i])
                for i in range(0, self.rear + 1):
                    print(self.queue[i])


size = int(input("Enter size of queue : "))
cq = CircularQueue(size)
cq.display()
cq.enqueue(1)
# cq.enqueue(2)
# cq.enqueue(3)
# cq.enqueue(5)
# cq.enqueue(6)
cq.display()
cq.dequeue()
cq.display()
cq.enqueue(9)
cq.display()
# cq.dequeue()
# cq.dequeue()
# cq.display()