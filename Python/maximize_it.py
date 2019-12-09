# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

first_multiple_input = input().rstrip().split()
k = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(k):
    matrix_item = input().strip().split()
    matrix.append([int(i) for i in matrix_item[1:]])
# print(matrix)

results = map(lambda x: sum(i**2 for i in x)%m, product(*matrix))
print(max(results))
