loctraceback
============

Want to see more precisely where you are or were at in a traceback or
callstack your Python code has several places in a line it could have
errored? Even if the code was something created at runtime with say
`eval` or `exec`?

Then this package is for you.

Some examples of the kinds of code this module can disambiguate:

.. code-block:: python

   i / j / k                              # which divide?
   prev[prev[0]]                          # which prev ?
   [e[0] for i in d[j] if got[i] == e[i]] # lots going on here
   exec(some_code % 10, namespace)        # code at runtime

Some example output (which can be found by running code in `example`:


Division example:

.. code-block:: python

    Traceback (most recent call last):
      File "tb-div.py", line 9, in <module> at offset 52
        a / b / c
        a / b / c
          -
    ZeroDivisionError: float division by zero


List comprehension example:

.. code-block:: python


    File "tb-comp.py", line 9, in <listcomp> at offset 18
        [e[0] for i in d[j] if got[i] == e[i]]
    return [ e[0] for i in .0 if got[i] == e[i] ]
                                 ------
    IndexError: list index out of range

`exec` example:

.. code-block:: python

    Traceback (most recent call last):
     File "tb-exec.py", line 11, in <module> at offset 39
        exec(s)
        exec(s)
        -------
      File "<string>", line 4, in <module> at offset 18
      z = x / y
            -
      ZeroDivisionError: division by zero

Isolating function in call stack example:

.. code-block:: python

      File "call-fib.py", line 8, in fib at offset 58
        return fib(n-1) + fib(n-2)
        return fib(n - 1) + fib(n - 2)
                            ----------
          File "call-fib.py", line 10, in <module> at offset 54
               print("fib({})={}".format(2, fib(2)))
                                            ------

This modules extends the Python 3.6 API traceback module by adding in
fragment decomplation info for more precise location information.

Although the API is from Python 3.6, the code runs on 3.3 or greater.
Back-porting to ther Python versions is left as an exercise to the
reader.

See `these slides <http://rocky.github.io/pycon2018.co>`_ for
information on the technology behind this.
