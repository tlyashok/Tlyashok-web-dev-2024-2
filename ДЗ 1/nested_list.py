N = int(input())

students = []

for _ in range(N):
    name = input()
    score = float(input())
    students.append([name, score])

students.sort(key=lambda x: x[1])

second_highest_score = students[1][1]

second_highest_names = []

for student in students:
    if student[1] == second_highest_score:
        second_highest_names.append(student[0])

second_highest_names.sort()

for name in second_highest_names:
    print(name)