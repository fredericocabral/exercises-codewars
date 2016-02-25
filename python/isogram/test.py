import unittest
from exercise import solution


class Test_Isogram(unittest.TestCase):

    def test_no_repeat_letter(self):
        self.assertEqual(solution('Dermatoglyphics'), True)

    def test_repeat_letter(self):
        self.assertEqual(solution('aba'), False)

    def test_ignore_letter_case(self):
        self.assertEqual(solution('moOse'), False)

    def test_empty_is_valid_isogram(self):
        self.assertEqual(solution(''), True)

if __name__ == '__main__':
    unittest.main()
