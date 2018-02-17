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


This modules extends the Python 3.6 API traceback module by adding in
fragment decomplation info for more precise location information.

Although the API is from Python 3.6, the code runs on 3.3 or greater.

It could be back-ported to earlier Python versions as well, should
there be sufficient need/interest. Volunteers?

See `these slides <http://rocky.github.io/pycon2018.co>`_ for
information on the technology behind this.
