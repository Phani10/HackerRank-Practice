#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    hops = len(c)
    count = 0
    index = 0
    print(hops)

    while index <= hops:
        print(index)
        try:
            if c[index+2] == 0:
                index += 2
            else:
                index += 1
        except IndexError:
            if index+2 == hops:
                count += 1
            return count
        count += 1 
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
