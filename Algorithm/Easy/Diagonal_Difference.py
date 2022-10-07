'''
Diagonal Difference
https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true
'''

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    result = 0
    for i in range(len(arr)):
        result += arr[i][i] - arr[i][len(arr)-1-i]
    return abs(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


'''
3
11 2 4
4 5 6
10 8 -12
15
'''