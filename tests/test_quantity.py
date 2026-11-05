"""Regression tests for parse_quantity."""
import unittest

from warehouse.quantity import parse_quantity


class TestParseQuantity(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(parse_quantity("5"), 5)

    def test_positive_with_whitespace(self):
        self.assertEqual(parse_quantity("  10  "), 10)

    def test_zero_is_allowed(self):
        # Zero is a valid quantity (e.g. empty pick slot)
        self.assertEqual(parse_quantity("0"), 0)

    def test_negative_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "non-negative"):
            parse_quantity("-1")

    def test_large_negative_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "non-negative"):
            parse_quantity("-100")

    def test_non_integer_raises_value_error(self):
        with self.assertRaises(ValueError):
            parse_quantity("abc")


if __name__ == "__main__":
    unittest.main()
