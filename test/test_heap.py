import pytest
from src.heap import Heap

def test_heap_initialization():
    heap = Heap()
    assert heap.heap == []


def test_heap_insert():
    heap = Heap()
    heap.insert(1)
    assert heap.heap == [1]

def test_heap_insert_multiple():
    heap = Heap()
    heap.insert(1)
    heap.insert(2)
    assert heap.top() == 1

def test_heap_extract_min():
    heap = Heap()
    heap.insert(1)
    heap.insert(2)
    assert heap.extract_min() == 1
    assert heap.top() == 2

def test_heap_extract_min_empty():
    heap = Heap()
    assert heap.extract_min() is None

def test_heap_top():
    heap = Heap()
    heap.insert(1)
    heap.insert(2)
    assert heap.top() == 1

def test_heap_top_empty():
    heap = Heap()
    assert heap.top() is None

def test_heap_is_empty():
    heap = Heap()
    assert heap.is_empty() is True
    heap.insert(1)
    assert heap.is_empty() is False
    heap.extract_min()
    assert heap.is_empty() is True

def test_heap_heapify_up():
    heap = Heap()
    heap.heap = [2, 3, 1]
    heap.insert(0)
    assert heap.heap == [0, 2, 1, 3]

def test_heap_heapify_down():
    heap = Heap()
    heap.heap = [1, 3, 2]
    heap.extract_min()
    assert heap.heap == [2, 3]