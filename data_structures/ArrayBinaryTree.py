from dataclasses import dataclass, field


@dataclass
class ArrayBinaryTree:
    """
    Implementation of a binary tree using a list and computed links.
    The list stores the elements of the tree.

    """

    tree: list = field(default_factory=list)
    count: int = field(init=False)

    def __post_init__(self):
        self.count = len(self.tree)

    def root(self):
        return self.tree[0]

    def is_root(self, element):
        return element == self.tree[0]

    def elements(self):
        return self.tree

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def index_of(self, element):

        try:
            return self.tree.index(element)
        except ValueError:
            raise ValueError(f"{element} does not exist in the tree.")

    def left_child(self, element):

        i = 2 * self.index_of(element) + 1

        if i > self.count - 1:
            return None

        return self.tree[i]

    def right_child(self, element):

        i = 2 * self.index_of(element) + 2

        if i > self.count - 1:
            return None

        return self.tree[i]

    def sibling(self, element):

        if self.is_root(element) is True:
            return None

        # check if left or right child
        i = self.index_of(element)

        if i % 2 == 0:
            # element is a right child
            return self.tree[i - 1]
        else:
            # element is a left child
            return self.tree[i + 1]

    def parent(self, element):

        if self.is_root(element) is True:
            return None

        # floor division
        return self.tree[(self.index_of(element) - 1) // 2]

    def children(self, element):

        left = self.left_child(element)
        right = self.right_child(element)

        result = []

        if left is not None:
            result.append(left)

        if right is not None:
            result.append(right)

        return result

    def is_external(self, element):
        return len(self.children(element)) == 0

    def is_internal(self, element):
        return len(self.children(element)) > 0

    def depth(self, element):

        if self.is_root(element) is True:
            return 0

        return 1 + self.depth(self.parent(element))

    def height(self, element):

        if self.is_external(element) is True:
            return 0

        h = 0

        for child in self.children(element):
            h = max(h, self.height(child))

        return 1 + h

    def iter_level_order(self):
        return iter(self.tree)

    def iter_pre_order(self):

        order_list = []
        self.pre_order(0, order_list)
        return iter(order_list)

    def pre_order(self, node_index, order_list):

        if node_index < len(self.tree):
            if self.tree[node_index] is not None:
                order_list.append(self.tree[node_index])
                self.pre_order(2 * node_index + 1, order_list)
                self.pre_order(2 * node_index + 2, order_list)

    def iter_in_order(self):

        order_list = []
        self.in_order(0, order_list)
        return iter(order_list)

    def in_order(self, node_index, order_list):

        if node_index < len(self.tree):
            if self.tree[node_index] is not None:
                self.in_order(2 * node_index + 1, order_list)
                order_list.append(self.tree[node_index])
                self.in_order(2 * node_index + 2, order_list)

    def iter_post_order(self):

        order_list = []
        self.post_order(0, order_list)
        return iter(order_list)

    def post_order(self, node_index, order_list):

        if node_index < len(self.tree):
            if self.tree[node_index] is not None:
                self.post_order(2 * node_index + 1, order_list)
                self.post_order(2 * node_index + 2, order_list)
                order_list.append(self.tree[node_index])

    def swap_elements(self, element1, element2):
        index_1 = self.index_of(element1)
        index_2 = self.index_of(element2)
        self.tree[index_1] = element2
        self.tree[index_2] = element1

    def replace_element(self, element, new_element):
        self.tree[self.index_of(element)] = new_element