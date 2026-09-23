import unittest

def area(a):

    """
    Return area of the square with side = a

        Input:
            a(float/int) : side of square
        
        Output:
            square_area(float/int) : area of square
    """

    return a * a


def perimeter(a):

    """
    Return perimeter of the square with side = a
    
        Input:
            a(float/int) : side of square
            
        Output:
            square_perimeter(float/int) : perimeter of square
    """

    return 4 * a



class SquareTestCase(unittest.TestCase):
    
    def test_square_exists(self):
        res = perimeter(-5)
        self.assertEqual(res, "Square doesn't exists")
        
    def test_square_area(self):
        res = area(45.1)
        self.assertEqual(res, 45.1*45.1)
    
    def test_square_perimeter(self):
        res = perimeter(0.0001)
        self.assertEqual(res, 0.0004)
