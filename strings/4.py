'''
Problem:
    Write a method to decide if two strings are anagrams or not.
'''

import unittest


'''
Check if two strings are anagrams by sorting and comparing them.
'''
def is_anagram(input1, input2):
    if not isinstance(input1, str) or not isinstance(input2, str):
        raise TypeError('Must be strings that are compared.')

    return sorted(list(input1)) == sorted(list(input2))


class IsAnagramSpec(unittest.TestCase):
    def test_type(self):
        with self.assertRaises(TypeError):
            is_anagram(1, 'abc')
        with self.assertRaises(TypeError):
            is_anagram('abc', 1)

    def test_unique_anagrams(self):
        self.assertTrue(is_anagram('abc', 'cba'))
        self.assertFalse(is_anagram('abcd', 'bca'))
        self.assertFalse(is_anagram('abcd', 'bcak'))

    def test_multi_anagrams(self):
        self.assertTrue(is_anagram('abacb', 'aabbc'))

    def test_equal_same(self):
        self.assertTrue(is_anagram('abc', 'abc'))
        self.assertTrue(is_anagram('aaa', 'aaa'))


if __name__ == '__main__':
    unittest.main()