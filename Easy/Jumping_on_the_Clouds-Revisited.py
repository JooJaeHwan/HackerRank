'''
Jumping on the Clouds: Revisited
https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem?isFullScreen=true
'''


import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    cur = k % len(c)
    energy = 100 - 1 - c[cur]*2
    
    while cur != 0:
        cur = (cur + k) % len(c)
        energy -= 1 + c[cur]*2
        
    return energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()



'''
8 2
0 0 1 0 0 1 1 0

92
'''