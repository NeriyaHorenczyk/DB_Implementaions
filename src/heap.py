"""
Heap implementation
"""

class Heap:
    """
    Heap class
    """
    def __init__(self):
        """
        Constructor
        """
        self.heap = []

    def insert(self, data):
        """
        Insert data into the heap
        :param data:
        :return:
        """
        self.heap.append(data)
        self.__heapify_up(len(self.heap) - 1)

    def extract_min(self):
        """
        Extract the minimum element from the heap
        :return:
        """
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.__heapify_down(0)
        return min_val

    def __heapify_up(self, index):
        """
        Heapify up
        :param index:
        :return:
        """
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.__heapify_up(parent)

    def __heapify_down(self, index):
        """
        Heapify down
        :param index:
        :return:
        """
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.__heapify_down(smallest)

    def top(self):
        """
        Get the minimum element from the heap
        :return:
        """
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def is_empty(self):
        """
        Check if the heap is empty
        :return:
        """
        return len(self.heap) == 0
