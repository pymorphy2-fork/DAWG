#!/usr/bin/env python
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

setup(
    name="DAWG2",
    ext_modules=cythonize(
        extensions,
        annotate=False,
        compiler_directives=compiler_directives,
    ),
)
