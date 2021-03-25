"""python-loctraceback packaging information"""

# To the extent possible we make this file look more like a
# configuration file rather than code like setup.py. I find putting
# configuration stuff in the middle of a function call in setup.py,
# which for example requires commas in between parameters, is a little
# less elegant than having it here with reduced code, albeit there
# still is some room for improvement.

# Things that change more often go here.
copyright   = """
Copyright (C) 2018 Rocky Bernstein <rb@dustyfeet.com>.
"""

classifiers =  ['Development Status :: 3 - Alpha',
                'Intended Audience :: Developers',
                'Operating System :: OS Independent',
                'License :: OSI Approved :: Python Software Foundation License',
                'Programming Language :: Python',
                'Programming Language :: Python :: 3.3',
                'Programming Language :: Python :: 3.4',
                'Programming Language :: Python :: 3.5',
                'Programming Language :: Python :: 3.6',
                'Programming Language :: Python :: 3.7',
                'Programming Language :: Python :: 3.8',
                'Topic :: Software Development :: Debuggers',
                'Topic :: Software Development :: Libraries :: Python Modules',
                ]

# The rest in alphabetic order
author             = "Rocky Bernstein"
author_email       = "rb@dustyfeet.com"
ftp_url            = None
install_requires   = ['uncompyle6 >= 3.0.1', # uses newer API
                      'xdis >= 5.0.0, < 5.1.0',  # ditto
                      ]

license            = 'GPL-3.0'
mailing_list       = 'python-debugger@googlegroups.com'
modname            = 'loctraceback'
py_modules         = None
short_desc         = 'traceback with more exact location info'
web                = 'https://github.com/rocky/python-loctraceback/'

# tracebacks in zip files are funky and not debuggable
zip_safe = True

import os.path
def get_srcdir():
    filename = os.path.normcase(os.path.dirname(os.path.abspath(__file__)))
    return os.path.realpath(filename)

srcdir = get_srcdir()

def read(*rnames):
    return open(os.path.join(srcdir, *rnames)).read()

# Get info from files; set: long_description and __version__
long_description   = ( read("README.rst") + '\n' )
exec(read('loctraceback/version.py'))
