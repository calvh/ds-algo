from data_structures.LinkedBinaryTree import *
from data_structures.BinaryTreeNode import *

bt0 = BinaryTreeNode(0)
bt1 = BinaryTreeNode(1)
bt2 = BinaryTreeNode(2)
bt3 = BinaryTreeNode(3)
bt4 = BinaryTreeNode(4)
bt5 = BinaryTreeNode(5)
bt6 = BinaryTreeNode(6)


tree3 = LinkedBinaryTree(bt3)
tree4 = LinkedBinaryTree(bt4)
tree5 = LinkedBinaryTree(bt5)
tree6 = LinkedBinaryTree(bt6)

tree1 = LinkedBinaryTree(bt1, tree3, tree4)
tree2 = LinkedBinaryTree(bt2, tree5, tree6)

tree0 = LinkedBinaryTree(bt0, tree1, tree2)


print(tree0.get_root())
print(tree0.size())
print(tree0.positions())
print(tree0.elements())
print(tree0.depth(bt5))
print(tree0.height(bt2))
print(tree0.left_child(bt0))
print(tree0.left_child(bt1))
print(tree0.right_child(bt1))
print(tree0.sibling(bt1))
print(tree0.parent(bt1))
print(tree0.children(bt1))
print(tree0.is_external(bt1))
print(tree0.is_internal(bt1))
print(tree0.is_external(bt6))
print(tree0.is_internal(bt6))


def printIter(iterator):

    output = ""

    for count, value in enumerate(iterator):
        if count == tree0.size() - 1:
            output += f"{value}"
        else:
            output += f"{value}, "

    print(output)


printIter(tree0.iter_level_order())
printIter(tree0.iter_pre_order())
printIter(tree0.iter_in_order())
printIter(tree0.iter_post_order())