#!/bin/python3
"""
hacker rank
 https://www.hackerrank.com/challenges/happy-ladybugs
"""
import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def count_chars(txt,ch):
    result = 0
    for char in txt:
        if char.__eq__(ch):
            result += 1     # same as result = result + 1
    return result
def already(b,len2):
    len1=len(b)
    shift=1
    for i in range(0,len1-1):
        if not b[i].__eq__(b[i+1]):
            shift=shift+1
    if shift is not len2:
        return False
    return True
def happyLadybugs(b):
    #ar=b.split('')
    ar = []
    for line in b:
        ar.extend(line)
        
    ar=list(set(ar))
    len1=len(ar)
    
    
    for i in range(0,len1):
        if ar[i] is not "_" and count_chars(b,ar[i])==1:
            return "NO"
    if already(b,len1):
        return "YES"   
    if not b.__contains__("_"):
        return "NO"
    return "YES"        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
