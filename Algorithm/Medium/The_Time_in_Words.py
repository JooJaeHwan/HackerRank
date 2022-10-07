'''
The Time in Words
https://www.hackerrank.com/challenges/the-time-in-words/problem?isFullScreen=true
'''

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    time = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen",15:"quarter", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty", 30:"half"}
    if int(m) > 30:
        if 60-int(m) in time:
            if 60-int(m) == 15 or 60-int(m) == 30:
                return time[60-int(m)] + " to " + time[h+1]
            if 60- int(m) == 1:
                return time[60-int(m)] + " minute" + " to " + time[h+1]
            else:
                return time[60-int(m)] + " minutes" + " to " + time[h+1]
        else:
            if (60-int(m))%10 == 1:
                return time[20] + " " + time[int(m)%10] + " minute" + " to " + time[h+1]
            return time[20] + " " + time[(60-int(m))%10] +" minutes" + " to " + time[h+1]
    else:
        if m == 00:
            return time[h] + " o' clock"
        if int(m) in time:
            if int(m) == 15 or int(m) == 30:
                return time[int(m)] + " past " + time[h]
            if int(m) == 1:
                return time[int(m)] + " minute" + " past " + time[h]
            else:
                return time[int(m)] + " minutes" + " past " + time[h]
        else:
            if int(m)%10 == 1:
                return time[20] + " " + time[int(m)%10] + " minute" + " past " + time[h]
            return time[20] + " " + time[int(m)%10] + " minutes" + " past " + time[h]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()

'''
5
47
thirteen minutes to six
'''