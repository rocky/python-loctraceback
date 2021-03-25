#!/bin/bash
PACKAGE=loctraceback

# FIXME put some of the below in a common routine
function finish {
  cd $owd
}

cd $(dirname ${BASH_SOURCE[0]})
owd=$(pwd)
trap finish EXIT

if ! source ./pyenv-versions ; then
    exit $?
fi

cd ..
source VERSION.py
echo $__version__

for pyversion in $PYVERSIONS; do
    if ! pyenv local $pyversion ; then
	exit $?
    fi
    # pip bdist_egg create too-general wheels. So
    # we narrow that by moving the generated wheel.

    # Pick out first two number of version, e.g. 3.5.1 -> 35
    first_two=$(echo $pyversion | cut -d'.' -f 1-2 | sed -e 's/\.//')
    rm -fr build
    python setup.py bdist_egg bdist_wheel
    if (( $first_two >= 30 )) ; then
	mv -v dist/${PACKAGE}-$__version__-{py3,py$first_two}-none-any.whl
    else
	mv -v dist/${PACKAGE}-$__version__-{py2,py$first_two}-none-any.whl
    fi
done

python ./setup.py sdist
