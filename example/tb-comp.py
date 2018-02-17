import loctraceback as traceback
import sys

# from traceback_example import produce_exception

try:
    got = []
    d, j, e = [[0]], 0, [0]
    [e[0] for i in d[j] if got[i] == e[i]]
    [e[0] for i in d[j] if got[i] == e[i]]
except Exception as err:
    print( 'print_exc():')
    traceback.print_exc(file=sys.stdout)
    print()
    print('print_exc(1):')
    traceback.print_exc(limit=1, file=sys.stdout)
