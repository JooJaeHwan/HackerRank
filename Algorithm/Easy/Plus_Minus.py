'''
Plus Minus
https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true
'''

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    plus, minus, zero = 0, 0, 0
    for a in arr:
        if a > 0:
            plus += 1
        elif a < 0 :
            minus += 1
        else:
            zero += 1
    print(f"{plus/len(arr):.6f}")
    print(f"{minus/len(arr):.6f}")
    print(f"{zero/len(arr):.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


'''
6               
-4 3 -9 0 4 1
0.500000
0.333333
0.166667
'''