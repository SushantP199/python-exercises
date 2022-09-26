import gc


class Node:

    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insertAF(self, key, data):
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

    def insertBF(self, key, data):
        new_node = Node(data)
        ptr = self.head
        # preptr = ptr
        while ptr.data != key:
            # preptr = ptr
            ptr = ptr.next
        # preptr.next = new_node
        # new_node.prev = preptr
        # new_node.next = ptr
        # ptr.prev = new_node
        new_node.next = ptr
        ptr.prev.next = new_node
        new_node.prev = ptr.prev
        ptr.prev  = new_node

    def append(self, data):
        new_node = Node(data)
        temp = self.head
        if temp is not None:
            while temp.next is not None:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            new_node.prev = temp
        else:
            self.head = new_node

    def deleteNode(self, key):
        temp = self.head
        # case 1
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            temp = temp.next
        temp.prev.next = temp.next
        if temp is None:
            return
        if temp.next is not None:
            temp.next.prev = temp.prev
        temp = None
        gc.collect()

    def deleteBF(self, key):
        ptr = self.head
        while ptr.data != key:
            ptr = ptr.next
        preptr = ptr.prev
        if preptr == self.head:
            self.deleteNode(key)
        else:
            preptr.prev.next = ptr
            ptr.prev = preptr.prev
            del preptr

    def delete_dll(self):
        temp = self.head
        while temp is not None:
            self.head.prev = None
            ptr = temp.next
            del temp
            self.head = ptr
            temp = self.head
            # print(ptr.prev.data)

    def reverse_dll(self):
        curr = self.head
        while curr is not None:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        self.head = temp.prev

    def deleteAF(self, key):
        preptr = self.head
        while preptr.data != key:
            preptr = preptr.next
        if preptr.next is None:
            return
        ptr = preptr.next
        preptr.next = ptr.next
        if ptr.next is not None:
            ptr.next.prev = preptr
        del ptr

    def count(self, node):
        if not node:
            return 0
        else:
            return 1 + self.count(node.next)

    def drive_count(self):
        return self.count(self.head)

    def search(self, key):
        temp = self.head
        self.pos = 1
        while temp.data != key:
            self.pos += 1
            temp = temp.next
        print(f"Data {key} is at position {self.pos}")

    def dll_dcll(self):
        last = self.head
        while last.next is not None:
            last = last.next
            d = last.data
        self.head.prev = last
        last.next = self.head

    def display_dcll(self, node):
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
        return self.display_dcll(self.head)

    def display(self, node):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next


dll = DoublyLinkedList()
dll.push(2)
dll.push(5)
dll.append(3)
dll.append(7)
dll.insertAF(5, 1)
dll.display(Node(2))
dll.deleteNode(7)
print("After del 3")
dll.display(Node(2))
print("Insert be")
dll.insertBF(2, 7)
dll.display(Node(2))
print("del bef")
dll.deleteBF(1)
dll.display(Node(2))
print("del bef")
# dll.deleteAF(3)
# dll.display(Node(5))
# dll.search(3)
# print("del dll")
# dll.delete_dll()
# dll.display(Node(2))
print("rev dll")
# dll.reverse_dll()
dll.display(Node(2))
print("total nodes", dll.drive_count())
dll.dll_dcll()
dll.print_dcll()
