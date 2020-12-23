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

    def is_root(self, v):
        return v == self.tree[0]

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def index_of(self, v):

        # todo see if there is a more efficient way to implement this
        try:
            return self.tree.index(v)
        except ValueError:
            raise ValueError(f"Node {v} does not exist.")

    def left_child(self, v):

        i = 2 * self.index_of(v) + 1

        if i > self.count - 1:
            return None

        return self.tree[i]

    def right_child(self, v):

        i = 2 * self.index_of(v) + 2

        if i > self.count - 1:
            return None

        return self.tree[i]

    def sibling(self, v):

        if self.is_root(v) is True:
            return None

        # check if left or right child
        i = self.index_of(v)

        if i % 2 == 0:
            # v is a right child
            return self.tree[i - 1]
        else:
            # v is a left child
            return self.tree[i + 1]

    def parent(self, v):

        if self.is_root(v) is True:
            return None

        # floor division
        return self.tree[(self.index_of(v) - 1) // 2]

    def children(self, v):

        i = self.index_of(v)

        left = self.left_child(v)
        right = self.right_child(v)

        result = []

        if left is not None:
            result.append(left)

        if right is not None:
            result.append(right)

        return result

    def is_external(self, v):
        return len(self.children(v)) == 0

    def is_internal(self, v):
        return len(self.children(v)) > 0

    def elements(self):
        return self.tree

    def depth(self, v):

        if self.is_root(v) is True:
            return 0

        return 1 + self.depth(self.parent(v))

    def height(self, v):

        if self.is_external(v) is True:
            return 0

        h = 0

        for child in self.children(v):
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

    def swap_elements(self, v1, v2):
        index_1 = self.index_of(v1)
        index_2 = self.index_of(v2)
        self.tree[index_1] = v2
        self.tree[index_2] = v1

    def replace_element(self, v, element):
        self.tree[self.index_of(v)] = element