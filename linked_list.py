from typing import Any, Optional, List, Generator

from _types import Predicate


class NotFoundException(Exception):
    pass


class Node:
    def __init__(self, value: Any, next_: Optional['Node'] = None) -> None:
        self.value = value
        self.next = next_


class LinkedList:
    def __init__(self, values: Optional[List] = None) -> None:
        if values:
            self.root = Node(values[0])

            current = self.root
            for value in values[1:]:
                current.next = Node(value)
                current = current.next

            self._last_node = current
        else:
            self.root = None
            self._last_node = None

    def __eq__(self, other: Any) -> NotImplemented:
        return NotImplemented

    def __repr__(self) -> str:
        class_name = type(self).__name__
        values = list(self)
        return f'{class_name}({repr(values)})'

    def __iter__(self) -> Generator[Any, None, None]:
        current = self.root
        while current is not None:
            yield current.value
            current = current.next

    def add(self, value: Any) -> None:
        if self.root is not None:
            self._last_node.next = Node(value)
            self._last_node = self._last_node.next
        else:
            self.root = Node(value)
            self._last_node = self.root

    def search(self, predicate: Predicate) -> Any:
        try:
            return next(value for value in self if predicate(value))
        except StopIteration:
            raise NotFoundException

    def is_empty(self) -> bool:
        return self.root is None
