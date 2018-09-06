from typing import Generic, List, TypeVar, Any, Callable

Item = TypeVar('Item')


class Node(Generic[Item]):
    def __init__(
            self, 
            value: Item, 
            children: List['Node[Item]'] = None) -> None:
        self.value = value
        if children is None:
            children = []
        self.children = children

    def add_child(self, child: 'Node[Item]') -> None:
        self.children.append(child)

    def remove_child(self, value: 'Node[Item]') -> None:
        self.children = [c for c in self.children if c.value != value]

    def __repr__(self):
        return 'Node(%s)' % self.value.__repr__()


class BTree(Generic[Item]):
    def __init__(
            self, 
            value: Item, 
            left: 'BTree[Item]' = None, 
            right: 'BTree[Item]' = None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def traverse(self, callback) -> None:
        if self.left:
            self.left.traverse(callback)
        callback(self.value)
        if self.right:
            self.right.traverse(callback)

    def __repr__(self):
        return 'BTree(%s, %s, %s)' % (self.left, self.value, self.right)
