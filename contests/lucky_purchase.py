'''
hacker rank
https://www.hackerrank.com/contests/w35/challenges/lucky-purchase/problem
'''

#!/bin/python

import sys

if __name__ == "__main__":
    n = int(raw_input().strip())
    price = 1000000000
    name = ""
    for a0 in xrange(n):
        name, value = raw_input().strip().split(' ')
        name, value = [str(name), int(value)]
        counts = dict()
        for i in str(value):
            counts[i] = counts.get(i, 0) + 1

        if len(counts) == 2 and counts.get("7", 0) == counts.get("4", 0) and counts.get("4", 0) > 0:
            if int(value) < price:
                name = name
                price = value
    if name == "":
        print(-1)
    else:
        print(name)