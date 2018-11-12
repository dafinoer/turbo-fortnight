#!/bin/python3

# https://www.hackerrank.com/challenges/apple-and-orange/problem

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Count apple
    apple_count = 0
    for apple in apples :
        location = a + apple
        if location >= s and location <= t :
            apple_count += 1
    print(apple_count)
    # Count orange
    orange_count = 0
    for orange in oranges :
        location = b + orange
        if location >= s and location <= t :
            orange_count += 1
    print(orange_count)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    789`t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)