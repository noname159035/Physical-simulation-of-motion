import unittest
from metods import *

class metod_test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_circle_w(10.4, 5.2), 2)
    def test_2(self):
        self.assertEqual(find_circle_U(10, 5), 50)
    def test_3(self):
        self.assertEqual(find_circle_a_o(5, 5), 5)
    def test_4(self):
        self.assertEqual(find_circle_S(10, 5), 50)
    def test_5(self):
        self.assertEqual(find_circle_T(10, 2), 1.256)
    def test_6(self):
        self.assertEqual(find_circle_delta_s(100, 5, 2, 9), 60)
    def test_7(self):
        self.assertEqual(find_circle_delta_f(65, 5), 13)
    def test_8(self):
        self.assertEqual(find_circle_U2(15, 5), 3)
    def test_9(self):
        self.assertEqual(find_circle_R(10.4, 5.2), 2)
    def test_10(self):
        self.assertEqual(find_circle_R2(20, 5, 2), 2)
    def test_11(self):
        self.assertEqual(find_circle_U3(20, 5), 10)
    def test_12(self):
        self.assertEqual(find_circle_t(10, 2.5), 4)

    def test_13(self):
        self.assertEqual(find_angle_U_st_x(10, 180), -10)
    def test_14(self):
        self.assertEqual(find_angle_U_st_x(10, 0), 10)
    def test_15(self):
        self.assertEqual(find_angle_t_fall(29.43), 3)
    def test_16(self):
        self.assertEqual(find_angle_H(10, 19.62), 29.62)
    def test_17(self):
        self.assertEqual(find_angle_L(10, 3), 30)
    def test_18(self):
        self.assertEqual(find_angle_U_fin(19.62, 0), 19.62)
    def test_19(self):
        self.assertEqual(find_angle_U_st(19.62, 19.62), 0)
    def test_20(self):
        self.assertEqual(find_angle_h_st(2, 100), 80.38)
    def test_21(self):
        self.assertEqual(find_angle_d(19.62, 1), 90)
    def test_22(self):
        self.assertEqual(find_angle_t(10, 5), 2))