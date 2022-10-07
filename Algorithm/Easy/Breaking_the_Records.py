'''
Breaking the Records
https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true
'''


import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    minium, maximum = scores[0], scores[0]
    min_cnt, max_cnt = 0, 0
    for score in scores[1:]:
        if score > maximum:
            max_cnt += 1
            maximum = score
        if score < minium:
            min_cnt += 1
            minium = score
    return max_cnt, min_cnt
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


'''
9
10 5 20 20 4 5 2 25 1

2 4
'''