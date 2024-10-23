import unittest
from calculation import hitung_total

class TestHitungTotal(unittest.TestCase):
    def test_hitung_total_pi(self):
        # Test case 1: Categories = 'PI', Fee = 20000, Duration = 30, Percentage Discount = 5
        row = {'Categories': 'PI', 'Fee': 20000, 'Duration': 30, 'Percentage Discount': 5}
        expected_output = 20000 * 30 - 1000  # Expected output based on the calculation
        self.assertEqual(hitung_total(row), expected_output)

    def test_hitung_total_non_pi(self):
        # Test case 2: Categories = 'Non-PI', Fee = 25000, Duration = 40, Percentage Discount = 10
        row = {'Categories': 'Non-PI', 'Fee': 25000, 'Duration': 40, 'Percentage Discount': 10}
        expected_output = 25000 * 40 - (2500 + 2500 * 0.02)  # Expected output based on the calculation
        self.assertEqual(hitung_total(row), expected_output)

    def test_hitung_total_custom_discount(self):
        # Test case 3: Categories = 'PI', Fee = 30000, Duration = 35, Percentage Discount = 5
        row = {'Categories': 'PI', 'Fee': 30000, 'Duration': 35, 'Percentage Discount': 5}
        expected_output = 30000 * 35 - 1500  # Expected output based on the calculation
        self.assertEqual(hitung_total(row), expected_output)

    def test_hitung_total_zero_discount(self):
        # Test case 4: Categories = 'Non-PI', Fee = 20000, Duration = 30, Percentage Discount = 0
        row = {'Categories': 'Non-PI', 'Fee': 20000, 'Duration': 30, 'Percentage Discount': 0}
        expected_output = 20000 * 30  # Expected output based on the calculation (no discount)
        self.assertEqual(hitung_total(row), expected_output)

if __name__ == '__main__':
    unittest.main()
