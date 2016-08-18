# -*- coding: utf-8 -*-
"""
This script will be used to determine what a type of triangle
The matching types are stored in the class KindOfTriangle

Description of types:
    - equilateral: 3 equal sides 3, 3, 3
    - isosceles: at least 2 equal sides 2, 2, 1
    - scalene: 3 unequal sides 1, 2, 3

"""


class KindOfTriangle:

    def __init__(self, x, y, z):
        """
        :params  x, y, z: lengths of a triangle
        """
        self.x = x
        self.y = y
        self.z = z
        # check validity right away
        self._check_validity_of_triangle()

        # triangle types
        self.EQUILATERAL = "equilateral"
        self.ISOSCELES = "isosceles"
        self.SCALENE = "scalene"

        # build triangle name dict
        self.TRIANGLE_TYPES = {
            self.EQUILATERAL: self.is_equilateral(),
            self.ISOSCELES: self.is_isosceles(),
            self.SCALENE: self.is_scalene()
        }

    def _check_validity_of_triangle(self):
        """
        initial check to determine if passed in values could form a triangle
        :return: ValueError or True
        """
        if self.x <= 0 or self.y <= 0 or self.z <= 0:
            raise ValueError("Negative or zero side in triangle.")
        elif (self.x > self.y + self.z) or (self.y > self.x + self.z) or (self.z > self.y + self.x):
            raise ValueError("Impossible triangle.")
        else:
            return True

    def is_equilateral(self):
        """
        if the sides are all equal then the triangle is equilateral
        :return: boolean
        """
        return self.x == self.y == self.z

    def is_isosceles(self):
        """
        if 2 sides are equal then the triangle is isosceles
        :return: boolean
        """
        return self.x == self.y or self.x == self.z

    def is_scalene(self):
        """
        if the sides are not isosceles then the triangle must be a scalene
        :return: boolean
        """
        return not self.is_isosceles()

    def name_of_triangle(self):
        """
        :return: English name of triangle
        """
        return next((key for key, value in self.TRIANGLE_TYPES.items() if value), None)

