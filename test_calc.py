import unittest
import calc_implementer as ci

class calc_test(unittest.TestCase):

    def test_add(self):
        self.assertEqual(ci.add(23,45),68)


    def test_sub(self):
        self.assertEqual(ci.sub(24,21),3)
        self.assertEqual(ci.sub(55,21),34)


if __name__ == '__main__':
    unittest.main()
