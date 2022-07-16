'''
★★★★★
The Grid Search
https://www.hackerrank.com/challenges/the-grid-search/problem?isFullScreen=true
'''

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#
def occurrences(string, sub):
    res = []
    ind = 0
    while ind < len(string) - len(sub) + 1:
        found = string.find(sub, ind)
        if found != -1:
            res.append(found)
            ind = found + 1
        else:
            break
    return res

def gridSearch(G, P):
    for ind_g in range(len(G) - len(P) + 1):
        cur = -1
        all_occurrences = []
        for ind_p, s_pat in enumerate(P):
            all_occurrences.append(occurrences(G[ind_g + ind_p], s_pat))
        ourset = set(all_occurrences[0])
        for lst in all_occurrences:
            ourset &= set(lst)
        if len(ourset) >= 1:
            return 'YES'
            
    
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()


'''
2
10 10
7283455864
6731158619
8988242643
3830589324
2229505813
5633845374
6473530293
7053106601
0834282956
4607924137
3 4
9505
3845
3530
15 15
400453592126560
114213133098692
474386082879648
522356951189169
887109450487496
252802633388782
502771484966748
075975207693780
511799789562806
404007454272504
549043809916080
962410809534811
445893523733475
768705303214174
650629270887160
2 2
99
99
YES
NO
'''