__author__ = 'lenovo'
#coding=utf-8
import unittest
from ch02.owntest.name_function import get_formatted_name
class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        format_name = get_formatted_name('king','ivan')
        self.assertEqual(format_name,'King van')

if __name__== '__main__':
    unittest.main()