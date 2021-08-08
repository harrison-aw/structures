from typing import Optional, Any, List, Tuple

from linked_list import LinkedList


Hash = int


class _Entry:
    def __init__(self, hash_: int, value: Any) -> None:
        self.hash = hash_
        self.value = value

    def __repr__(self) -> str:
        class_name = type(self).__name__
        hash_ = repr(self.hash)
        value = repr(self.value)
        return f'{class_name}({hash_}, {value})'


class HashMap:
    def __init__(self, data: Optional[List[Tuple[int, List]]] = None, size: int = 128) -> None:
        if data is None:
            data = []

        self._data = [LinkedList()] * size
        for entries in data:
            for hash_, value in entries:
                self._data[hash_ % size].add(_Entry(hash_, value))

    def __getitem__(self, key: Any) -> Any:
        hash_ = hash(key)
        list_ = self._data[hash_ % len(self._data)]
        return list_.search(lambda entry: entry.hash == hash_).value

    def __setitem__(self, key: Any, value: Any) -> None:
        hash_ = hash(key)
        list_ = self._data[hash_ % len(self._data)]
        for entry in list_:
            if entry.hash == hash_:
                entry.value = value
                break
        else:
            list_.add(_Entry(hash_, value))
