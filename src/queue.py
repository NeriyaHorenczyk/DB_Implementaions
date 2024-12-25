from typing import List

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def front(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0