import math
import os
import random
import re
import sys
def compareTriplets(a, b):
    alice = 0
    bob = 0
    store_1 = []
    if a[0] > b[0]:
        alice += 1
    if a[0] < b[0]:
        bob += 1
    if a[1] > b[1]:
        alice += 1
    if a[1] < b[1]:
        bob += 1
    if a[2] > b[2]:
        alice += 1
    if a[2] < b[2]:
        bob += 1
    print(alice, bob)
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
result = compareTriplets(a, b)
