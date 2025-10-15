import math
import time
import random

def orientation(p, q, r):
    """
    Determine the orientation of three points (p, q, r).
    - Returns 0 if collinear
    - Returns 1 if clockwise
    - Returns -1 if anti-clockwise
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else -1

def brute_hull(points):
    """
    Compute convex hull for small sets (<=5 points) using brute force.
    Checks all pairs to see if they form a hull edge (all points on one side).
    Then sorts the hull points in anti-clockwise order around the centroid.
    """
    n = len(points)
    if n <= 2:
        return points[:]  # Base case: already a hull
    
    hull_set = set()
    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]
            # Line equation: a*x + b*y + c = 0
            a = p1[1] - p2[1]
            b = p2[0] - p1[0]
            c = p1[0] * p2[1] - p1[1] * p2[0]
            
            positive_side = 0
            negative_side = 0
            for k in range(n):
                val = a * points[k][0] + b * points[k][1] + c
                if val >= 0:
                    positive_side += 1
                if val <= 0:
                    negative_side += 1
            
            # If all points are on one side or collinear, it's a hull edge
            if positive_side == n or negative_side == n:
                hull_set.add(tuple(p1))  # Use tuple for set compatibility
                hull_set.add(tuple(p2))
    
    hull_points = list(hull_set)
    if len(hull_points) <= 1:
        return hull_points
    
    # Compute centroid
    centroid_x = sum(p[0] for p in hull_points) / len(hull_points)
    centroid_y = sum(p[1] for p in hull_points) / len(hull_points)
    
    # Sort by polar angle around centroid
    hull_points.sort(key=lambda p: math.atan2(p[1] - centroid_y, p[0] - centroid_x))
    return hull_points

def merge_hulls(left_hull, right_hull):
    """
    Merge two convex hulls by finding upper and lower tangents.
    Assumes hulls are sorted in anti-clockwise order.
    """
    n_left = len(left_hull)
    n_right = len(right_hull)
    if n_left == 0:
        return right_hull
    if n_right == 0:
        return left_hull
    
    # Find rightmost point in left hull
    rightmost_left_idx = 0
    for i in range(1, n_left):
        if left_hull[i][0] > left_hull[rightmost_left_idx][0]:
            rightmost_left_idx = i
    
    # Find leftmost point in right hull
    leftmost_right_idx = 0
    for i in range(1, n_right):
        if right_hull[i][0] < right_hull[leftmost_right_idx][0]:
            leftmost_right_idx = i
    
    # Find upper tangent
    upper_left_idx = rightmost_left_idx
    upper_right_idx = leftmost_right_idx
    done = False
    while not done:
        done = True
        while orientation(right_hull[upper_right_idx], left_hull[upper_left_idx], left_hull[(upper_left_idx + 1) % n_left]) >= 0:
            upper_left_idx = (upper_left_idx + 1) % n_left
        while orientation(left_hull[upper_left_idx], right_hull[upper_right_idx], right_hull[(upper_right_idx - 1) % n_right]) <= 0:
            upper_right_idx = (upper_right_idx - 1) % n_right
            done = False
    
    # Find lower tangent
    lower_left_idx = rightmost_left_idx
    lower_right_idx = leftmost_right_idx
    done = False
    while not done:
        done = True
        while orientation(left_hull[lower_left_idx], right_hull[lower_right_idx], right_hull[(lower_right_idx + 1) % n_right]) >= 0:
            lower_right_idx = (lower_right_idx + 1) % n_right
        while orientation(right_hull[lower_right_idx], left_hull[lower_left_idx], left_hull[(lower_left_idx - 1) % n_left]) <= 0:
            lower_left_idx = (lower_left_idx - 1) % n_left
            done = False
    
    # Build the merged hull
    merged = []
    idx = upper_left_idx
    merged.append(left_hull[upper_left_idx])
    while idx != lower_left_idx:
        idx = (idx + 1) % n_left
        merged.append(left_hull[idx])
    
    idx = lower_right_idx
    merged.append(right_hull[lower_right_idx])
    while idx != upper_right_idx:
        idx = (idx + 1) % n_right
        merged.append(right_hull[idx])
    
    return merged

def divide_and_conquer(points):
    """
    Recursive divide-and-conquer function to compute convex hull.
    Divides points into left/right, computes hulls recursively, then merges.
    """
    if len(points) <= 5:
        return brute_hull(points)
    
    mid = len(points) // 2
    left_points = points[:mid]
    right_points = points[mid:]
    
    left_hull = divide_and_conquer(left_points)
    right_hull = divide_and_conquer(right_points)
    
    return merge_hulls(left_hull, right_hull)

def convex_hull(points):
    """
    Main function to compute the convex hull.
    Removes duplicates, sorts by x (then y), and calls divide-and-conquer.
    """
    # Remove duplicates by converting to set (points as tuples)
    points = list(set(tuple(p) for p in points))
    if len(points) <= 1:
        return points
    
    # Sort by x-coordinate, then y-coordinate
    points.sort(key=lambda p: (p[0], p[1]))
    
    return divide_and_conquer(points)

# Testing section to log times for different n (using random points)
if __name__ == "__main__":
    random.seed(42)  # For reproducibility
    for n in [1000, 5000, 10000, 50000, 100000, 500000, 1000000]:
        points = [(random.random() * 1000, random.random() * 1000) for _ in range(n)]
        start = time.time()
        hull = convex_hull(points)
        end = time.time()
        print(f"For n={n}, time={end - start:.6f} seconds, hull size={len(hull)}")