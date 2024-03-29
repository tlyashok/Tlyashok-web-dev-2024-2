import sys

def my_sum_argv():
    args = sys.argv[1:]
    args = map(float, args)
    result = sum(args)
    print(result)