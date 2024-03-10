import csv

total_expenses = {'Взрослый': 0, 'Пенсионер': 0, 'Ребенок': 0}

with open('products.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        total_expenses['Взрослый'] += float(row['Взрослый'])
        total_expenses['Пенсионер'] += float(row['Пенсионер'])
        total_expenses['Ребенок'] += float(row['Ребенок'])

for category, expenses in total_expenses.items():
    print(f"{expenses:.2f}", end=" ")