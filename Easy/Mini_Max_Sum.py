'''
Mini Max Sum
https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true
'''

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    print(sum(arr)-max(arr), sum(arr)-min(arr))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

'''
1 2 3 4 5
10 14
'''