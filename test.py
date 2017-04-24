import unittest
from app import draw_square

class TestDrawingMethods(unittest.TestCase):
    
    def test_draw_square(self):
        self.assertEqual(draw_square((1,1), 2), [(1,1), (1,3), (3,1), (3,3)])
        

    # def test_draw_circle(self):
        # self.assertEqual(draw_circle((1,1), 2),[(1,3), (1,-1), (3,1), (-1,1)] )


if __name__ == "__main__":
    unittest.main()

