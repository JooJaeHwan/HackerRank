'''
Almost Sorted
https://www.hackerrank.com/challenges/almost-sorted/problem?isFullScreen=true
'''

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def almostSorted(arr):
    swap_l = -1
    swap_r = -1
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            swap_l = i - 1
            break
            
    for i in range(swap_l + 1, len(arr)):
        if i == len(arr) - 1 or arr[i + 1] > arr[swap_l]:
            swap_r = i
            arr[swap_l], arr[swap_r] = arr[swap_r], arr[swap_l]
            break
            
    if is_sorted(arr):
        print("yes")
        print("swap {} {}".format(swap_l + 1, swap_r + 1))
        return True
    
    arr[swap_l], arr[swap_r] = arr[swap_r], arr[swap_l]
    
    rev_l = -1
    rev_r = -1
    for i in range(len(arr) - 1):
        if rev_l == -1 and arr[i] > arr[i + 1]:
            rev_l = i
        elif rev_l != -1 and arr[i] < arr[i + 1]:
            rev_r = i
            break
    
    to_rev = arr[rev_l:rev_r+1]
    arr = arr[:rev_l] + to_rev[::-1] + arr[rev_r+1:]
    
    if is_sorted(arr):
        print("yes")
        print("reverse {} {}".format(rev_l + 1, rev_r + 1))
        return True
    
    print("no")
    return False

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)


'''
6
1 5 4 3 2 6

yes
reverse 2 5
'''