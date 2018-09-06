from typing import TypeVar, Generic, Iterator


Item = TypeVar('Item')


class List(Generic[Item]):
    def __init__(
            self, 
            value: Item, 
            tail: 'List[Item]' = None) -> None:
        self.value = value
        self.tail = tail

    def append(self, value: Item):
        if self.tail is None:
            self.tail = List(value)
        else:
            self.tail.append(value)

    def last(self) -> 'List[Item]':
        if not self.tail:
            return self
        else:
            return self.tail.last()

    def __iter__(self) -> Iterator[Item]:
        head = self
        while head:
            yield head.value
            head = head.tail
