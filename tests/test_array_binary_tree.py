from data_structures.ArrayBinaryTree import *

tree1 = ArrayBinaryTree([0, 1, 2, 3, 4, 5, 6, 7, 8])

print(tree1.depth(5))
print(tree1.height(2))
print(tree1.root())
print(tree1.size())
print(tree1.left_child(0))
print(tree1.left_child(1))
print(tree1.right_child(1))
print(tree1.sibling(1))
print(tree1.parent(1))
print(tree1.children(1))
print(tree1.is_external(1))
print(tree1.is_internal(1))


def printIter(iterator):

    output = ""

    for count, value in enumerate(iterator):
        if count == tree1.size() - 1:
            output += f"{value}"
        else:
            output += f"{value}, "

    print(output)


printIter(tree1.iter_pre_order())
printIter(tree1.iter_in_order())
printIter(tree1.iter_post_order())
printIter(tree1.iter_level_order())