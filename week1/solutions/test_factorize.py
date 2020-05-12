import unittest
import factorize


class TestFactorize(unittest.TestCase):

    def test_wrong_types_raise_exception(self):
        cases = ('string', 1.5)
        for case in cases:
            with self.subTest(x=case):
                self.assertRaises(TypeError, factorize.factorize, case)

    def test_negative(self):
        cases = (-1, -10, -100)
        for case in cases:
            with self.subTest(x=case):
                self.assertRaises(ValueError, factorize.factorize, case)

    def test_zero_and_one_cases(self):
        cases = (0, 1)
        for case in cases:
            with self.subTest(x=case):
                self.assertEqual(factorize.factorize(case), tuple([case]))

    def test_simple_numbers(self):
        cases = [
            (3, (3,)),
            (13, (13,)),
            (29, (29,)),
        ]
        for case, answer in cases:
            with self.subTest(x=case):
                self.assertEqual(factorize.factorize(case), answer)

    def test_two_simple_multipliers(self):
        cases = [
            (6, (2, 3)),
            (26, (2, 13)),
            (121, (11, 11)),
        ]
        for case, answer in cases:
            with self.subTest(x=case):
                self.assertEqual(factorize.factorize(case), answer)

    def test_many_multipliers(self):
        cases = [
            (1001, (7, 11, 13)),
            (9699690, (2, 3, 5, 7, 11, 13, 17, 19)),
        ]
        for case, answer in cases:
            with self.subTest(x=case):
                self.assertEqual(factorize.factorize(case), answer)


if __name__ == "__main__":
    print(factorize.__doc__)
    unittest.main()
