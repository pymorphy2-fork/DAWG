from _base_types cimport BaseType, CharType, SizeType, UCharType, ValueType


cdef extern from "../lib/dawgdic/src/dawgdic/guide-unit.h" namespace "dawgdic":
    cdef cppclass GuideUnit:
        GuideUnit() nogil

        void set_child(UCharType child) nogil
        void set_sibling(UCharType sibling) nogil
        UCharType child() nogil
        UCharType sibling() nogil
