import random


def quick_sort(s, lower=0, upper=None):
    """Sorts a list of numbers in-place using quick-sort.

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

    # choose random index as pivot
    pivot = random.randint(lower, upper)

    # perform partitioning
    left = lower
    right = upper
    done = False

    while done is False:

        while s[left] < s[pivot]:
            left += 1

        while s[right] > s[pivot]:
            right += 1

        if left >= right:
            done = True
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right += 1

    # partition element
    part = right

    # recurse
    quick_sort(s, lower, part)
    quick_sort(s, part + 1, upper)


if __name__ == "__main__":
    n = 100
    s = [random.randint(0, n) for x in range(n)]
    quick_sort(s)
    print(s)
