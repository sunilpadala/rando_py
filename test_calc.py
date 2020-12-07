import unittest
import simple_calc as sc

class calc_test(unittest.TestCase):

    def test_add(self):
        self.assertEqual(sc.add(23,45),68)


    def test_sub(self):
        self.assertEqual(sc.sub(24,21),3)


if __name__ == '__main__':
    unittest.main()
