# annotations required for self-referencing class, remove in Python 4.0
from __future__ import annotations
from dataclasses import dataclass, field, InitVar
from collections import deque
from data_structures.BinaryTreeNode import *


@dataclass
class LinkedBinaryTree:
    """
    Implementation of a binary tree using a linked structure.

    """

    root: BinaryTreeNode = None
    left_subtree: InitVar[LinkedBinaryTree] = None
    right_subtree: InitVar[LinkedBinaryTree] = None

    def __post_init__(self, left_subtree, right_subtree):

        if self.root is not None:
            if left_subtree is not None:
                self.root.left = left_subtree.root
                left_subtree.root.parent = self.root

            if right_subtree is not None:
                self.root.right = right_subtree.root
                right_subtree.root.parent = self.root

    def get_root(self):
        return self.root

    def is_root(self, node):
        return node == self.root

    def size(self):
        return self.root.num_descendants() + 1

    def is_empty(self):
        return self.size() == 0

    def left_child(self, node):
        return node.left

    def right_child(self, node):
        return node.right

    def sibling(self, node):

        if self.is_root(node) is True:
            return None

        if node.parent.left == node:
            return node.parent.right
        elif node.parent.right == node:
            return node.parent.left

    def parent(self, node):
        return node.parent

    def children(self, node):

        result = []

        left = node.left
        right = node.right

        if left is not None:
            result.append(left)

        if right is not None:
            result.append(right)

        return result

    def is_external(self, node):
        return node.left is None and node.right is None

    def is_internal(self, node):
        return (node.left is not None) or (node.right is not None)

    def in_order_next(self, node):
        if self.is_internal(node) is True:
            return node.right
        else:
            p = node.parent
            if node is p.left:
                return p
            else:
                while node is not p.left:
                    node = p
                    p = p.parent
                return p

    def elements(self):
        return self.iter_in_order()

    def positions(self):

        position_list = []
        self.positions_in_order(self.root, position_list)
        return iter(position_list)

    def positions_in_order(self, node, position_list):

        if node is not None:
            self.positions_in_order(node.left, position_list)
            position_list.append(node)
            self.positions_in_order(node.right, position_list)

    def swap_elements(self, node1, node2):
        node1.element, node2.element = node2.element, node1.element

    def replace_element(self, node, element):
        node.element = element

    def depth(self, node):

        if self.is_root(node) is True:
            return 0

        return 1 + self.depth(self.parent(node))

    def height(self, node):

        if self.is_external(node) is True:
            return 0

        h = 0

        for child in self.children(node):
            h = max(h, self.height(child))

        return 1 + h

    def iter_level_order(self):

        queue = deque()
        order_list = []

        queue.append(self.root)

        while queue:
            node = queue.popleft()
            order_list.append(node.element)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return iter(order_list)

    def iter_pre_order(self):

        order_list = []
        self.pre_order(self.root, order_list)
        return iter(order_list)

    def pre_order(self, node, order_list):

        if node is not None:
            order_list.append(node.element)
            self.pre_order(node.left, order_list)
            self.pre_order(node.right, order_list)

    def iter_in_order(self):

        order_list = []
        self.in_order(self.root, order_list)
        return iter(order_list)

    def in_order(self, node, order_list):

        if node is not None:
            self.in_order(node.left, order_list)
            order_list.append(node.element)
            self.in_order(node.right, order_list)

    def iter_post_order(self):

        order_list = []
        self.post_order(self.root, order_list)
        return iter(order_list)

    def post_order(self, node, order_list):

        if node is not None:
            self.post_order(node.left, order_list)
            self.post_order(node.right, order_list)
            order_list.append(node.element)
