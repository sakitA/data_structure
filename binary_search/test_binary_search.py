import unittest

from binary_search import algo


class MyTestCase(unittest.TestCase):
    massiv = [3, 5, 2, 1, 20, 12, 10]

    massiv.sort()

    def test_mektub_var(self):
        # gözlənilən nəticə
        expected = 3

        # real nəticə
        actual = algo.binary_search(mektublar=self.massiv, kod=3)

        self.assertEqual(expected, actual)

    def test_mektub_yoxdur(self):
        # gözlənilən nəticə
        expected = "Məktub yoxdur"

        # real nəticə
        actual = algo.binary_search(mektublar=self.massiv, kod=33)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
