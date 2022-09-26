class Node:

    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class CircularDoublyLinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
        else:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            new_node.next = self.head
            new_node.prev = temp
            self.head.prev = new_node
            temp.next = new_node
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            new_node.next = self.head
            new_node.prev = temp
            temp.next = new_node
            self.head.prev = new_node

    def insert_after(self, key, data):
        new_node = Node(data)
        temp = self.head
        while temp.data != key:
            temp = temp.next
            if temp is None :
                print("previous node is does not exist")
                return
        new_node.next = temp.next
        if temp.next is not None:
            temp.next.prev = new_node
        temp.next = new_node
        new_node.prev = temp

    def insert_before(self, key, data):
        new_node = Node(data)
        temp = self.head
        if temp.data == key:
            self.push(data)
            return
        while temp.data != key:
            temp = temp.next
        new_node.prev = temp.prev
        new_node.next = temp
        temp.prev.next = new_node
        temp.prev = new_node

    def delete_node(self, key):
        temp = self.head
        # case 1 : deleting head
        if temp.data is key and temp is self.head:
            if temp.next is self.head:
                del temp
                self.head = None
                return
            else:
                while temp.next is not self.head:
                    temp = temp.next
                temp.next = self.head.next
                del self.head
                self.head = temp.next
                self.head.prev = temp
                return
        # case 2 : deleting in between
        while temp.data != key:
            temp = temp.next
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        # case 3 : deleting node is not present
        if temp.next == self.head:
            return
        del temp

    def delete_dcll(self):
        curr = self.head
        while curr.next is not self.head:
            last = curr.prev
            last.next = curr.next
            curr.next.prev = last
            del curr
            curr = last.next
            self.head = curr
        del curr
        self.head = None

    def reverse_dcll(self):
        curr = self.head
        while True:
            t = curr.data
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
            if curr is self.head:
                self.head = curr.next
                break

    def search(self, key):
        curr = self.head
        pos = 1
        if curr is not None:
            while curr.next is not self.head:
                if curr.data == key:
                    print(f"Data {curr.data} is found at position {pos}")
                    break
                curr = curr.next
                pos += 1

        if curr.next is self.head:
            print("Data is not found in list")

    def display(self, node):
        if node is not None:
            while True:
                print(node.data, end="  ")
                node = node.next
                if node == self.head:
                    break
        else:
            print("list is empty")
        print()

    def print_dcll(self):
        return self.display(self.head)


dcll = CircularDoublyLinkedList()
dcll.push(2)
dcll.push(7)
dcll.push(4)
dcll.append(1)
dcll.append(9)
dcll.print_dcll()
dcll.insert_before(7, 5)
dcll.print_dcll()
print("aft del")
dcll.delete_node(9)
dcll.print_dcll()
dcll.insert_after(2, 0)
dcll.insert_after(0, 1)
dcll.insert_after(1, 7)
dcll.print_dcll()
dcll.insert_before(1, 3)
dcll.print_dcll()
dcll.delete_node(3)
dcll.print_dcll()
# dcll.delete_dcll()
# dcll.print_dcll()
dcll.reverse_dcll()
dcll.print_dcll()
dcll.search(11)