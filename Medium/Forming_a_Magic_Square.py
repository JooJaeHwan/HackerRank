'''
Forming a Magic Square
https://www.hackerrank.com/challenges/magic-square-forming/problem?isFullScreen=true
'''

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    possibilities = []
    for a in range(1, 10):
        for b in range(1, 10):
            if set([a, 15-a-b, b, 5+b-a, 5, 5+a-b, 10-b, a+b-5, 10-a]) == set(range(1, 10)):
                possibilities.append([a, 15-a-b, b,
                                      5+b-a, 5, 5+a-b,
                                      10-b, a+b-5, 10-a])


    temp = []
    for i in range(len(s)):
        temp += s[i]

    com_min = sum(range(10))

    for p in possibilities:
        com = 0
        for i in range(len(temp)):
            com += abs(temp[i]-p[i])

        if com < com_min:
            com_min = com
    
    return com_min


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()


'''
4 9 2
3 5 7
8 1 5
1
'''