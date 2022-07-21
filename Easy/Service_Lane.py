'''
Service Lane
https://www.hackerrank.com/challenges/service-lane/problem?isFullScreen=true
'''


import math
import os
import random
import re
import sys

#
# Complete the 'serviceLane' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY cases
#

def serviceLane(n, cases):
    for i, j in cases:
        res = 3
        for inter in range(i, j + 1):
            res = min(res, width[inter])
        yield res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


'''
8 5
2 3 1 2 3 2 3 3
0 3
4 6
6 7
3 5
0 7

1
2
3
2
1
'''