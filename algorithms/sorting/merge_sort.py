import random


def merge_sort(s, lower=0, upper=None):
    """Sorts a list of numbers in-place using merge sort.

    Args:
      s: A list containing numbers.
      lower: lower bound (inclusive) of s to be sorted.
      upper: upper bound (inclusive) of s to be sorted.

    Returns:
      s

    """

    if upper is None:
        upper = len(s) - 1

    # base case (1 element or less)
    if lower >= upper:
        return

    # midpoint
    mid = (lower + upper) // 2

    # recur step
    merge_sort(s, lower, mid)  # s1
    merge_sort(s, mid + 1, upper)  # s2

    # merge step
    temp = []

    i = lower  # counter for s1 goes from lower to mid
    j = mid + 1  # counter for s2 goes from mid+1 to upper

    while i <= mid and j <= upper:
        if s[i] <= s[j]:
            temp.append(s[i])
            i += 1
        else:
            temp.append(s[j])
            j += 1

    while i <= mid:
        temp.append(s[i])
        i += 1

    while j <= upper:
        temp.append(s[j])
        j += 1

    # copy contents of temp list to s
    for k in range(len(temp)):
        s[lower + k] = temp[k]


if __name__ == "__main__":
    n = 100
    s = [random.randint(0, n) for x in range(n)]
    merge_sort(s)
    print(s)