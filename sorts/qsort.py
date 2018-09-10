'''
Quick Sort
Average complexity: O(n*log^n)
Worst case complexity: O(n^2)
'''

import abc
import unittest
import math
from typing import Any, List


class Sortable(abc.ABCMeta):
    @abc.abstractmethod
    def __lt__(self, other: Any) -> bool: ...


def qsort(array: List[Sortable]) -> List[Sortable]:
    def process_partition(low: int, high: int) -> None:
        if low >= high:
            return

        low_index, high_index, pivot = low, high, array[low]
        while True:
            while array[low_index] < pivot:
                low_index = low_index + 1

            while pivot < array[high_index]:
                high_index = high_index - 1

            if low_index < high_index:
                tmp = array[high_index]
                array[high_index] = array[low_index]
                array[low_index] = tmp
                # prevent infinte back and forth
                low_index = low_index + 1
                high_index = high_index - 1
            else:
                process_partition(low, high_index)
                process_partition(high_index + 1, high)
                break

    process_partition(0, len(array) - 1)
    return array

        
class QsortSpec(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(qsort([]), [])

    def test_simple(self):
        self.assertEqual(
            qsort([3, 1]),
            [1, 3]
        )
        self.assertEqual(
            qsort([7, 4, 2, 1, 0, 9, 7]), 
            [0, 1, 2, 4, 7, 7, 9]
        )


if __name__ == '__main__':
    unittest.main()