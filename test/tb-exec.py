import loctraceback as traceback
import sys

# from traceback_example import produce_exception

s = """
x = 1
y = 0
z = x / y"""
try:
    exec(s)
except Exception as err:
    print( 'print_exc():')
    traceback.print_exc(file=sys.stdout)
    print()
    print('print_exc(1):')
    traceback.print_exc(limit=1, file=sys.stdout)
