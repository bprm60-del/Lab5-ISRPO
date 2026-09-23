import unittest

def area(a,h):

    """
    Returns area of the triangle

        Input:
            a(float/int) : one side of the triangle
            h(float/int) : altititude drown to that side

        Output:
            triangle_area(float/int) : area of the triangle
    """

    return a*h/2

def perimeter(a,b,c):

    """
    Returns perimeter of the triangle
    
        Input:
            a(float/int) : first side of the triangle
            b(float/int) : second side of the triangle
            c(float/int) : third side of the traingle
    
        Output:
            triangle_perimeter(float/int) : perimeter of the triangle
    """

    sides = sorted([a,b,c])
    if sides[2] >= sides[0]+sides[1]:
        return "Triangle doesn't exists"
    
    return sum(sides)

class TriangleTestCase(unittest.TestCase):
    
    def test_triangle_exists_negative(self):
        res = perimeter(102,-1,100)
        self.assertEqual(res, "Triangle doesn't exists")
        
    def test_triangle_exists_impossibility(self):
        res = perimeter(100, 1000, 10000)
        self.assertEqual(res, "Triangle doesn't exists")
        
    def test_triangle_area(self):
        res = area(10, 5)
        self.assertEqual(res, 25)
        
    def test_triangle_perimeter(self):
        res = perimeter(6, 8, 10)
        self.assertEqual(res, 24)
    