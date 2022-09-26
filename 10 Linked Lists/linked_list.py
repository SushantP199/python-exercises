class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    # TODO insert before
    def insertBF(self, key_value, new_value):
        new_node = Node(new_value)
        temp = self.head
        while temp.data != key_value:
            prev = temp
            temp = temp.next
            if temp is None:
                print(f"Previous node {prev_node} given by does not exist")
                break
        if temp is not None:
            new_node.next = temp
            prev.next = new_node

    def insertAF(self, prev_node, new_value):
        new_node = Node(new_value)
        temp = self.head
        while temp.data != prev_node:
            temp = temp.next
            if temp is None:
                print(f"Previous node {prev_node} given by does not exist")
                break
        if temp is not None:
            new_node.next = temp.next
            temp.next = new_node

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def deleteNode(self, key):
        temp = self.head
        # case 1
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        # case 2
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        # case 3
        if temp is None:
            return

        prev.next = temp.next
        temp = None

    # TODO delete after
    def deleteAF(self, key):
        temp = self.head
        prev = temp
        if temp.data == key:
            temp = prev.next
            prev.next = temp.next
            del temp
        else:
            while prev.data != key:
                prev = temp
                temp = temp.next
            if temp is not None:
                prev.next = temp.next
                del temp

    def delete_ll(self):
        curr = self.head
        while curr:
            temp = curr.next
            del curr
            self.head = temp
            curr = self.head

    def total_nodes(self, node):
        if not node:
            return 0
        else:
            return 1 + self.total_nodes(node.next)

    def getcount(self):
        return self.total_nodes(self.head)

    def counter(self):
        count = 0
        temp = self.head
        while temp:
            count = count + 1
            temp = temp.next
        return count

    def reverse_ll(self):
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def search(self, key):
        i = 0
        temp = self.head
        while temp.data != key:
            i += 1
            temp = temp.next
        print(f"{key} is at position {i+1}")

    # TODO Linked List to Circular Linked List
    # def ll_to_cll(self, head):
    def ll_to_cll(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = self.head
        return self.head
        # start = head
        # while head.next:
        #     head = head.next
        # head.next = start
        # return start

    def displaycl(self):
        temp = self.head
        # TODO do while implementation in python
        while True:
            print(temp.data)
            temp = temp.next
            if temp == self.head:
                break

    def display(self):
        print("\n*LINKED LIST*")
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    list = LinkedList()
    # ch = 0
    # while ch != 9:
    #     print("\n*** Linked List Operations ***")
    #     print("1.InsertAt Head\n2.InsertAt End\n3.Insert After\n4.Delete Given\n"
    #           "5.Delete All\n6.Count The Total Nodes\n7.Reverse The Linked List\n8.Display\n9.Exit")
    #     ch = int(input("\nEnter your choice : "))
    #     if ch == 1:
    #         new_value = input("Enter a value : ")
    #         list.push(new_value)
    #     elif ch == 2:
    #         new_value = input("Enter a value : ")
    #         list.append(new_value)
    #     elif ch == 3:
    #         prev_value = input("Enter a value after which you want to add node")
    #         new_value = input("Enter a value : ")
    #         list.insertAF(prev_value,new_value)
    #     elif ch == 4:
    #         key = input("Enter a key : ")
    #         list.deleteNode(key)
    #     elif ch == 5:
    #         list.delete_ll()
    #     elif ch == 6:
    #         count = list.counter()
    #         print("Total no of nodes in linked list ={}".format(count))
    #         # list.getcount()
    #     elif ch == 7:
    #         list.reverse_ll()
    #     elif ch == 8:
    #         list.display()
    #     elif ch == 9:
    #         break
    #     else:
    #         print("Enter valid choice BET 1 and 9\n")
    list.push(2)
    list.insertAF(2,3)
    list.display()
    list.insertBF(3,4)
    list.display()
    # list.deleteNode(2)
    # list.deleteNode(3)
    # list.deleteNode(4)
    list.deleteAF(3)
    list.display()
    list.search(2)
    print(list.getcount())
    # list.ll_to_cll(Node(2))
    # list.ll_to_cll()
    print("---------")
    # list.displaycl()
    # list.delete_ll()
    list.reverse_ll()
    list.display()