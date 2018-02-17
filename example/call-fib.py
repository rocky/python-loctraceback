import loctraceback as traceback
import sys

def fib(n):
    if n <= 1:
        traceback.print_stack(file=sys.stdout)
        return 1
    return fib(n-1) + fib(n-2)

print("fib({})={}".format(2, fib(2)))
