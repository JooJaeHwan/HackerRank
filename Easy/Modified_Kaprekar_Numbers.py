'''
Modified Kaprekar Numbers
https://www.hackerrank.com/challenges/kaprekar-numbers/problem?isFullScreen=true
'''


import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#
def is_kaprekar(num):
    if num < 4:
        if num == 1:
            return True
        else:
            return False
    num_sq = pow(num, 2)
    num_sq_str = str(num_sq)
    
    left = num_sq_str[:len(num_sq_str)//2]
    right = num_sq_str[len(num_sq_str)//2:]
    
    
    if int(left) + int(right) == num:
        return True
    else:
        return False
    
def kaprekarNumbers(p, q):
    answer = [i for i in range(p, q+1) if is_kaprekar(i)]
    if len(answer) != 0:
        print(*answer)
    else:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)



'''
1
100

1 9 45 55 99
'''