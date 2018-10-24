#!/bin/python3

"""
hacker rank

https://www.hackerrank.com/challenges/plus-minus/problem
"""

# Complete the plusMinus function below.
def plusMinus(arr):
    nos = len(arr)

    pos = len([x for x in arr if x > 0])
    neg = len([x for x in arr if x < 0])
    oo = len([x for x in arr if x == 0])

    pos, neg, oo = pos/nos, neg/nos, oo/nos

    print('{:f}'.format(pos))
    print('{:f}'.format(neg))
    print('{:f}'.format(oo))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
