from data_structures.ArrayBinaryTree import *

tree1 = ArrayBinaryTree([0,1,2,3,4,5,6,7,8])

print(tree1.depth(5))
print(tree1.height(2))

def printIter(iterator):
    output = ""

    for e in iterator:
        output += f"{e}, "

    print(output)

printIter(tree1.iter_pre_order())
printIter(tree1.iter_in_order())
printIter(tree1.iter_post_order())
printIter(tree1.iter_level_order())