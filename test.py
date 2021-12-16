import unittest
from metods import *


class metod_test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_circle_w(10, 5), 2)
    def test_2(self):
        self.assertEqual(find_circle_U(10, 5), 50)
    def test_3(self):
        self.assertEqual(find_circle_a_o(5, 5), 5)
    def test_4(self):
        self.assertEqual(find_circle_S(10, 5), 2)
    def test_5(self):
        self.assertEqual(find_circle_T(10, 2), 31.4)
    def test_6(self):
        self.assertEqual(find_circle_delta_s(100, 5, ), 50)
    def test_7(self):
        self.assertEqual(find_circle_a_o(5, 5), 5)
    def test_8(self):
        self.assertEqual(find_circle_S(10, 5), 2)

