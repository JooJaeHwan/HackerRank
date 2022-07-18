'''
Save the Prisoner!
https://www.hackerrank.com/challenges/save-the-prisoner/problem?isFullScreen=true
'''


import math
import os
import random
import re
import sys

#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#


def saveThePrisoner(n, m, s):
    ans = (s+m-1)%n

    if ans==0:
        return n

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()



'''
2
5 2 1
5 2 2

2
3
'''