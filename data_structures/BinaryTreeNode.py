# annotations required for self-referencing class, remove in Python 4.0
from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class BinaryTreeNode:
    """
    Linked node class for binary trees.
    """

    element: any
    left: BinaryTreeNode = field(default=None, compare=False)
    right: BinaryTreeNode = field(default=None, compare=False)
    parent: BinaryTreeNode = field(default=None, compare=False)

    def num_descendants(self):

        result = 0

        if self.left is not None:
            result += 1 + self.left.num_descendants()

        if self.right is not None:
            result += 1 + self.left.num_descendants()

        return result

    def set_left(self, node: BinaryTreeNode):
        self.left = node

    def set_right(self, node: BinaryTreeNode):
        self.right = node

    def set_parent(self, node: BinaryTreeNode):
        self.parent = node
