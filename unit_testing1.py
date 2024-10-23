import unittest
from calculation import hitung_diskon

class TestHitungDiskon(unittest.TestCase):
    def test_hitung_diskon_case1(self):
        # Test case 1: Fee = 20000, Percentage Discount = 5
        row = {'Fee': 20000, 'Percentage Discount': 5}
        expected_output = 1000  # Expected output based on the calculation
        self.assertEqual(hitung_diskon(row), expected_output)

    def test_hitung_diskon_case2(self):
        # Test case 2: Fee = 25000, Percentage Discount = 10
        row = {'Fee': 25000, 'Percentage Discount': 10}
        expected_output = 2500  # Expected output based on the calculation
        self.assertEqual(hitung_diskon(row), expected_output)

    def test_hitung_diskon_case3(self):
        # Test case 3: Fee = 30000, Percentage Discount = 5
        row = {'Fee': 30000, 'Percentage Discount': 5}
        expected_output = 1500  # Expected output based on the calculation
        self.assertEqual(hitung_diskon(row), expected_output)

if __name__ == '__main__':
    unittest.main()
