class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.count = 0
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head is not None:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node

    def append(self, data):
        new_node = Node(data)

        temp = self.head
        if temp is None:
            new_node.next = new_node
            self.head = new_node
            return
        while temp.next != self.head:
            temp = temp.next
        new_node.next = self.head
        temp.next = new_node

    def insertAF(self, key, data):
        new_node = Node(data)
        temp = self.head
        if self.head is not None:
            while temp.data != key:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    def insertBF(self, key, data):
        new_node = Node(data)

        if self.head is not None:
            temp = self.head
            # if key == temp.data:
            #     cll.push(data)
            #     return
            while temp.data != key:
                prev = temp
                temp = temp.next
            new_node.next = temp
            prev.next = new_node

    def deleteNode(self, key):
        temp = self.head
        prev = None

        while temp:
            if temp.data == key and temp == self.head:  # head deletion
                if temp.next == self.head:  # 1 - only one head elem
                    temp = None
                    self.head = None
                    return
                else:  # 2 - more than head elem
                    while temp.next != self.head:
                        temp = temp.next
                    temp.next = self.head.next
                    self.head = None
                    self.head = temp.next
                    return
            if temp.data == key:  # in between deletion
                prev.next = temp.next
                temp = None
                return
            if temp.next == self.head:
                break

            prev = temp
            temp = temp.next

    def delete_cll(self):
        curr = self.head
        while True:
            temp = curr.next
            while curr.next != self.head:
                curr = curr.next
            prev = curr
            del curr
            prev.next = temp
            self.head = prev.next
            curr = self.head
            if curr.next == self.head:
                del curr
                self.head = None
                break

    def count_nodes(self):
        temp = self.head
        self.count = self.count + 1
        while temp.next != self.head:
            self.count = self.count + 1
            temp = temp.next
        print("Total nodes = ",self.count)

    def rec_count_nodes(self, node):
        if node.next == self.head:
            return 1
        else:
            return 1 + self.rec_count_nodes(node.next)

    def driver_rec_count(self):
        return self.rec_count_nodes(self.head)

    def reverse_ll(self):
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

    def reverse_cll(self):
        # curr = self.head
        # while curr.next != self.head:
        #     curr = curr.next
        # prev = curr
        prev = None
        curr = self.head
        while True:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            if curr == self.head:
                curr.next = prev
                break
        self.head = prev

    def display(self):
        print("*CIRCULAR LINKED LIST*")
        temp = self.head
        # TODO do while implementation in python
        # while True
        while temp:
            print(temp.data)
            temp = temp.next
            if temp == self.head:
                break


cll = CircularLinkedList()
cll.push(3)
cll.push(5)
cll.push(1)
cll.append(9)
cll.display()
cll.insertAF(9, 4)
print("--------------------")
cll.display()
cll.insertBF(3, 0)
print("--------------------")
cll.display()
cll.deleteNode(5)
print("--------------------")
cll.display()
cll.count_nodes()
print("-----")
print(cll.driver_rec_count())
cll.display()
print("del_cll")
# cll.delete_cll()
# cll.display()
print("rev cll")
cll.reverse_cll()
cll.display()