import random


def bucket_sort(s, key_range):
    """Sorts a list of (key, element) tuples in-place using bucket sort.

    Args:
      s: A list containing tuples of the form (<key>, <element>) and where the range of <key> is 0 to key_range inclusive.
      key_range: An integer defining the upper limit of key values.

    Returns:
      s

    """

    # initialize buckets
    buckets = [[] for i in range(key_range + 1)]

    # put elements into buckets based on keys
    for item in s:
        buckets[item[0]].append(item)

    # take items out of buckets in order
    i = 0
    for bucket in buckets:
        for item in bucket:
            s[i] = item
            i = i + 1


if __name__ == "__main__":
    key_range = 1000
    n = 50
    s = [(random.randint(0, key_range), "e") for x in range(n)]
    bucket_sort(s, key_range)
    print(*s, sep="\n")
