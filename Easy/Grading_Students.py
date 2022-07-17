'''
Grading Students
https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true
'''

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    for grade in grades:
        if grade < 38:
            yield grade
        else:
            if ((grade//5)+1)*5 - grade < 3:
                yield ((grade//5)+1)*5 
            else:
                yield grade

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


'''
4
73
67
38
33

75
67
40
33
'''