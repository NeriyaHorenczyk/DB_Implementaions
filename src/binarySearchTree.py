class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.__insert(self.root, data)

    def __insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.__insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.__insert(node.right, data)

    def search(self, key):
        return self.__search(self.root, key)

    def __search(self, node, key):
        if node is None:
            return False
        if node.data == key:
            return True
        if key < node.data:
            return self.__search(node.left, key)
        return self.__search(node.right, key)

    def delete(self, key):
        self.root = self.__delete(self.root, key)

    def __delete(self, node, key):
        if node is None:
            return node
        if key < node.data:
            node.left = self.__delete(node.left, key)
        elif key > node.data:
            node.right = self.__delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.data = self.__min_value(node.right)
            node.right = self.__delete(node.right, node.data)
        return node

    @staticmethod
    def __min_value(node):
        current = node
        while current.left:
            current = current.left
        return current.data

    def inorder(self):
        self.__inorder(self.root)

    def __inorder(self, node):
        if node:
            self.__inorder(node.left)
            print(node.data)
            self.__inorder(node.right)

    def preorder(self):
        self.__preorder(self.root)

    def __preorder(self, node):
        if node:
            print(node.data)
            self.__preorder(node.left)
            self.__preorder(node.right)

    def postorder(self):
        self.__postorder(self.root)

    def __postorder(self, node):
        if node:
            self.__postorder(node.left)
