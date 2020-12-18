import unittest
import numpy as np
import math


class Solution:
    def matrix_chain_product(self, dims):

        # number of matrices
        num_matrices = len(dims) - 1

        # initialize matrix n with dimensions of (num_matrices-1)^2
        n = [[None for j in range(num_matrices)] for i in range(num_matrices)]

        # assign all n_i,i values (diagonal)
        for i in range(num_matrices):
            n[i][i] = 0

        # b is a convenience variable representing the b-th diagonal being calculated
        # n_i,j needs values for n_i,i to n_i,j-1 and n_i+1,j to n_j,j
        for b in range(1, num_matrices):

            # go down the b-th diagonal
            for i in range(num_matrices - b):

                j = i + b

                # initial values
                n_ij_min = math.inf
                k_ij_min = i

                # find n_ij_min
                for k in range(i, j):

                    n_ij = n[i][k] + n[k + 1][j] + (dims[i] * dims[k + 1] * dims[j + 1])

                    if n_ij < n_ij_min:
                        n_ij_min = n_ij
                        k_ij_min = k

                # store k_ij_min on the opposite side (j, i)
                n[i][j] = n_ij_min
                n[j][i] = k_ij_min

        k_vals = []

        def find_k_min(i, j):

            if j - i > 1:
                # initial k_min
                k = n[j][i]
                k_vals.append(k)

                # find k_min for the two groups (A_0...A_k)(A_{k+1}...A_{n-1})
                find_k_min(i, k)
                find_k_min(k + 1, j)

        find_k_min(0, num_matrices - 1)

        print(np.array(n))
        print("k_vals=", sorted(k_vals))

        return n


class TestSolution(unittest.TestCase):
    def test_1(self):

        # A0 (d0xd1), A1 (d1xd2), A2 (d2xd3)
        # dims = [d0, d1, d2, d3]
        dims = [2, 10, 50, 20]
        num_matrices = len(dims) - 1
        n_min = 3000
        n_ij_min = Solution().matrix_chain_product(dims)[0][num_matrices - 1]
        self.assertEqual(n_ij_min, n_min)

    def test_2(self):

        dims = [10, 5, 2, 20, 12, 4, 60]
        num_matrices = len(dims) - 1
        n_min = 2356
        n_ij_min = Solution().matrix_chain_product(dims)[0][num_matrices - 1]
        self.assertEqual(n_ij_min, n_min)


if __name__ == "__main__":
    unittest.main()
