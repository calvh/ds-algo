def kmp(text, pattern):

    f = kmp_failure_function(pattern)
    m = len(pattern)
    n = len(text)

    i = 0
    j = 0

    while i < n:

        if text[i] == pattern[j]:

            if j == m - 1:
                # we have matched all characters in pattern
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

    # pattern is not a substring of text
    return -1


def kmp_failure_function(pattern):

    m = len(pattern)
    f = [0 for j in range(m)]
    j = 0
    i = 1

    while i < m:

        if pattern[i] == pattern[j]:
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