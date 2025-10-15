import unittest
from Project2 import convex_hull

def sort_hull(hull):
    """Helper function to sort hull points for consistent comparison."""
    return sorted(hull, key=lambda p: (p[0], p[1]))

class TestConvexHull(unittest.TestCase):

    def test_with_interior_points(self):
        """Tests a set of points with several interior points."""
        points = [(0, 0), (10, 0), (0, 10), (10, 10), (2, 2), (5, 5), (8, 3)]
        expected_hull = [(0, 0), (0, 10), (10, 0), (10, 10)]
        result_hull = convex_hull(points)
        self.assertEqual(sort_hull(result_hull), sort_hull(expected_hull))
        print("Passed: With Interior Points")

    def test_collinear_points_horizontal(self):
        """
        Tests points on a horizontal line.
        """
        points = [(0, 5), (2, 5), (5, 5), (10, 5), (-3, 5)]
        expected_hull = [(-3, 5), (0, 5), (2, 5), (5, 5), (10, 5)]
        result_hull = convex_hull(points)
        self.assertEqual(sort_hull(result_hull), sort_hull(expected_hull))
        print("Passed: Collinear Points (Horizontal)")

    def test_collinear_points_vertical(self):
        """
        Tests points on a vertical line.
        """
        points = [(1, 1), (1, 5), (1, 0), (1, 10)]
        expected_hull = [(1, 0), (1, 1), (1, 5), (1, 10)]
        result_hull = convex_hull(points)
        self.assertEqual(sort_hull(result_hull), sort_hull(expected_hull))
        print("Passed: Collinear Points (Vertical)")

    def test_point_on_edge(self):
        """
        Tests a case where a point lies on an edge between two hull vertices.
        """
        points = [(0, 0), (10, 0), (0, 10), (5, 5)]
        expected_hull = [(0, 0), (0, 10), (5, 5), (10, 0)]
        result_hull = convex_hull(points)
        self.assertEqual(sort_hull(result_hull), sort_hull(expected_hull))
        print("Passed: Point on Edge")
        
    def test_less_than_three_points(self):
        """Tests inputs with fewer than 3 points."""
        points_2 = [(1, 1), (5, 5)]
        self.assertEqual(sort_hull(convex_hull(points_2)), sort_hull(points_2))

        points_1 = [(3, 3)]
        self.assertEqual(sort_hull(convex_hull(points_1)), sort_hull(points_1))
        print("Passed: Less Than Three Points")

if __name__ == '__main__':
    unittest.main()