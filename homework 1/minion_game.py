#!/bin/env python3

vowels = 'AEIOU'

string = input()
stuart = 0
kevin = 0
substrings = set()

for i in range(1, len(string)+1):
    for j in range(len(string)-i+1):
        substrings.add(string[j:j+i])

for substring in substrings:
    if substring[0] in vowels:
        kevin += string.count(substring)
    else:
        stuart += string.count(substring)

if kevin > stuart:
    print('Кевин', kevin, sep=' ')
elif stuart > kevin:
    print('Стюарт', stuart, sep=' ')
else:
    print('Ничья', stuart, sep=' ')
