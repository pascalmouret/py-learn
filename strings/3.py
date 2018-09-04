'''
Problem:
    Design analgorithmandwrite code to remove the duplicate characters in a string 
    without using any additional buffer.
'''

import unittest


'''
This function will remove any duplicate occurences of a character after the first one by
looping through the characters in the string and removing duplicates with a look ahead.
'''
def remove_duplicates(input):
    if not isinstance(input, str):
        raise TypeError('This function only takes strings.')

    char_pos = 0
    # we can skip the last character, it won't be an uncleared character
    while (char_pos < len(input) - 1):
        search_pos = char_pos + 1
        while (search_pos < len(input)):
            if input[char_pos] == input[search_pos]:
                input = input[:search_pos] + input[search_pos + 1:]
            else:
                search_pos = search_pos + 1
        char_pos = char_pos + 1

    return input


class RemoveDuplicateSpec(unittest.TestCase):
    def test_type(self):
        with self.assertRaises(TypeError):
            remove_duplicates(1234)
    
    def test_simple_remove(self):
        self.assertEqual(remove_duplicates('aabc'), 'abc')
        self.assertEqual(remove_duplicates('abac'), 'abc')
        self.assertEqual(remove_duplicates('abbca'), 'abc')

    def test_multiple_remove(self):
       self.assertEqual(remove_duplicates('abbca'), 'abc')
       self.assertEqual(remove_duplicates('abcba'), 'abc')
       self.assertEqual(remove_duplicates('abbcbcac'), 'abc')


if __name__ == '__main__':
    unittest.main()
    