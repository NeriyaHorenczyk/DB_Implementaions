import pytest
from src.binarySearchTree import BinarySearchTree

def test_binary_search_tree_initialization():
    bst = BinarySearchTree()
    assert bst.root is None

def test_binary_search_tree_insert():
    bst = BinarySearchTree()
    bst.insert(1)
    assert bst.root.data == 1

def test_binary_search_tree_insert_multiple():
    bst = BinarySearchTree()
    bst.insert(1)
    bst.insert(2)
    assert bst.root.data == 1
    assert bst.root.right.data == 2

def test_binary_search_tree_find():
    bst = BinarySearchTree()
    bst.insert(1)
    bst.insert(2)
    node = bst.search(2)
    assert node is not None


def test_binary_search_tree_find_nonexistent():
    bst = BinarySearchTree()
    bst.insert(1)
    bst.insert(2)
    node = bst.search(3)
    assert node is False

def test_binary_search_tree_remove():
    bst = BinarySearchTree()
    bst.insert(1)
    bst.insert(2)
    bst.delete(1)
    assert bst.root.data == 2
    assert bst.root.left is None

def test_binary_search_tree_remove_nonexistent():
    bst = BinarySearchTree()
    bst.insert(1)
    bst.insert(2)
    bst.delete(3)
    assert bst.root.data == 1
    assert bst.root.right.data == 2