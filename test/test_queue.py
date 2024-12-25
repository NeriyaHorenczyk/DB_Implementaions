import pytest
from src.queue import Queue

def test_queue_initialization():
    queue = Queue()
    assert queue.queue == []

def test_queue_enqueue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.front() == 1

def test_queue_enqueue_multiple():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.front() == 1


def test_queue_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert queue.front() == 2

def test_queue_dequeue_empty():
    queue = Queue()
    assert queue.dequeue() is None

def test_queue_front():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.front() == 1

def test_queue_front_empty():
    queue = Queue()
    assert queue.front() is None

def test_queue_is_empty():
    queue = Queue()
    assert queue.is_empty() is True
    queue.enqueue(1)
    assert queue.is_empty() is False
    queue.dequeue()
    assert queue.is_empty() is True

