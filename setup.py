#!/usr/bin/env python
"""Setup script for the 'xdis' distribution."""

from __pkginfo__ import \
    author,           author_email,       install_requires,          \
    license,          long_description,   classifiers,               \
    modname,          py_modules,                     \
    short_desc,       \
    VERSION,          web,                zip_safe

from setuptools import setup, find_packages
setup(
       author             = author,
       author_email       = author_email,
       classifiers        = classifiers,
       description        = short_desc,
       install_requires   = install_requires,
       license            = license,
       long_description   = long_description,
       name               = modname,
       packages           = find_packages(),
       py_modules         = py_modules,
       url                = web,
       version            = VERSION,
       zip_safe           = zip_safe)
