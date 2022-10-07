'''
Counting Valleys
https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true
'''

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    level = 0
    cnt = 0
    for p in path:
        if p == "U":
            level += 1
        else:
            if level == 0:
                cnt += 1
            level -= 1
    return cnt
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()


'''
8
UDDDUDUU

1
'''