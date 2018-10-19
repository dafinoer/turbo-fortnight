#!/bin/python3

"""
hacker rank

https://www.hackerrank.com/challenges/compare-the-triplets/problem
"""

import math
import os
import random
import re
import sys
import functools

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    reducer = lambda tup, zab: (tup[0] + 1, tup[1]) if zab[0] > zab[1] else (tup[0], tup[1] + 1) if zab[0] < zab[1] else tup

    return functools.reduce(reducer, zip(a, b), (0, 0))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
