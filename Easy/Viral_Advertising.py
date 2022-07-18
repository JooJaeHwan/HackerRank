'''
Viral Advertising
https://www.hackerrank.com/challenges/strange-advertising/problem?isFullScreen=true
'''


import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#




def viralAdvertising(n):
    def calc_pattern():
        max_n = 50
        ads = 5
        output = []
        for i in range(max_n):
            output.append(ads//2)
            ads = (ads//2)*3
        
        return output
    pattern = calc_pattern()
    return sum(pattern[:n])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

    

'''
3

9
'''