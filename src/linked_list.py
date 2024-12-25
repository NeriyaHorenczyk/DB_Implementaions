"""
This module contains the implementation of a singly linked list.
"""

class Node:
    """
    Node class for LinkedList
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


class LinkedList:
    """
    LinkedList class
    """
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        """
        Append data to the list
        :param data:
        :return:
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.size += 1

    def print_list(self):
        """
        Print the list
        :return:
        """
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def remove(self, key):
        """
        Remove a node from the list
        :param key:
        :return:
        """
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            self.size -= 1
            return True
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return False
        prev.next = cur_node.next
        cur_node = None
        self.size -= 1
        return True

    def get_size(self):
        """
        Get the size of the list
        :return:
        """
        return self.size

    def find(self, key):
        """
        Find a node in the list
        :param key:
        :return:
        """
        cur_node = self.head
        while cur_node:
            if cur_node.data == key:
                return True
            cur_node = cur_node.next
        return False
