'''
Staircas
https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true
'''

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for i in range(1,n+1):
        print(' '*(n-i) + '#'*i)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)

'''
6 
     #
    ##
   ###
  ####
 #####
######
'''