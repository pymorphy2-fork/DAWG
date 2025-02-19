from io import BufferedIOBase
from pathlib import Path
from typing import Any, Iterable, Iterator, Mapping, Self, TypeAlias

Replaces: TypeAlias = Mapping[str, str | list[str]]
CompiledReplaces: TypeAlias = Mapping[str, list[tuple[bytes, str]]]

class DAWG:
    def __init__(self, arg: list[str | bytes] | None = None, input_is_sorted: bool = False) -> None: ...
    def __contains__(self, key: str | bytes) -> bool: ...
    def has_key(self, key: str) -> bool: ...
    def b_has_key(self, key: bytes) -> bool: ...
    def tobytes(self) -> bytes: ...
    def frombytes(self, data: bytes) -> Self: ...
    def read(self, f: BufferedIOBase) -> None: ...
    def write(self, f: BufferedIOBase) -> None: ...
    def load(self, path: str | bytes) -> Self: ...
    def save(self, path: str | bytes | Path) -> None: ...
    def similar_keys(self, key: str, replaces: CompiledReplaces) -> list[str]: ...
    def prefixes(self, key: str) -> list[str]: ...
    def b_prefixes(self, b_key: bytes) -> list[bytes]: ...
    def iterprefixes(self, key: str) -> Iterator[str]: ...
    @staticmethod
    def compile_replaces(replaces: Replaces) -> CompiledReplaces: ...

class CompletionDAWG(DAWG):
    def __init__(self, arg: list[str | bytes] | None = None, input_is_sorted: bool = False) -> None: ...
    def keys(self, prefix: str = "") -> list[str]: ...
    def iterkeys(self, prefix: str = "") -> Iterator[str]: ...
    def has_keys_with_prefix(self, prefix: str) -> bool: ...
    def tobytes(self) -> bytes: ...
    def frombytes(self, data: bytes) -> Self: ...
    def load(self, path: str | bytes) -> Self: ...

PAYLOAD_SEPARATOR: bytes
MAX_VALUE_SIZE: int

class BytesDAWG(CompletionDAWG):
    def __init__(self, arg: Iterable[tuple[str, bytes]] | None = None, payload_separator: bytes = PAYLOAD_SEPARATOR) -> None: ...
    def load(self, path: str | bytes) -> Self: ...
    def frombytes(self, data: bytes) -> Self: ...
    def b_has_key(self, key: bytes) -> bool: ...
    def __getitem__(self, key: str | bytes) -> list[bytes]: ...
    def get(self, key: str | bytes, default: list[bytes] | None = None) -> list[bytes] | None: ...
    def get_value(self, key: str) -> list[bytes]: ...
    def b_get_value(self, key: bytes) -> list[bytes]: ...
    def items(self, prefix: str = "") -> list[tuple[str, bytes]]: ...
    def iteritems(self, prefix: str = "") -> Iterator[tuple[str, bytes]]: ...
    def keys(self, prefix: str = "") -> list[str]: ...
    def iterkeys(self, prefix: str = "") -> Iterator[bytes]: ...
    def similar_items(self, key: str, replaces: CompiledReplaces) -> list[tuple[str, bytes]]: ...
    def similar_item_values(self, key: str, replaces: CompiledReplaces) -> list[bytes]: ...

class RecordDAWG(BytesDAWG):
    def __init__(self, fmt: str | bytes, arg: Iterable[tuple[str, tuple[Any, ...]]] | None = None, payload_separator: bytes = PAYLOAD_SEPARATOR) -> None: ...
    def items(self, prefix: str = "") -> list[tuple[str, tuple[Any, ...]]]: ...
    def iteritems(self, prefix: str | bytes = "") -> Iterator[tuple[str, tuple[Any, ...]]]: ...

LOOKUP_ERROR: int

class IntDAWG(DAWG):
    def __init__(self, arg: Iterable[tuple[str, int]] | Mapping[str, int] | None = None, input_is_sorted: bool = False) -> None: ...
    def __getitem__(self, key: str | bytes) -> int | None: ...
    def get(self, key: str | bytes, default: int | None = None) -> int | None: ...
    def get_value(self, key: str) -> int: ...
    def b_get_value(self, key: bytes) -> int: ...

class IntCompletionDAWG(CompletionDAWG, IntDAWG):
    def __init__(self, arg: Iterable[tuple[str, int]] | Mapping[str, int] | None = None, input_is_sorted: bool = False) -> None: ...
    def __getitem__(self, key: str | bytes) -> int: ...
    def get(self, key: str | bytes, default: int | None = None) -> int: ...
    def get_value(self, key: str) -> int: ...
    def b_get_value(self, key: bytes) -> int: ...
    def items(self, prefix: str = "") -> list[tuple[str, int]]: ...
    def iteritems(self, prefix: str = "") -> Iterator[tuple[str, int]]: ...
