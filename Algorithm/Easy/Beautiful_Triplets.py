'''
Beautiful Triplets
https://www.hackerrank.com/challenges/beautiful-triplets/problem?isFullScreen=true
'''


import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    return len([(a, a+d, a+d+d) for a in arr if a+d in arr and a+d+d in arr])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()



'''
7 3
1 2 4 5 7 8 10

3
'''