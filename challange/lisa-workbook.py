#!/bin/python3
 """
hacker rank
 https://www.hackerrank.com/challenges/lisa-workbook
"""
import math
import os
import random
import re
import sys
# Complete the workbook function below.
def workbook(n, k, arr):
    pageNo=0
    result=0
    for i in range(0,n):
        temp=arr[i]
        prob_count=0        
        while temp>0:
            pageNo=pageNo+1
            if temp<k:
                prob_count=prob_count+(temp)
                if prob_count-pageNo <temp and prob_count-pageNo>=0:
                    result=result+1
                 #   print(str(prob_count)+"--->"+str(pageNo)+"--->"+str(result)+"----"+str(prob_count-pageNo ))
                temp=0             
            else:    
                prob_count=prob_count+k
                temp=temp-k            
                if prob_count-pageNo <k and prob_count-pageNo>=0:
                    result=result+1
                   # print(str(prob_count)+"--->"+str(pageNo)+"--->"+str(result))
    return result             
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = workbook(n, k, arr)
    fptr.write(str(result) + '\n')
    fptr.close()