import unittest
import numpy as np


class Solution:
    def knapsack_01(self, items, w_max):

        b = [0 for w in range(w_max + 1)]

        # list of knapsacks
        knapsack_list = [set() for w in range(w_max + 1)]

        # loop k from 1 to n
        for item in list(items.items()):

            # item: [item_name, [weight, benefit]]
            item_name = item[0]

            w_k = item[1][0]

            b_k = item[1][1]

            # loop in reverse to access b[k-1] and b[k-1, w - w_k] before overwriting
            # loop w from w_max to w_k (if w < w_k do nothing)
            for w in range(w_max, w_k - 1, -1):

                x = b[w - w_k] + b_k

                if x > b[w]:
                    # item is worth putting in
                    b[w] = x

                    # add item to knapsack entry
                    knapsack_list[w] = knapsack_list[w - w_k] ^ set({item_name})

        print(b)
        print(knapsack_list)

        return knapsack_list[w_max]


class TestSolution(unittest.TestCase):
    def test_1(self):

        # "item": [weight, benefit]
        s = {"a": [2, 3], "b": [4, 5], "c": [5, 8], "d": [3, 4], "e": [9, 10]}

        w_max = 20
        knapsack = {"a", "b", "c", "e"}
        knapsack_w_max = Solution().knapsack_01(s, w_max)
        self.assertSetEqual(knapsack_w_max, knapsack)

    def test_2(self):

        s = {
            "a": [12, 4],
            "b": [10, 6],
            "c": [8, 5],
            "d": [11, 7],
            "e": [14, 3],
            "f": [7, 1],
            "g": [9, 6],
        }
        w_max = 18
        knapsack = {"b", "c"}
        knapsack_w_max = Solution().knapsack_01(s, w_max)
        self.assertSetEqual(knapsack_w_max, knapsack)


if __name__ == "__main__":
    unittest.main()