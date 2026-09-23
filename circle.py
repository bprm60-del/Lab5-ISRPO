import unittest
import math


def area(r):

    """
    Returns area of the circle with radius = r

        Input:
            r(float/int) : radius

        Output:
            circle_area(float/int) : area of the circle
    """
    return math.pi * r * r


def perimeter(r):

    """
    Returns perimeter of the circle with radius = r
    
        Input:
            r(float/int) : radius
    
        Output:
            circle_perimeter(float/int) : perimeter of the circle
    """
    
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    
    def test_circle_exists(self):
        res =  perimeter(-10)
        self.assertEqual(res, "Circle doesn't exists")
        
    def test_circle_area(self):
        res = area(10)
        self.assertEqual(res, 10*10*math.pi)
    
    def test_circle_perimeter(self):
        res = perimeter(7)
        self.assertEqual(res, 14*math.pi)