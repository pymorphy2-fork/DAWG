# DAWG2

[![image](https://github.com/pymorphy2-fork/DAWG/actions/workflows/tests.yml/badge.svg)](https://github.com/pymorphy2-fork/DAWG/actions/workflows/tests.yml)
[![image](https://coveralls.io/repos/github/pymorphy2-fork/DAWG/badge.svg?branch=master)](https://coveralls.io/github/pymorphy2-fork/DAWG?branch=master)
[![image](https://img.shields.io/pypi/v/dawg2)](https://pypi.org/project/dawg2/)
![image](https://img.shields.io/pypi/pyversions/dawg2)

This is a fork of [DAWG](https://pypi.org/project/DAWG/) project rebuilt
with Python 3.10+ support.

Installation:

    pip install dawg2

But imported name is still `dawg`, not dawg2.

This package provides DAWG
([DAFSA](https://en.wikipedia.org/wiki/Deterministic_acyclic_finite_state_automaton))-based
dictionary-like read-only objects for Python.

String data in a DAWG may take 200x less memory than in a standard
Python dict and the raw lookup speed is comparable; it also provides
fast advanced methods like prefix search.

- Docs: <https://dawg.readthedocs.org>
- Source code: <https://github.com/pymorphy2-fork/DAWG>
- New issue tracker: <https://github.com/pymorphy2-fork/DAWG/issues>
- "Old" issue tracker: <https://github.com/pytries/DAWG/issues>

# License

Wrapper code is licensed under MIT License. Bundled
[dawgdic](https://code.google.com/p/dawgdic/) C++ library is licensed
under BSD license. Bundled [libb64](http://libb64.sourceforge.net/) is
Public Domain.
