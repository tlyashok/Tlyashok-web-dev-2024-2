def wrapper(f):
    def fun(l):
        sorted_numbers = []
        for number in l:
            s = number
            if len(s) == 11:
                s = s[1:]
            s = '+7 (' + s[:3] + ') ' + s[3:6] + '-' + s[6:8] + '-' + s[8:10]
            sorted_numbers.append(s)
        sorted_numbers.sort()
        return sorted_numbers
    return fun

@wrapper
def sort_phone(l):
    return l


if __name__ == '__main__':
    n = int(input())
    l = [input() for _ in range(n)]
    result = sort_phone(l)
    print(*result, sep='\n')