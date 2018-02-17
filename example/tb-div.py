import loctraceback as traceback
import sys

# from traceback_example import produce_exception

# a, b, c = 1, 0, 1
a, b, c = 1, 1, 0
try:
    a / b / c
except Exception as err:
    print( 'print_exc():')
    traceback.print_exc(file=sys.stdout)
    print()
    print('print_exc(1):')
    traceback.print_exc(limit=1, file=sys.stdout)
