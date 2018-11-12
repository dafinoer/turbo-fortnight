#!/bin/python3

"""
hacker rank

https://www.hackerrank.com/challenges/mini-max-sum/problem
"""

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    allSum = sum(arr)
    fourSum = [allSum - x for x in arr]
    print(min(fourSum), max(fourSum))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
