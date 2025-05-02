import unittest

class Testisodd(unittest.TestCase):
    def Test_odd_num(self):
        self.assertTrue(is_odd(3))

if __name__ == '__main__':
    unittest.main()

    