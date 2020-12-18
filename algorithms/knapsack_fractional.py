import unittest


class Solution:
    def knapsack_fractional(self, S, W):

        knapsack = {}

        # sort items in descending order by value = weight/benefit
        # O(n log n)
        items = sorted(S.items(), key=lambda i: i[1][1] / i[1][0], reverse=True)

        w = 0  # current weight
        i = 0

        # extract items from sorted list into knapsack
        # O(n)
        while w < W and i < len(items) - 1:

            item = items[i]
            w_i = item[1][0]

            if w + w_i <= W:

                # if the whole item fits, put it in
                w = w + w_i
                knapsack[item[0]] = w_i

            else:

                # knapsack will be full, put in a fraction of the item
                knapsack[item[0]] = W - w
                w = W

            i = i + 1

        return knapsack


class TestSolution(unittest.TestCase):
    def test_0(self):

        # item: [weight, benefit]
        d = {1: [4, 12], 2: [8, 32], 3: [2, 40], 4: [6, 30], 5: [1, 50]}

        # item: weight
        solution = {5: 1, 3: 2, 4: 6, 2: 1}

        self.assertDictEqual(Solution().knapsack_fractional(d, 10), solution)


if __name__ == "__main__":
    unittest.main()