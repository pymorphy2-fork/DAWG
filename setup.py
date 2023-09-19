#! /usr/bin/env python
import glob
import os

from Cython.Build import cythonize
from setuptools import Extension, setup

TEST = os.environ.get("TEST", "false").casefold() == "true"

compiler_directives = {"language_level": 3}
define_macros = []

if TEST:
    compiler_directives.update({"linetrace": True, "profile": True})
    define_macros.extend([("CYTHON_TRACE", "1"), ("CYTHON_TRACE_NOGIL", "1")])

extensions = [
    Extension(
        "dawg",
        sources=glob.glob("src/*.pyx") + glob.glob("lib/b64/*.c"),
        include_dirs=["lib"],
        language="c++",
        define_macros=define_macros,
    )
]

ext_modules = cythonize(
    extensions,
    language="c++",
    annotate=False,
    compiler_directives=compiler_directives,
)

setup(
    name="DAWG2",
    version="0.10.0",
    description="Fast and memory efficient DAWG (DAFSA) for Python",
    long_description=open("README.md").read() + "\n\n" + open("CHANGES.md").read(),
    author="Mikhail Korobov",
    author_email="kmike84@gmail.com",
    url="https://github.com/pymorphy2-fork/DAWG/",
    ext_modules=ext_modules,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Cython",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Text Processing :: Linguistic",
    ],
)
