import unittest
from main import add, substract, multyply, divide, check, rem_divide

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertNotEqual(add(3, 7), 9)

    def test_subtract(self):
        self.assertEqual(substract(7, 4), 3)
        self.assertNotEqual(substract(4, 2), 1)

    def test_multiply(self):
        self.assertNotEqual(multyply(2, 5), 12)
        self.assertEqual(multyply(3, 6), 18)

    def test_divide_success(self):
        self.assertNotEqual(divide(4, 2), 3)
        self.assertEqual(divide(20, 5), 4)

    def test_divide_by_0(self):
        self.assertRaises(ValueError, divide, 6, 0)

    def test_divide_success_rem(self):
        self.assertNotEqual(rem_divide(4, 2), 1)
        self.assertEqual(rem_divide(20, 5), 0)
        self.assertEqual(rem_divide(7, 3), 1)

    def test_divide_rem_by_0(self):
        self.assertRaises(ValueError, rem_divide, 6, 0)

    def test_check(self):
        self.assertTrue(check(2))
        self.assertTrue(check(6))
        self.assertTrue(check(222))
        self.assertFalse(check(3))
        self.assertTrue(not check(111))
        self.assertTrue(not check(113))

if __name__ == '__main__':
    unittest.main()