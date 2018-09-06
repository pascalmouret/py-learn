from typing import TypeVar, Generic, Optional

from pylearn.lists.list import List


Item = TypeVar('Item')


class Queue(Generic[Item]):
    def __init__(self, items: Optional[List[Item]] = None) -> None:
        self._front = items
        if self._front:
            self._back = self._front.last()

    def enqueue(self, item: Item) -> None:
        back = List(item)
        if not self._front:
            self._front = back
            self._back = back
        else:
            self._back.tail = back
            self._back = back

    def dequeue(self) -> Optional[Item]:
        if self._front:
            front = self._front
            self._front = self._front.tail
            return front.value
        return None
