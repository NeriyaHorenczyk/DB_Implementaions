"""
This file contains the tests for the stack data structure.
"""
from src.stack import Stack


def test_stack_initialization():
    """
    This test checks if the stack is initialized correctly.
    :return:
    """
    stack = Stack()
    assert stack.stack == []

def test_stack_push():
    """
    This test checks if the push method works correctly.
    :return:
    """
    stack = Stack()
    stack.push(1)
    assert stack.stack == [1]


def test_stack_push_multiple():
    """
    This test checks if the push method works correctly with multiple elements.
    :return:
    """
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.top() == 2

def test_stack_pop():
    """
    This test checks if the pop method works correctly.
    :return:
    """
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.top() == 1

def test_stack_pop_empty():
    """
    This test checks if the pop method works correctly when the stack is empty.
    :return:
    """
    stack = Stack()
    assert stack.pop() is None

def test_stack_peek():
    """
    This test checks if the top method works correctly.
    :return:
    """
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.top() == 2
    assert stack.stack == [1, 2]


def test_stack_peek_empty():
    """
    This test checks if the top method works correctly when the stack is empty.
    :return:
    """
    stack = Stack()
    assert stack.top() is None

def test_stack_is_empty():
    """
    This test checks if the is_empty method works correctly.
    :return:
    """
    stack = Stack()
    assert stack.is_empty() is True
    stack.push(1)
    assert stack.is_empty() is False
    stack.pop()
    assert stack.is_empty() is True
