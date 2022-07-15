'''
Queen's Attack II
https://www.hackerrank.com/challenges/queens-attack-2/problem?isFullScreen=true
'''


import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    moves = {'n': n - r_q, 'nw': min(n - r_q, c_q-1), 'ne': min(n - r_q, n - c_q),
         's': r_q-1, 'sw': min(r_q-1, c_q-1), 'se': min(r_q-1, n - c_q), 'w': c_q-1, 'e': n - c_q}
    for r, c in obstacles:
        if c == c_q:
            if r > r_q:
                moves['n'] = min(r-r_q-1, moves['n'])
            else:
                moves['s'] = min(r_q-r-1, moves['s'])
        elif r == r_q:
            if c > c_q:
                moves['e'] = min(c-c_q-1, moves['e'])
            else:
                moves['w'] = min(c_q-c-1, moves['w'])
        elif c - r == c_q - r_q:
            if c < c_q and r < r_q:
                moves['sw'] = min(min(c_q-c-1, r_q-r-1), moves['sw'])
            elif c > c_q and r > r_q:
                moves['ne'] = min(min(c-c_q-1, r-r_q-1), moves['ne'])
        elif c + r == c_q + r_q:
            if c < c_q and r > r_q:
                moves['nw'] = min(min(r-r_q-1, c_q-c-1), moves['nw'])
            elif c > c_q and r < r_q:
                moves['se'] = min(min(r_q-r-1, c-c_q-1), moves['se'])
    return sum(moves.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()


'''
5 3
4 3
5 5
4 2
2 3
10
'''
