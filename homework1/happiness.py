#!/bin/env python3

num1, num2 = list(map(int, input().split()))
array1 =  list(map(int, input().split()))
array2 =  list(map(int, input().split()))
array3 =  list(map(int, input().split()))
happiness = 0
for i in array1:
    if i in array2: happiness += 1
    if i in array3: happiness -= 1
print(happiness)
