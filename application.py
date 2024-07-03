import numpy as np

def chebyshev_distance(p1, p2):
    """
    Calculate the Chebyshev distance between two points by transforming them into numpy arrays,
    and then returning the maximum absolute difference between their corresponding coordinates.
    
    Args:
        p1 (iterable): The first point as an iterable of coordinates.
        p2 (iterable): The second point as an iterable of coordinates.

    Returns:
        int or float: The Chebyshev distance between the given two points.
    """
    
    p1_np_arr = np.array(p1)
    p2_np_arr = np.array(p2)
    
    return np.max(np.abs(p1_np_arr - p2_np_arr))

if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance(point1, point2)
    print("Chebyshev Distance:", distance)
