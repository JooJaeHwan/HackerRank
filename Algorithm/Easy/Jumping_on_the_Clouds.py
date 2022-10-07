'''
Jumping on the Clouds
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?isFullScreen=true
'''


import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    x,y = 0,0
    while x<len(c)-2:
        x = x+1 if c[x+2] else x+2
        y+=1
    if x<len(c)-1:
        y+=1
    return y

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()



'''
7
0 0 1 0 0 1 0

4
'''