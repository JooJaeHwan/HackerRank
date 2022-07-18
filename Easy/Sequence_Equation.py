'''
Sequence Equation
https://www.hackerrank.com/challenges/permutation-equation/problem?isFullScreen=true
'''


import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#


def permutationEquation(p):
    indices = [p.index(i)+1 for i in range(1, len(p)+1)]
    return [p.index(ele)+1 for ele in indices]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()



'''
3
2 3 1

2
3
1
'''