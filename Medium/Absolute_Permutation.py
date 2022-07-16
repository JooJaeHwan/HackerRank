'''
Absolute Permutation
https://www.hackerrank.com/challenges/absolute-permutation/problem?isFullScreen=true
'''

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    out = []
    switch = k
    if k == 0:
        return [x for x in range(1, n+1)]
    
    if n % (2*k) != 0:
        return [-1]
        
    for pos in range(1, n + 1):
        out.append(pos + switch)
        
        if pos % k == 0:
            switch *= -1
            
    return out
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()


'''
3
2 1
3 0
3 2
2 1
1 2 3
-1
'''