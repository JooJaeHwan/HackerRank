'''
Larry's Array
https://www.hackerrank.com/challenges/larrys-array/problem?isFullScreen=true
'''

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

def larrysArray(A):
    s = sorted(A)
    for i in s[:-2]:
        if A.index(i) % 2:
            print(A)
            A.remove(i)
            A[0], A[1] = A[1], A[0]
        else:
            print(A)
            A.remove(i)
    if A[0] < A[1]:
        return "YES"
    else:
        return "NO"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()


'''
3
3
3 1 2
4
1 3 4 2
5
1 2 3 5 4

YES
YES
NO
'''