import math
from real import Real
import unittest


class TestRealMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Real.PRECISION = 30
        Real.MAX_MANTISS = 10000
        Real.MIN_MANTISS = -100

    def assert_equal(self, real, double):
        failed = False
        try:
            self.assertTrue(abs(float(str(real)) - float(double)) < 1e-6)
        except AssertionError:
            failed = True
        if failed:
            self.assertEqual(float(str(real)), float(double))

    def test_creation(self):
        self.assert_equal(Real(1), 1)
        self.assert_equal(Real(99), 99)
        self.assert_equal(Real(31415), 31415)

    def test_creation_error_when_not_integer(self):
        with self.assertRaises(TypeError):
            Real(1.0)

    def test_negative(self):
        self.assert_equal(-Real(5), -5)

    def test_sum_diff_long(self):
        self.assert_equal(Real(1) + Real(0), 1 + 0)
        self.assert_equal(Real(1) + Real(123), 1 + 123)
        self.assert_equal(Real(133) - Real(135), 133 - 135)

    def test_multiplication_long(self):
        self.assert_equal(Real(1) * Real(2), 1 * 2)
        self.assert_equal(Real(14) * Real(0), 0)
        self.assert_equal(Real(56) * Real(24), 56 * 24)

    def test_division(self):
        self.assert_equal(Real(1) / Real(3), 1 / 3)
        self.assert_equal(Real(99) / Real(33), 3)
        self.assert_equal(Real(123) / Real(7), 123 / 7)

    def test_summ_diff_fraction(self):
        self.assert_equal(Real(1) / Real(3) + Real(4) / Real(5), 1 / 3 + 4 / 5)
        self.assert_equal(Real(100) / Real(3) + Real(3) / Real(7), 100 / 3 + 3 / 7)
        self.assert_equal(Real(0) / Real(3) + Real(4) / Real(5), 4 / 5)

    def test_multiplication_fraction(self):
        self.assert_equal((Real(1) / Real(3)) * (Real(4) / Real(5)), 1 / 3 * 4 / 5)
        self.assert_equal((Real(100) / Real(3)) * (Real(3) / Real(7)), 100 / 3 * 3 / 7)
        self.assert_equal((Real(0) / Real(3)) * (Real(4) / Real(5)), 0)

    def test_division_error_when_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.assert_equal(Real(4) / Real(0), 0)

    def test_floordiv(self):
        self.assertTrue(Real(123) // Real(12), 123 // 12)
        self.assertTrue((Real(123) / Real(7)) // (Real(12) / Real(13)), (123 / 7) // (12 / 13))

    def test_mod(self):
        self.assertTrue(Real(123) % Real(12), 123 % 12)
        self.assertTrue((Real(123) / Real(7)) % (Real(12) / Real(13)), (123 / 7) % (12 / 13))

    def test_sqrt(self):
        self.assert_equal(Real(0).sqrt(), 0)
        self.assert_equal(Real(123).sqrt(), math.sqrt(123))
        self.assert_equal((Real(123) / Real(33)).sqrt(), math.sqrt(123 / 33))

    def test_pow(self):
        self.assertTrue(False)

    def test_arc_functions(self):
        self.assert_equal(Real.pi(), math.pi)
        self.assert_equal(Real(0).asin(), 0)
        self.assert_equal((Real(3) / Real(7)).asin(), math.asin(3 / 7))
        self.assert_equal((Real(3) / Real(7)).acos(), math.acos(3 / 7))
        self.assert_equal((Real(3) / Real(7)).atan(), math.atan(3 / 7))

    def test_trig_functions(self):
        self.assert_equal(Real(0).sin(), 0)
        self.assert_equal((Real.pi() / Real(2)).sin(), 1)
        self.assert_equal(Real(0).tan(), 0)
        self.assert_equal((Real(123) / Real(779)).sin(), math.sin(123/779))
        self.assert_equal((Real(123) / Real(779)).cos(), math.cos(123/779))
        self.assert_equal((Real(123) / Real(779)).tan(), math.tan(123/779))

    def test_comparators(self):
        # assertTrue
        self.assertTrue(Real(0)  < Real(1))
        self.assertTrue(Real(-3) < Real(2))
        self.assertTrue(Real(-3) < Real(-2))
        self.assertTrue(Real(1)  > Real(0))
        self.assertTrue(Real(2)  > Real(-3))
        self.assertTrue(Real(-2) > Real(-3))
        self.assertTrue(Real(5) == Real(5))
        self.assertTrue(Real(5) <= Real(6))
        self.assertTrue(Real(5) <= Real(5))
        self.assertTrue(Real(6) >= Real(5))
        self.assertTrue(Real(5) >= Real(5))
        # assertFalse
        self.assertFalse(Real(0)  > Real(1))
        self.assertFalse(Real(-3) > Real(2))
        self.assertFalse(Real(-3) > Real(-2))
        self.assertFalse(Real(1)  < Real(0))
        self.assertFalse(Real(2)  < Real(-3))
        self.assertFalse(Real(-2) < Real(-3))
        self.assertFalse(Real(5) == Real(6))
        self.assertFalse(Real(5) >= Real(6))
        self.assertFalse(Real(6) <= Real(5))

if __name__ == '__main__':
    unittest.main()

