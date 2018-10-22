#!/bin/python3

import sys

def surfaceArea(A):
    # Complete this function
    dict_height = {}
    H = len(A)
    W = len(A[0])
    total_cost = 0
    for i in range(H):
        for j in range(W):
            dict_height[(i, j)] = A[i][j]
    for i in range(H):
        for j in range(W):
            for k in range(dict_height[(i,j)]):
                cost = 4
                if i - 1 in range(H) and j in range(W):
                    if k < dict_height[(i-1,j)]:
                        cost -= 1
                if i in range(H) and j + 1 in range(W):
                    if k < dict_height[(i,j+1)]:
                        cost -= 1
                if i + 1 in range(H) and j in range(W):
                    if k < dict_height[(i+1,j)]:
                        cost -= 1
                if i in range(H) and j - 1 in range(W):
                    if k < dict_height[(i,j-1)]:
                        cost -= 1
                total_cost += cost
    total_cost += (2 * H * W)
    return total_cost
                        
                
    
if __name__ == "__main__":
    H, W = input().strip().split(' ')
    H, W = [int(H), int(W)]
    A = []
    for A_i in range(H):
       A_t = [int(A_temp) for A_temp in input().strip().split(' ')]
       A.append(A_t)
    result = surfaceArea(A)
    print(result)