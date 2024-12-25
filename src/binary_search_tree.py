"""
Binary Search Tree implementation in Python
"""
class Node:
    """
    Node class for BinarySearchTree
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)

class BinarySearchTree:
    """
    BinarySearchTree class
    """
    def __init__(self):
        self.root = None

    def insert(self, data):
        """
        Insert data into the tree
        :param data:
        :return:
        """
        if self.root is None:
            self.root = Node(data)
        else:
            self.__insert(self.root, data)

    def __insert(self, node, data):
        """
        Helper function for insert
        :param node:
        :param data:
        :return:
        """
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
        """
        Search for a key in the tree
        :param key:
        :return:
        """
        return self.__search(self.root, key)

    def __search(self, node, key):
        """
        Helper function for search
        :param node:
        :param key:
        :return:
        """
        if node is None:
            return False
        if node.data == key:
            return True
        if key < node.data:
            return self.__search(node.left, key)
        return self.__search(node.right, key)

    def delete(self, key):
        """
        Delete a node from the tree
        :param key:
        :return:
        """
        self.root = self.__delete(self.root, key)

    def __delete(self, node, key):
        """
        Delete a node from the tree
        :param node:
        :param key:
        :return:
        """
        if node is None:
            return node
        if key < node.data:
            node.left = self.__delete(node.left, key)
        elif key > node.data:
            node.right = self.__delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            node.data = self.__min_value(node.right)
            node.right = self.__delete(node.right, node.data)
        return node

    @staticmethod
    def __min_value(node):
        """
        Get the minimum value in the tree
        :param node:
        :return:
        """
        current = node
        while current.left:
            current = current.left
        return current.data

    def inorder(self):
        """
        Inorder traversal of the tree
        :return:
        """
        self.__inorder(self.root)

    def __inorder(self, node):
        """
        Helper function for inorder
        :param node:
        :return:
        """
        if node:
            self.__inorder(node.left)
            print(node.data)
            self.__inorder(node.right)

    def preorder(self):
        """
        Preorder traversal of the tree
        :return:
        """
        self.__preorder(self.root)

    def __preorder(self, node):
        """
        Helper function for preorder
        :param node:
        :return:
        """
        if node:
            print(node.data)
            self.__preorder(node.left)
            self.__preorder(node.right)

    def postorder(self):
        """
        Postorder traversal of the tree
        :return:
        """
        self.__postorder(self.root)

    def __postorder(self, node):
        """
        Helper function for postorder
        :param node:
        :return:
        """
        if node:
            self.__postorder(node.left)
