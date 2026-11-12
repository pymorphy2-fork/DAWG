#!/usr/bin/env python
import glob
import os
import re
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

from Cython.Build import cythonize
from setuptools import Extension, setup

config = tomllib.loads(Path(__file__).with_name("pyproject.toml").read_text(encoding="utf8"))
python_range = re.fullmatch(r">=3\.(\d+),<3\.(\d+)", config["project"]["requires-python"])
if python_range is None:
    raise ValueError('requires-python must have the form ">=3.MIN,<3.MAX"')
min_python, max_python = map(int, python_range.groups())
if min_python >= max_python:
    raise ValueError("requires-python must describe a non-empty range")
classifiers = config["tool"]["dawg"]["classifiers"] + [
    f"Programming Language :: Python :: 3.{minor}"
    for minor in range(min_python, max_python)
]

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
    classifiers=classifiers,
    ext_modules=cythonize(
        extensions,
        annotate=False,
        compiler_directives=compiler_directives,
    ),
)
