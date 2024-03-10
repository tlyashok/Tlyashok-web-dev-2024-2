def check_number(n):
    if n % 2 != 0:
        return "Weird"
    else:
        if n in range(2, 6):
            return "Not Weird"
        elif n in range(6, 21):
            return "Weird"
        else:
            return "Not Weird"

n = int(input())
result = check_number(n)
print(result)