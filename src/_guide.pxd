from _base_types cimport BaseType, CharType, SizeType, UCharType, ValueType
from _guide_unit cimport GuideUnit
from iostream cimport istream, ostream


cdef extern from "../lib/dawgdic/src/dawgdic/guide.h" namespace "dawgdic":
    cdef cppclass Guide:

        Guide()

        GuideUnit *units()
        SizeType size()
        SizeType total_size()
        SizeType file_size()

        # The root index.
        BaseType root()

        UCharType child(BaseType index)
        UCharType sibling(BaseType index)

        # Reads a dictionary from an input stream.
        bint Read(istream *input)

        # Writes a dictionry to an output stream.
        bint Write(ostream *output)

        # Maps memory with its size.
        void Map(void *address)

        # Swaps Guides.
        void Swap(Guide *Guide)

        # Initializes a Guide.
        void Clear()