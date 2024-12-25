"""
Stack implementation
"""
class Stack:
    """
    Stack class
    """
    def __init__(self):
        self.stack = []

    def push(self, data):
        """
        Push data into the stack
        :param data:
        :return:
        """
        self.stack.append(data)

    def pop(self):
        """
        Pop data from the stack
        :return:
        """
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def top(self):
        """
        Get the top element of the stack
        :return:
        """
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def is_empty(self):
        """
        Check if the stack is empty
        :return:
        """
        return len(self.stack) == 0
