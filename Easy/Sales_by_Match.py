'''
Sales by Match
https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true
'''


import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#
from collections import Counter

def sockMerchant(n, ar):
    cnt = 0
    for a in list(Counter(ar).values()):
        cnt += a//2
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()



'''
9 
10 20 20 10 10 30 50 10 20

3
'''