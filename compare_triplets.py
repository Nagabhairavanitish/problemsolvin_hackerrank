#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    k= 0
    j =0
    for i in range(len(a)):
        if (a[i] > b[i]):
            k +=1
        elif (a[i] < b[i]):
            j +=1
        else:
            k +=0
            j +=0
    return k, j

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()