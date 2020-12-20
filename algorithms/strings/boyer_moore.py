def boyer_moore(text, pattern):

    last = last_constructor(set(text).union(set(pattern)), pattern)
    m = len(pattern)
    n = len(text)

    i = m - 1
    j = m - 1

    while i <= n - 1:

        if pattern[j] == text[i]:
            # match

            if j == 0:
                # full match
                return i
            else:
                # partial match, continue
                i -= 1
                j -= 1

        else:
            # no match

            # jump step
            i += m - min(j, 1 + last[text[i]])

            j = m - 1

    return -1


def last_constructor(alphabet, pattern):

    d = {}

    for i in range(len(pattern)):
        d[pattern[i]] = i

    for c in alphabet:
        if c not in d:
            d[c] = -1

    return d