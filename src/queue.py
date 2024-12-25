"""
Queue implementation in Python
"""
class Queue:
    """
    Queue class
    """
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        """
        Enqueue data into the queue
        :param data:
        :return:
        """
        self.queue.append(data)

    def dequeue(self):
        """
        Dequeue data from the queue
        :return:
        """
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def front(self):
        """
        Get the front element of the queue
        :return:
        """
        if len(self.queue) == 0:
            return None
        return self.queue[0]

    def is_empty(self):
        """
        Check if the queue is empty
        :return:
        """
        return len(self.queue) == 0
