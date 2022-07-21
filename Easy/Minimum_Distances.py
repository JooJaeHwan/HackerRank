'''
Minimum Distances
https://www.hackerrank.com/challenges/minimum-distances/problem?isFullScreen=true
'''


import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    answer = [abs((idx-(a[idx+1:].index(num)+idx+1))) for idx, num in enumerate(a) if num in a[idx+1:]]
    if answer == []:
        return -1
    return min(answer)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()



'''
6
7 1 3 4 1 7

3
'''