import unittest
from exercise import createDict


class ExerciseTest(unittest.TestCase):

    def test_keys_and_values(self):
        response = createDict(['a', 'b'], [1, 2])
        self.assertEqual(response, {'a': 1, 'b': 2})

    def test_other_keys_and_values(self):
        response = createDict(['z', 'x'], [4, 5])
        self.assertEqual(response, {'z': 4, 'x': 5})

    def test_keys_with_not_enough_values(self):
        response = createDict(['a', 'b', 'c'], [1, 2])
        self.assertEqual(response, {'a': 1, 'b': 2, 'c': None})

    def test_ignore_if_there_not_enough_keys(self):
        response = createDict(['a', 'b', 'c'], [1, 2, 3, 4])
        self.assertEqual(response, {'a': 1, 'b': 2, 'c': 3})

if __name__ == '__main__':
    unittest.main()
