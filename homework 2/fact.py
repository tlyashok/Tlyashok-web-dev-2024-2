import timeit

def fact_rec(n):
    if n == 1:
        return 1
    return fact_rec(n-1) * n

def fact_it(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

if __name__ == '__main__':
    #fact_rec(100) - 4E-5
    #fact_it(100)  - 3E-5
    print(timeit.timeit(lambda: fact_it(100), number=5), 
          timeit.timeit(lambda: fact_rec(100), number=5))