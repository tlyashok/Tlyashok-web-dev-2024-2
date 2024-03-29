#!/bin/env python3

size = int(input())
matrix1 = [list(map(int, input().split())) for _ in range(size)]
matrix2 = [list(map(int, input().split())) for _ in range(size)]
# matrix1_transposed = [[matrix1[j][i] for j in range(size)] for i in range(size)]
matrix2_transposed = [[matrix2[j][i] for j in range(size)] for i in range(size)]
matrix3 = [[0 for _ in range(size)] for _ in range(size)]
for i in range(size):
    for j in range(size):
        matrix3[i][j] = sum([matrix1[i][k] * matrix2_transposed[j][k] for k in range(size)])
for line in matrix3:
    print(*line)
