import unittest
import calc_implementer as ci

class calcTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(ci.add(23,45),68)


    def test_sub(self):
        self.assertEqual(ci.sub(24,21),3)
        self.assertEqual(ci.sub(55,21),34)

    def test_my_own(self):
        self.assertEquals(ci.add(23,34,21),ci.sub(0,-23,-34,-21),'success')


if __name__ == '__main__':
    unittest.main()
