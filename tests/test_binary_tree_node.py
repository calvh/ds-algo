from data_structures.BinaryTreeNode import *


bt1 = BinaryTreeNode(1)
bt2 = BinaryTreeNode(2)
bt3 = BinaryTreeNode(3, bt1, bt2)
bt4 = BinaryTreeNode(1)

print(bt3)
print(bt1 == bt4)