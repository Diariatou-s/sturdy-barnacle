def chebyshev_distance(p1, p2):
    """
    Calculate the Chebyshev distance between two points by going through each 
    coordinate and computing the maximum absolute difference between corresponding 
    coordinates of the points.
    
    Args:
        p1 (iterable): The first point as an iterable of coordinates.
        p2 (iterable): The second point as an iterable of coordinates.

    Returns:
        int or float: The Chebyshev distance between the given two points.
    """
    max_diff = 0
    for x, y in zip(p1, p2):
        diff = abs(x - y)
        if diff > max_diff:
            max_diff = diff
    return max_diff

if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance(point1, point2)
    print("Chebyshev Distance:", distance)
