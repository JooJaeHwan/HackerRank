'''
Climbing the Leaderboard
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true
'''


import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

from bisect import bisect_right
'''
bisect 이분 탐색
오름차순으로 되어있어야됨
'''

def climbingLeaderboard(ranked, player):
    answer = []
    ranked = sorted(set(ranked))

    for score in player:
        answer.append(len(ranked)-bisect_right((ranked), score)+1)
        
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


'''
7
100 100 50 40 40 20 10
4
5 25 50 120
6
4
2
1
'''