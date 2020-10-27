#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations
# Complete the formingMagicSquare function below.
def check(ar,a):
    arr=[[0 for i in range (3)] for i in range (3)]
    for i in range (3):
        for j in range (3):
            arr[i][j]=ar[i*3+j]
    if (arr[0][0]+arr[1][1]+arr[2][2]==15) and (arr[0][2]+arr[1][1]+arr[2][0]==15) and(arr[0][0]+arr[0][1]+arr[0][2]==15)and(arr[1][0]+arr[1][1]+arr[1][2]==15)and(arr[2][0]+arr[2][1]+arr[2][2]==15)and(arr[0][0]+arr[1][0]+arr[2][0]==15)and(arr[0][1]+arr[1][1]+arr[2][1]==15)and(arr[0][2]+arr[1][2]+arr[2][2]==15):
        a.append(arr)
    return a

def calc_diff(s,sq):
    n=0
    for i  in range (3):
        for j in range (3):
            n+=abs(s[i][j]-sq[i][j])
    return n
def formingMagicSquare(s):
    square=[1,2,3,4,5,6,7,8,9]
    l=list(permutations(square))
    a=[]
    diff=[]
    for i in range ( len(l)):
        a=check(list(l[i]),a)
    for i in range (len(a)):
        diff.append(calc_diff(s,a[i]))
    x=min(diff)
    return x


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
