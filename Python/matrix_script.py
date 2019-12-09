#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

my_string = list()
for col in range(m):
    for row in range(n):
        my_string.append(matrix[row][col])
my_string = ''.join([i for i in my_string])

my_string = re.sub(r"(?<=\w)([^\w]+)(?=\w)",' ',my_string)
print(my_string)
