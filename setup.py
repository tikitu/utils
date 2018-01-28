# -*- coding: utf-8 -*-
import re
from setuptools import setup


REQUIRES = [
]


def find_version(fname):
    '''Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    '''
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version

__version__ = find_version("utils/__init__.py")


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content

setup(
    name='tikitu-utils',
    version=__version__,
    description='Handy utilities.',
    long_description=read("README.rst"),
    author='Tikitu de Jager',
    author_email='tikitu@logophile.org',
    # url='https://bitbucket.org/tikitu/dripfeed',
    install_requires=REQUIRES,
    license=read("LICENSE"),
    zip_safe=False,
    keywords='utilities',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    packages=["utils"],
    entry_points={
        'console_scripts': [
            "worked = utils:worked"
        ]
    },
#    tests_require=[
#        'nose',
#        'mock',
#    ],
#    test_suite='nose.collector'
)
