import unittest
from app import draw_square, draw_circle, vector_move

class TestDrawingMethods(unittest.TestCase):
    
    def test_draw_square(self):
        self.assertEqual(draw_square((1,1), 2), [(1,1), (1,3), (3,1), (3,3)])
        

    def test_draw_circle(self):
        self.assertEqual(draw_circle((1,1), 2),[(1,3), (1,-1), (3,1), (-1,1)] )

    def test_vector_move(self):
        shape_array = [(1,3), (1,-1), (3,1), (-1,1)]
        result = [(2,4), (2,0), (4,2), (0,2)]
        vector = (1,1)
        self.assertEqual(vector_move(shape_array, vector), result)

if __name__ == "__main__":
    unittest.main()

