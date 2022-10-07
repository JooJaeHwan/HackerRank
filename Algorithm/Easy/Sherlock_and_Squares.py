'''
Sherlock and Squares
https://www.hackerrank.com/challenges/sherlock-and-squares/problem?isFullScreen=true
'''


from math import floor, ceil
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    res = 0
    res = floor(b**0.5)+1 - ceil(a**0.5)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()



'''
2
3 9
17 24

2
0
'''