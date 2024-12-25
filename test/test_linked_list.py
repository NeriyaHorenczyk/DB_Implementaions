import pytest
from src.linked_list import LinkedList


def test_linked_list_initialization():
    ll = LinkedList()
    assert ll.head is None


def test_linked_list_append():
    ll = LinkedList()
    ll.append(1)
    assert ll.head.data == 1
    assert ll.head.next is None


def test_linked_list_append_multiple():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    assert ll.head.data == 1
    assert ll.head.next.data == 2


def test_linked_list_remove():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.remove(1)
    assert ll.head.data == 2
    assert ll.head.next is None


def test_linked_list_remove_nonexistent():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.remove(3)
    assert ll.head.data == 1
    assert ll.head.next.data == 2


def test_linked_list_find():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    node = ll.find(2)
    assert node is not None


def test_linked_list_find_nonexistent():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    node = ll.find(3)
    assert node is False
