# -*- coding: utf-8 -*-
import unittest

from triangle import KindOfTriangle


class KindOfTriangleTests(unittest.TestCase):

    def test_triangle_validity_negative(self):
        # negative value
        with self.assertRaises(ValueError):
            KindOfTriangle(-1, 2, 3)

    def test_triangle_validity_zero(self):
        # negative value
        with self.assertRaises(ValueError):
            KindOfTriangle(2, 2, 0)

    def test_triangle_validity_side_lengths_off(self):
        # 2 + 3 is not > 8
        with self.assertRaises(ValueError):
            KindOfTriangle(8, 2, 3)

    def test_triangle_error_not_enough_sides(self):
        # missing value
        with self.assertRaises(TypeError):
            KindOfTriangle(8, 2,)

    def test_triangle_is_valid_decimal(self):
        triangle = KindOfTriangle(2.5, 2.5, 2.5)
        self.assertTrue(triangle.is_equilateral())

    def test_triangle_is_equilateral(self):
        triangle = KindOfTriangle(2, 2, 2)
        self.assertTrue(triangle.is_equilateral())
        self.assertTrue(triangle.TRIANGLE_TYPES[triangle.EQUILATERAL])

    def test_triangle_is_isosceles(self):
        triangle = KindOfTriangle(2, 2, 3)
        self.assertTrue(triangle.is_isosceles())
        self.assertTrue(triangle.TRIANGLE_TYPES[triangle.ISOSCELES])

    def test_triangle_is_scalene(self):
        triangle = KindOfTriangle(1, 2, 3)
        self.assertTrue(triangle.is_scalene())
        self.assertTrue(triangle.TRIANGLE_TYPES[triangle.SCALENE])

    def test_name_of_triangle(self):
        triangle = KindOfTriangle(2, 2, 3)
        self.assertEqual(triangle.name_of_triangle(), triangle.ISOSCELES)

if __name__ == '__main__':
    unittest.main()
