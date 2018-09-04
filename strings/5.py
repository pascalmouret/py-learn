'''
Problem:
    Write a method to replace all spaces in a string with ‘%20’
'''

import unittest


def urlencode_spaces(input):
    if not isinstance(input, str):
        raise TypeError('Non-string value provided.')

    pos = 0
    while pos < len(input):
        if input[pos] == ' ':
            input = input[:pos] + '%20' + input[pos + 1:]
            pos = pos + 3
        else:
            pos = pos + 1

    return input


class UrlencodeSpacesSpec(unittest.TestCase):
    def test_type(self):
        with self.assertRaises(TypeError):
            urlencode_spaces(1234)

    def test_no_space(self):
        self.assertEqual(urlencode_spaces('abc'), 'abc')
    
    def test_only_space(self):
        self.assertEqual(urlencode_spaces(' '), '%20')
        
    def test_simple_space(self):
        self.assertEqual(urlencode_spaces('ab c'), 'ab%20c')
        self.assertEqual(urlencode_spaces('abc '), 'abc%20')
        self.assertEqual(urlencode_spaces(' abc'), '%20abc')

    def test_multiple_spaces(self):
        self.assertEqual(urlencode_spaces('ab  c'), 'ab%20%20c')
        self.assertEqual(urlencode_spaces('   '), '%20%20%20')
        
        
if __name__ == '__main__':
    unittest.main()