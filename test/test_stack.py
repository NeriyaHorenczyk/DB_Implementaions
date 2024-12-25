import pytest
from src.stack import Stack


def test_stack_initialization():
    stack = Stack()
    assert stack.stack == []

def test_stack_push():
    stack = Stack()
    stack.push(1)
    assert stack.stack == [1]


def test_stack_push_multiple():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.top() == 2

def test_stack_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.top() == 1

def test_stack_pop_empty():
    stack = Stack()
    assert stack.pop() is None

def test_stack_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.top() == 2
    assert stack.stack == [1, 2]


def test_stack_peek_empty():
    stack = Stack()
    assert stack.top() is None

def test_stack_is_empty():
    stack = Stack()
    assert stack.is_empty() is True
    stack.push(1)
    assert stack.is_empty() is False
    stack.pop()
    assert stack.is_empty() is True




