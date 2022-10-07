'''
★★★★★
3D Surface Area
https://www.hackerrank.com/challenges/3d-surface-area/problem?isFullScreen=true
'''

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    H = len(A)
    W = len(A[0])
    ans = 2*H*W
    for i in range(H):
        for j in range(W):
            # top
            if i == 0:
                ans += A[i][j]
            
            # left
            if j == 0:
                ans += A[i][j]
            
            # right
            if j == W-1:
                ans += A[i][j]
            else:
                ans += abs(A[i][j]-A[i][j+1])
            
            # bottom
            if i == H-1:
                ans += A[i][j]
            else:
                ans += abs(A[i][j]-A[i+1][j])
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()

'''
3 3
1 3 4
2 2 3
1 2 4
60
'''