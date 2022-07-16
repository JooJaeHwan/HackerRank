'''
★★★★★
Non-Divisible Subset
https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true
'''


import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    remainder_cnt = {}
    answer = 0

    for num in s:
        remainder = num % k
        if remainder in remainder_cnt:
            remainder_cnt[remainder] = remainder_cnt[remainder] + 1
        else:
            remainder_cnt[remainder] = 1

    for remainder in range((k+1)//2, k):
        opposite_remainder = k - remainder
        if remainder == opposite_remainder and remainder in remainder_cnt:
            answer += 1
            continue


        if remainder in remainder_cnt and opposite_remainder in remainder_cnt:
            answer += max(remainder_cnt[remainder], remainder_cnt[opposite_remainder])
        elif remainder in remainder_cnt:
            answer += remainder_cnt[remainder]
        elif opposite_remainder in remainder_cnt:
            answer += remainder_cnt[opposite_remainder]

    if 0 in remainder_cnt:
        answer += 1

    return answer        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()

'''
4 3      
1 7 2 4
3
'''