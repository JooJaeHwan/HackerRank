'''
Lily's Homework
https://www.hackerrank.com/challenges/lilys-homework/problem?isFullScreen=true
'''


import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def solution(arr):
    cnt = 0
    n = len(arr)
    sorted_arr = sorted(arr)
    index_dict = {arr[i] : i for i in range(n)}
 
    for i in range(n):
        if arr[i] != sorted_arr[i]:
            get_index = index_dict[sorted_arr[i]]
            index_dict[arr[i]] = index_dict[sorted_arr+[i]]
            arr[i], arr[get_index] = sorted_arr[i], arr[i]
            cnt += 1

    return cnt

def lilysHomework(arr):
    reversed_arr = list(reversed(arr))

    return min(solution(arr), solution(reversed_arr))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


'''
4
2 5 3 1 

2
'''