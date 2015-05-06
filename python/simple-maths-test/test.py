import unittest
from exercise import number_property, is_prime, is_even, is_multiple_of_10


class TestSimpleMathsTestExercice(unittest.TestCase):

    def test_check_if_number_is_prime(self):
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))

    def test_check_if_number_is_not_prime(self):
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(20))

    def test_check_if_number_is_less_than_1_should_not_be_prime(self):
        self.assertFalse(is_prime(0))

    def test_check_if_number_is_even(self):
        self.assertTrue(is_even(2))

    def test_check_if_number_is_odd(self):
        self.assertFalse(is_even(3))

    def test_check_if_number_is_multiple_of_10(self):
        self.assertTrue(is_multiple_of_10(10))

    def test_check_if_number_is_not_multiple_of_10(self):
        self.assertFalse(is_multiple_of_10(11))

    def test_check_number_prime_even_and_multiple_of_10(self):
        self.assertEqual(number_property(7), [True, False, False])
        self.assertEqual(number_property(10), [False, True, True])
        self.assertEqual(number_property(-7), [False, False, False])
        self.assertEqual(number_property(-10), [False, True, True])
        self.assertEqual(number_property(125), [False, False, False])


if __name__ == '__main__':
    unittest.main()
