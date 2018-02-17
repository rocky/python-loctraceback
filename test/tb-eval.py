import loctraceback as traceback
import sys

# from traceback_example import produce_exception

ns = {'a': 1,
      'b': 1,
      'c': 0}
s = "%s / %s / %s" % tuple(sorted(ns.keys()))
try:
    eval(s, ns)
except Exception as err:
    print( 'print_exc():')
    traceback.print_exc(file=sys.stdout)
    print()
    print('print_exc(1):')
    traceback.print_exc(limit=1, file=sys.stdout)
