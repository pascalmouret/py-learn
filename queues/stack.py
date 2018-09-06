from typing import TypeVar, Generic, Optional

from pylearn.lists.list import List


Item = TypeVar('Item')


class Stack(Generic[Item]):
    def __init__(self, items: Optional[List[Item]]) -> None:
        self._top = items

    def push(self, item: Item) -> None:
        self._top = List(item, self._top)
    
    def pop(self) -> Optional[Item]:
        if self._top:
            result = self._top.value
            self._top = self._top.tail
            return result
        else:
            return None
