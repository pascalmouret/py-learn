'''
Merge Sort
Complexity: O(n*log^n)
'''

import abc
import math
import unittest
from typing import Any, List


class Sortable(abc.ABCMeta):
    @abc.abstractmethod
    def __lt__(self, other: Any) -> bool: ...


def merge_sort(array: List[Sortable]) -> List[Sortable]:
    if len(array) <= 1:
        return array

    half = math.floor(len(array) / 2)
    left = merge_sort(array[0:half])
    right = merge_sort(array[half:len(array)])

    l_index, r_index, result = 0, 0, []
    while len(result) < len(array):
        if left[l_index] < right[r_index]:
            result.append(left[l_index])
            l_index = l_index + 1
            if l_index == len(left):
                result.extend(right[r_index:])
        else:
            result.append(right[r_index])
            r_index = r_index + 1
            if r_index == len(right):
                result.extend(left[l_index:])
        
    return result

        
class QsortSpec(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(merge_sort([]), [])

    def test_sort(self):
        self.assertEqual(
            merge_sort([3, 1]),
            [1, 3]
        )
        self.assertEqual(
            merge_sort([7, 4, 2, 1, 0, 9, 7]), 
            [0, 1, 2, 4, 7, 7, 9]
        )

    def test_equal(self):
        self.assertEqual(
            merge_sort([2, 4, 4, 2]),
            [2, 2, 4, 4]
        )
        self.assertEqual(
            merge_sort([7, 7, 7, 7]),
            [7, 7, 7, 7]
        )


if __name__ == '__main__':
    unittest.main()