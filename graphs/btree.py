import abc
import unittest
from typing import Generic, TypeVar, Callable, List, Any, Type


class AbstractItem(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __lt__(self, other: Any) -> bool: ...


Item = TypeVar('Item', bound=AbstractItem)


class BTree(Generic[Item]):
    def __init__(
            self, 
            value: Item, 
            left: 'BTree[Item]' = None, 
            right: 'BTree[Item]' = None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def traverse(self, callback: Callable[[Item], None]) -> None:
        if self.left:
            self.left.traverse(callback)
        callback(self.value)
        if self.right:
            self.right.traverse(callback)

    def insert(self, value: Item) -> None:
        if value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = self.__class__(value)
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = self.__class__(value)

    @classmethod
    def from_list(cls, items: List[Item]):
        '''
        Create a BTree based on a list. There is no gurantee of a balanced
        tree.
        Note: There is no type hint because it seems the type system cannot
        handle generic classmethods.
        '''
        if not len(items):
            return None

        root = cls(items[0])
        if len(items) > 1:
            for item in items[1:]:
                root.insert(item)

        return root

    def __eq__(self, other):
        return isinstance(other, BTree) and self.__dict__ == other.__dict__
            
    def __repr__(self):
        return 'BTree(%s, %s, %s)' % (self.left, self.value, self.right)



class BTreeTest(unittest.TestCase):
    def test_from_list(self):
        self.assertEqual(
            BTree.from_list([1, 2, 3]),
            BTree(1, None, BTree(2, None, BTree(3)))
        )
        self.assertEqual(
            BTree.from_list([1, 2, 3, 4]),
            BTree(1, None, BTree(2, None, BTree(3, None, BTree(4))))
        )
        self.assertEqual(
            BTree.from_list([3, 2, 5, 4, 1]),
            BTree(3, BTree(2, BTree(1)), BTree(5, BTree(4)))
        )
        self.assertEqual(
            BTree.from_list([]),
            None
        )
        self.assertEqual(
            BTree.from_list([1]),
            BTree(1)
        )


if __name__ == '__main__':
    unittest.main()
        
