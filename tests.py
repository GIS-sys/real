from real import Real
import unittest


class TestRealMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Real.PRECISION = 30
        Real.MAX_MANTISS = 10000
        Real.MIN_MANTISS = -100

    def assert_equal(self, real, double):
        try:
            self.assertTrue(abs(float(str(real)) - float(double)) < 1e-6)
        except AssertionError:
            self.assertEqual(float(str(real)), float(double))

    def test_creation(self):
        self.assert_equal(Real(1), 1.0)
        self.assert_equal(Real(99), 99.0)
        self.assert_equal(Real(31415), 31415.0)

    def test_creation_error_when_not_integer(self):
        with self.assertRaises(TypeError):
            Real(1.0)

    def test_negative(self):
        self.assert_equal(-Real(5), -5.0)

    def test_sum_diff_long(self):
        self.assert_equal(Real(1) + Real(0), 1.0 + 0.0)
        self.assert_equal(Real(1) + Real(123), 1.0 + 123.0)
        self.assert_equal(Real(133) - Real(135), 133.0 - 135.0)

    def test_multiplication_long(self):
        self.assert_equal(Real(1) * Real(2), 1.0 * 2.0)
        self.assert_equal(Real(14) * Real(0), 0.0)
        self.assert_equal(Real(56) * Real(24), 56.0 * 24.0)

    def test_division(self):
        self.assert_equal(Real(1) / Real(3), 1 / 3)
        self.assert_equal(Real(99) / Real(33), 3.0)
        self.assert_equal(Real(123) / Real(7), 123 / 7)

    def test_summ_diff_fraction(self):
        self.assert_equal(Real(1) / Real(3) + Real(4) / Real(5), 1 / 3 + 4 / 5)
        self.assert_equal(Real(100) / Real(3) + Real(3) / Real(7), 100 / 3 + 3 / 7)
        self.assert_equal(Real(0) / Real(3) + Real(4) / Real(5), 4 / 5)

    def test_multiplication_fraction(self):
        self.assert_equal((Real(1) / Real(3)) * (Real(4) / Real(5)), 1 / 3 * 4 / 5)
        self.assert_equal((Real(100) / Real(3)) * (Real(3) / Real(7)), 100 / 3 * 3 / 7)
        self.assert_equal((Real(0) / Real(3)) * (Real(4) / Real(5)), 0.0)

    def test_division_error_when_zero(self):
        pass

    def test_sqrt(self):
        pass

    def test_trig_functions(self):
        pass

    def test_arc_functions(self):
        pass

if __name__ == '__main__':
    unittest.main()

