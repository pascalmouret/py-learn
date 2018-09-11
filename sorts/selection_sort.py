'''
Selection Sort
Complexity: O(n^2)
'''

import abc
import unittest
from typing import Any, List


class Sortable(abc.ABCMeta):
    @abc.abstractmethod
    def __lt__(self, other: Any) -> bool: ...


def selection_sort(array: List[Sortable]) -> List[Sortable]:
    for element_index in range(0, len(array) - 1):
        min_index = element_index
        for search_index in range(element_index + 1, len(array)):
            if array[search_index] < array[min_index]:
                min_index = search_index
        tmp = array[element_index]
        array[element_index] = array[min_index]
        array[min_index] = tmp
    return array


class SelectionSortTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(selection_sort([]), [])

    def test_sort(self):
        self.assertEqual(
            selection_sort([6, 4, 0, 2]),
            [0, 2, 4, 6]
        )

    def test_equal(self):
        self.assertEqual(
            selection_sort([2, 4, 4, 2]),
            [2, 2, 4, 4]
        )


if __name__ == '__main__':
    unittest.main()