import unittest
import prime_number_check as PC


class TestPrimeNumber(unittest.TestCase):
    def test_is_prime(self):
        test_case_1 = PC.is_prime(8)
        test_case_2 = PC.is_prime()
        test_case_3 = PC.is_prime(98)
        self.assertEqual(test_case_1, False)
        self.assertEqual(test_case_2, False)
        self.assertEqual(test_case_3, True)


if __name__ == '__main__':
    unittest.main()
