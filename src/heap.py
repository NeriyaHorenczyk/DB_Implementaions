from typing import List

class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, data):
        self.heap.append(data)
        self.__heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.__heapify_down(0)
        return min_val

    def __heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.__heapify_up(parent)

    def __heapify_down(self, index):
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
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0