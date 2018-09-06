from typing import TypeVar, Generic

Item = TypeVar('Item')


class List(Generic[Item]):
    def __init__(self, value: Item) -> None:
        self.value = value
        self.tail = None

    def append(self, value: Item):
        if self.tail is None:
            self.tail = item
        else:
            self.tail.append(item)
