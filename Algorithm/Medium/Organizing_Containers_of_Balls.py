'''
Organizing Containers of Balls
https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem?isFullScreen=true
'''

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    Rows = []
    Cols = []
    Works = True
    
    for i in range(len(container)):
        Rows.append(sum(container[i]))
       
            
    N = [list(i) for i in zip(*container)]
    for i in range(len(container)):
        Cols.append(sum(N[i]))
  
    Rows.sort()
    Cols.sort()
    if(Rows == Cols):
        return "Possible"
    else:
        return "Impossible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()

'''
2
3
1 3 1
2 1 2
3 3 3
3
0 2 1
1 1 1
2 0 0
Impossible
Possible
'''