import unittest
from heapq import *


class Solution:
    def task_scheduling(self, tasks):

        # sort by start time
        tasks.sort(key=lambda t: t[0])

        # initialize machine heap
        machines = []
        heapify(machines)

        for t in tasks:

            t_start = t[0]
            t_finish = t[1]

            # find available machine
            try:
                # find machine with earliest finish time
                m = machines[0]

                if m[0] <= t_start:

                    # machine available
                    m[1].append(t)
                    m[0] = t_finish

                    # remove m and insert it again
                    heapreplace(machines, m)
                else:
                    # no available machines, create new machine
                    heappush(machines, [t_finish, [t]])

                # heapreplace(machines, )
            except IndexError:
                # no machines, create new machine
                heappush(machines, [t_finish, [t]])

        print(f"machines: {machines}")
        return [machines, len(machines)]


class TestSolution(unittest.TestCase):
    def test_0(self):

        tasks = [[1, 4], [5, 9], [3, 5], [4, 6]]
        n = 2
        self.assertEqual(Solution().task_scheduling(tasks)[1], n)

    def test_1(self):

        tasks = [[1, 3], [1, 4], [2, 5], [3, 7], [4, 7], [6, 9], [7, 8]]
        n = 3
        self.assertEqual(Solution().task_scheduling(tasks)[1], n)


if __name__ == "__main__":
    unittest.main()