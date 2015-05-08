import unittest
from exercise import open_or_senior


class TestCategorizeNewMember(unittest.TestCase):

    def test_senior_member(self):
        response = open_or_senior([[55, 8], [56, 12]])
        self.assertEqual(response, ['Senior', 'Senior'])

    def test_open_member(self):
        result = open_or_senior([[20, 2], [10, 5]])
        self.assertEqual(result, ['Open', 'Open'])

    def test_open_and_senior_member(self):
        result = open_or_senior([[70, 8], [18, -1]])
        self.assertEqual(result, ['Senior', 'Open'])


if __name__ == '__main__':
    unittest.main()
