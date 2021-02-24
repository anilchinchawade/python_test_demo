import mathlib
import unittest


class test_Class(unittest.TestCase):
    def test_total(self):
        res = mathlib.total(3,4)
        assert res == 7

    def test_multiply(self):
        res = mathlib.multiply(3,4)
        assert res == 12


if __name__ == "__main__":
    unittest.main()