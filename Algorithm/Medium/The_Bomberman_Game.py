'''
The Bomberman Game
https://www.hackerrank.com/challenges/bomber-man/problem?isFullScreen=true
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bomberMan function below.
def bomberMan(n, grid):
    # track the time laps 1 second before explode.
    def timeLaps(g):
        t = list(map(lambda r:list(map(int,r.replace('O','1').replace('.','2') )),g))
        for i in range(len(t)):
            for j in range(len(t[i])):
                if t[i][j] == 1:
                    t[i][j] = 3
                    # up
                    if i-1 >= 0:
                        if t[i-1][j] != 3:
                            t[i-1][j] = 3
                    # down
                    if i+1 < len(t):
                        if t[i+1][j] != 1:
                            t[i+1][j] = 3
                    # left
                    if j-1 >= 0:
                        if t[i][j-1] != 3:
                            t[i][j-1] = 3
                    # right
                    if j+1 < len(t[i]):
                        if t[i][j+1] != 1:
                            t[i][j+1] = 3
                elif t[i][j] != 3:
                    t[i][j] -= 1
        _t = list(map(lambda r: ''.join(list(map(str,r))), t))
        return list(map(lambda r: r.replace('1','O').replace('3','.'), _t))

    if n == 1:
        return grid
    elif n == 2:
        return list(map(lambda row: row.replace('.', 'O'), grid))
    else:
        if ((n - 1) / 2) % 2 == 1:
            return timeLaps(grid)
        elif ((n - 1) / 2) % 2 == 0:
            temp_grid = timeLaps(grid)
            return timeLaps(temp_grid)
        else:
            return list(map(lambda row: row.replace('.', 'O'), grid))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()


'''
6 7 3
.......
...O...
....O..
.......
OO.....
OO.....

OOO.OOO
OO...OO
OOO...O
..OO.OO
...OOOO
...OOOO
'''