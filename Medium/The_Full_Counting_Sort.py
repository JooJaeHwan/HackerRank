'''
The Full Counting Sort
https://www.hackerrank.com/challenges/countingsort4/problem?isFullScreen=true
'''


import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#
from collections import defaultdict

def countSort(arr):
    d = defaultdict(list)
    h = len(arr) // 2
    for i, (x,y) in enumerate(arr):
        d[int(x)].append("-" if i<h else y)
    print(' '.join([j for i in range(max(d)+1) for j in d[i]]))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)


'''20
0 ab
6 cd
0 ef
6 gh
4 ij
0 ab
6 cd
0 ef
6 gh
0 ij
4 that
3 be
0 to
1 be
5 question
1 or
2 not
4 is
2 to
4 the

- - - - - to be or not to be - that is the question - - - -
'''