import unittest

def area(a,b):

    """
    Returns area of rectangle

        Input:
            a(float/int) : one side of rectangle
            b(float/int) : other side of rectangle
        
        Output:
            rectangle_area(float/int) : area of rectangle
    """

    return a*b

def perimeter(a,b):

    """
    Returns perimeter of rectangle
    
        Input:
            a(float/int) : one side of rectangle
            b(float/int) : other side of rectangle
            
        Output:
            rectangle_perimeter(float/int) : perimeter of rectangle
    """

    return 2*(a+b)


class RectangleTestCase(unittest.TestCase):
    
    def test_rectangle_exists(self):
        res = perimeter(-1, 10000e2)
        self.assertEqual(res, "Rectangle doesn't exists")
    
    def test_rectangle_area(self):
        res = area(10, 5)
        self.assertEqual(res, 50)
    
    def test_rectangle_perimeter(self):
        res = perimeter(1, 1)
        self.assertEqual(res, 4)