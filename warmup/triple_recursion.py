'''
hacker rank
https://www.hackerrank.com/contests/w35/challenges/triple-recursion/problem
'''

#!/bin/python

def tripleRecursion(n, m, k):
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in xrange(n):
        for j in xrange(n):
            if i == j:
                if i == 0:
                    matrix[0][0] = m
                else:
                    matrix[i][j] = matrix[i - 1][j - 1] + k
            elif i > j:
                matrix[i][j] = matrix[i - 1][j] - 1
            else:
                matrix[i][j] = matrix[i][j - 1] - 1
    for i in xrange(n):
        print(' '.join(str(x) for x in matrix[i]))


if __name__ == "__main__":
    n, m, k = raw_input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    tripleRecursion(n, m, k)
