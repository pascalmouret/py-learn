'''
Problem: 
    Determine if string has only unique characters. Do not use additional data structures.
'''

import unittest


'''
Check each character in the string against ever character coming after it. If any
comparison is true, return false.

This will not take into consideration character that look the same but have different
unicode designations.
'''
def has_no_duplicate_chars(input):
    if not isinstance(input, str):
        raise TypeError('Can only perform check on strings.')

    search_pos = 0
    # loop through all characters except the last - it can't be a duplicate at that point
    while (search_pos < len(input) - 1):
        current_pos = search_pos + 1
        while (current_pos < len(input)):
            if input[search_pos] == input[current_pos]:
                return False
            current_pos = current_pos + 1
        search_pos = search_pos + 1

    return True


class HasNoDuplicateCharsSpec(unittest.TestCase):
    def test_type(self):
        with self.assertRaises(TypeError):
            has_no_duplicate_chars(True)
        with self.assertRaises(TypeError):
           has_no_duplicate_chars(1234)

    def test_finds_duplicate(self):
        self.assertTrue(has_no_duplicate_chars('abcd'))
        self.assertFalse(has_no_duplicate_chars('aabcd'))
        self.assertFalse(has_no_duplicate_chars('abcdd'))
        self.assertFalse(has_no_duplicate_chars('abcdb'))


if __name__ == '__main__':
    unittest.main()