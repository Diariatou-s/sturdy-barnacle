def chebyshev_distance(p1, p2):
    """
    Calculate the Chebyshev distance between two points by using a lambda function 
    and the map function to calculate the absolute difference between 
    corresponding coordinates of the two points, and then finding the maximum
    difference.
    
    Args:
        p1 (iterable): The first point as an iterable of coordinates.
        p2 (iterable): The second point as an iterable of coordinates.

    Returns:
        int or float: The Chebyshev distance between the given two points.
    """
    
    return max(map(lambda xy: abs(xy[0] - xy[1]), zip(p1, p2)))

if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance(point1, point2)
    print("Chebyshev Distance:", distance)
