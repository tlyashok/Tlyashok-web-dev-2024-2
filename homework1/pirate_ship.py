#!/bin/env python3

max_weight, count_different = list(map(int, input().split()))
items = [input().split() for i in range(count_different)]
for i in range(len(items)):
    items[i][1] = int(items[i][1])
    items[i][2] = int(items[i][2])
    items[i].append(items[i][2] / items[i][1])
items.sort(key=lambda item: -item[3])

# name weight price price_to_weight_ratio
weight = 0
taken_items = []
for i in range(len(items)):
    if weight + items[i][1] <= max_weight:
        weight += items[i][1] 
        taken_items.append(items[i][0:3])
    elif weight != max_weight:
        ratio = (max_weight - weight) / items[i][1]
        weight = max_weight
        taken_items.append([items[i][0], items[i][1] * ratio, items[i][2] * ratio])
taken_items.sort(key=lambda item: -item[2])
for item in taken_items:
    print(f'{item[0]} {item[1]:.2f} {item[2]:.2f}')
