#! /usr/bin/env python
import glob
from setuptools import setup, Extension
from Cython.Build import cythonize


extensions = [
    Extension(
        "dawg",
        sources=glob.glob('src/*.pyx')# + glob.glob('lib/b64/*.c'),
        include_dirs=['lib'],
        extra_compile_args=["-a", "--cplus", "-2"],
        language="c++",
    )
]

setup(
    name="DAWG2",
    version="0.9.1",
    description="Fast and memory efficient DAWG (DAFSA) for Python",
    long_description=open('README.rst').read() + '\n\n' + open('CHANGES.rst').read(),
    author='Mikhail Korobov',
    author_email='kmike84@gmail.com',
    url='https://github.com/pymorphy2-fork/DAWG/',

    ext_modules=cythonize(extensions),

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Cython',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing :: Linguistic',
    ],
)
