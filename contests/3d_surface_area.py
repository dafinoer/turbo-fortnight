'''
hacker rank
https://www.hackerrank.com/contests/w35/challenges/3d-surface-area/problem
'''

#!/bin/python

def surfaceArea(A):
    cubes = 0
    hidden = 0
    for i in xrange(len(A)):
        for j in xrange(len(A[0])):
            num = A[i][j]
            cubes += num
            hidden += num - 1
            if j > 0:
                hidden += min(num, A[i][j-1])
            if i > 0:
                hidden += min(num, A[i-1][j])
    return cubes * 6 - hidden * 2

if __name__ == "__main__":
    H, W = raw_input().strip().split(' ')
    H, W = [int(H), int(W)]
    A = []
    for A_i in xrange(H):
        A_temp = map(int,raw_input().strip().split(' '))
        A.append(A_temp)
    result = surfaceArea(A)
    print result