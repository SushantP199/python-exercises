class Node:

    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def insert_node(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_node(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_node(node.right, data)

    def insert_helper(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(self.root, data)

    def inorder_successor(self, node):
        if node.left is None:
            return node
        else:
            return self.inorder_successor(node.left)

    def delete_node(self, node, data):
        if node is None:
            return node
        elif data < node.data:
            node.left = self.delete_node(node.left, data)
        elif data > node.data:
            node.right = self.delete_node(node.right, data)
        else:
            # case 1 : Node with No child or One child
            if node.right is None:
                temp = node.left
                node = None
                return temp
            if node.left is None:
                temp = node.right
                node = None
                return temp

            # case 2 : Node with Two children
            temp = self.inorder_successor(node.right)
            node.data = temp.data
            node.right = self.delete_node(node.right, temp.data)
        return node

    def search_node(self, node, data):
        if node is None:
            print("Node is not present")
            return False
        elif data == node.data:
            print("Node is present")
            return True
        else:
            if data < node.data:
                val = self.search_node(node.left, data)
            if data > node.data:
                val = self.search_node(node.right, data)
            return val

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")


bst = BinarySearchTree()
bst.insert_helper(10)
root = bst.get_root()
bst.inorder(root)
print()
bst.insert_helper(5)
bst.insert_helper(12)
bst.insert_helper(1)
bst.insert_helper(3)
bst.insert_helper(9)
bst.insert_helper(11)
bst.insert_helper(13)
bst.inorder(root)
print()
# bst.preorder(root)
# print()
# bst.postorder(root)
d = bst.delete_node(root, 5)
print(d.data)
bst.inorder(root)
root = bst.get_root()
print(root.data)
print(bst.search_node(root, 5))
