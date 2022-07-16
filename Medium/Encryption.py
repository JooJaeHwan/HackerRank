'''
Encryption
https://www.hackerrank.com/challenges/encryption/problem?isFullScreen=true
'''

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    answer_str = ""
    s_len = len(s)
    len_sqrt = math.sqrt(s_len)
    row = math.floor(len_sqrt)
    col = math.ceil(len_sqrt)
    
    for i in range(0, col):
        for j in range(i, s_len, col):
            answer_str += s[j]
        answer_str += ' '

    return answer_str
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

'''
haveaniceday
hae and via ecy
'''