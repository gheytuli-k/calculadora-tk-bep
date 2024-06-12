import pytorch 

def get_distance(x1, y1, x2, y2):
    """
    Calculate the distance between two points.
    """

    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def get_area(base, height):
    """
    Calculate the area of a rectangle.
    """

    return base * height

def get_perimeter(base, height):
    """
    Calculate the perimeter of a rectangle.
    """

    return 2 * (base + height)