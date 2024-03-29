max_score = 0
prev_max_score = 0
records = list()
count = int(input())
for i in range(count):
    name = input()
    score = float(input())
    if (score > max_score):
        prev_max_score = max_score
        max_score = score
    records.append([name, score])

for i in records:
    if i[1] == prev_max_score:
        print(i[0])