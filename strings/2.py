'''
Problem:
    Reverse a C-style (null terminated) string.
'''

import unittest
import math


def reverse(input):
    if not isinstance(input, str):
        raise TypeError('Tried to reverse a non-string with string only function.')
    
    input = list(input)
    
    current_pos = 0
    # use floor because for odd chracter counts we can ignore the middle
    while (current_pos < math.floor(len(input) / 2)):
        tmp = input[current_pos]
        input[current_pos] = input[-(current_pos + 1)]
        input[-(current_pos + 1)] = tmp
        current_pos = current_pos + 1

    return ''.join(input)


class ReverseSpec(unittest.TestCase):
    def test_type(self):
        with self.assertRaises(TypeError):
            reverse(1234)
        with self.assertRaises(TypeError):
            reverse(['1', '2', '3'])

    def test_reverse(self):
        self.assertEqual(reverse('abc'), 'cba')
        self.assertEqual(reverse('abcd'), 'dcba')


if __name__ == '__main__':
    unittest.main()