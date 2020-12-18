import unittest


class Solution:
    def kmp(self, T, P):

        f = self.kmp_failfunc(P)
        print(f)
        m = len(P)
        n = len(T)

        i = 0
        j = 0

        while i < n:

            if T[i] == P[j]:

                if j == m - 1:
                    # we have matched all characters in P
                    return i - m + 1

                # we have matched j+1 characters, move to next
                i = i + 1
                j = j + 1

            elif j > 0:
                # build from previous match
                j = f[j - 1]

            else:
                # no match
                i = i + 1

        # P is not a substring of T
        return -1

    @staticmethod
    def kmp_failfunc(P):

        m = len(P)
        f = [0 for j in range(m)]
        j = 0
        i = 1

        while i < m:

            if P[i] == P[j]:
                # we have matched j+1 characters
                f[i] = j + 1
                i = i + 1
                j = j + 1

            elif j > 0:
                # j indexes after a prefix that just matched
                j = f[j - 1]
            else:
                # no match
                f[i] = 0
                i = i + 1

        return f


class TestSolution(unittest.TestCase):
    def test_1(self):
        T = "abacaabaccabacabaabb"
        P = "abacab"
        self.assertEqual(Solution().kmp(T, P), 10)

    def test_2(self):
        T = "cbabacabb"
        P = "abaca"
        self.assertEqual(Solution().kmp(T, P), 2)

    def test_3(self):
        T = "cbabacabb"
        P = "cabbb"
        self.assertEqual(Solution().kmp(T, P), -1)
    
    def test_4(self):
        T = "aaabaadaabaaa"
        P = "aabaaa"
        self.assertEqual(Solution().kmp(T, P), 7)


if __name__ == "__main__":
    unittest.main()