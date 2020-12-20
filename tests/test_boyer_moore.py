from algorithms.strings.boyer_moore import *


def test1():
    T = "abacaabaccabacabaabb"
    P = "abacab"
    answer = 10
    return boyer_moore(T, P)


def test2():
    T = "cbabacabb"
    P = "abaca"
    answer = 2
    return boyer_moore(T, P)


def test3():
    T = "cbabacabb"
    P = "cabbb"
    answer = -1
    return boyer_moore(T, P)


def test4():
    T = "aaabaadaabaaa"
    P = "aabaaa"
    answer = 7
    return boyer_moore(T, P)


print(test1())
print(test2())
print(test3())
print(test4())