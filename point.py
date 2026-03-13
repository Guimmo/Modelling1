class Point:
    """
    Simple class to represent a point in 2D space.
    """
    def __init__(self, x, y):
        """
        Constructor for Point class.
        :param x: x coordinate of point
        :param y: y coordinate of point
        """
        self.x = x     # x is a class attribute
        self.y = y
    def __str__(self):
        """
        String representation of Point class.
        :return: String representation of Point class
        """
        return f"P<{self.x},{self.y}>"

p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1.x, p1.y)
print(p2.x, p2.y)
print(p1, p2)  # P<1,2>

