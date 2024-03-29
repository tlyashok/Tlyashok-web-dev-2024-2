from timeit import timeit

def process_list(arr):
    result = []
    for i in arr:
        if i % 2 == 0:
            result.append(i**2)
        else:
            result.append(i**3)
    return result

def process_list_gen(arr):
    for i in arr:
        if i % 2 == 0:
            yield i**2
        else:
            yield i**3

if __name__=='__main__':
    #process_list([1,2,3,4,5])     - 7E-6
    #process_list_gen([1,2,3,4,5]) - 6E-6
    print(
        timeit(lambda: process_list([1,2,3,4,5]), number=5),
        timeit(lambda: [i for i in process_list_gen([1,2,3,4,5])], number=5),
    )

