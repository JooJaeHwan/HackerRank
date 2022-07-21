'''
ACM ICPC Team
https://www.hackerrank.com/challenges/acm-icpc-team/problem?isFullScreen=true
'''


import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    ans = []
    for i in range(n):
        for j in range(i+1, n):
            know=0            
            for a,b in zip(topic[i], topic[j]):
                if a=='1' or b=='1':
                   know+=1
            ans.append(know)
    return [max(ans), ans.count(max(ans))]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()



'''
4 5
10101
11100
11010
00101

5
2
'''