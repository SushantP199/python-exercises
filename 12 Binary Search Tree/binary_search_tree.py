class Node:

    def __init__(self, data):
        self.left = None
        self.key = data
        self.right = None


class BinarySearchTree:

    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        return self.root

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_helper(self.root, data)

    def insert_helper(self, node, data):
        if node.key > data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_helper(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_helper(node.right, data)

    def inorder_successor(self, node):
        val = node.right
        while val.left is not None:
            val = val.left
        return val

    def inorder_predcessor(self, node):
        val = node.left
        while val.right is not None:
            val = val.right
        return val

    def delete_node(self, node, data):
        if node is None:
            return node
        if key < node.key:
            node.left = self.delete_node(node.left, data)
        elif key > node.key:
            node.right = self.delete_node(node.right, data)
        else:
            # case 1 : node with No or One child
            if node.left is None:
                temp = node.right
                node = None
                return temp
            if node.right is None:
                temp = node.left
                node = None
                return temp

            # case 2 : node with Two child
            temp = self.inorder_successor(node)
            node.key = temp.key
            node.right = self.delete_node(node.right, temp.key)
        return node

    def search(self, node, key):
        if node is None:
            print("Key is not Found")
            return False
        elif node.key == key:
            print('Key was found')
            return True
        else:
            if key < node.key:
                self.search(node.left, key)
            else:
                
                self.search(node.right, key)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.key, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=" ")

bst = BinarySearchTree()
bst.insert(10)
root = bst.get_root()
bst.insert(5)
bst.insert(12)
bst.insert(1)
bst.insert(3)
bst.insert(9)
bst.insert(11)
bst.insert(13)
bst.inorder(root)
print()
bst.preorder(root)
print()
bst.postorder(root)