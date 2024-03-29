#!/bin/env python3

def isLeap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if __name__ == '__main__':
    year = int(input())
    print(isLeap(year))
        
