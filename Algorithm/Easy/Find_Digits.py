'''
Find Digits
https://www.hackerrank.com/challenges/find-digits/problem?isFullScreen=true
'''


import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    return len([i for i in [*str(n)] if i != '0' and int(n) % int(i) == 0])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()


'''
2
12
1012

2
3
'''