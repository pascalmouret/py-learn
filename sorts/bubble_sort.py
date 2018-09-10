'''
Bubble Sort
Complexity: O(n^2)
'''

import abc
import unittest
from typing import List, Any


class Sortable(abc.ABCMeta):
    @abc.abstractmethod
    def __lt__(self, other: Any) -> bool: ...


def bubble_sort(array: List[Sortable]) -> List[Sortable]:
    sweep_again = True
    while sweep_again:
        sweep_again = False
        for index in range(0, len(array) - 1):
            if array[index] > array[index + 1]:
                tmp = array[index]
                array[index] = array[index + 1]
                array[index + 1] = tmp
                sweep_again = True
    return array


class BubbleSortSpec(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(bubble_sort([]), [])

    def test_sort(self):
        self.assertEqual(
            bubble_sort([6, 4, 0, 2]),
            [0, 2, 4, 6]
        )

    def test_equal(self):
        self.assertEqual(
            bubble_sort([2, 4, 4, 2]),
            [2, 2, 4, 4]
        )


if __name__ == '__main__':
    unittest.main()