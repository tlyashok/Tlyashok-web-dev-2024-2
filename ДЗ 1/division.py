a = int(input())
b = int(input())

try:
    print(a // b)
    print(a / b)
except ZeroDivisionError:
    print("Деление на ноль невозможно.")