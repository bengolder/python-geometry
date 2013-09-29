from vector import Point3d, Vector3d

class Line3d(object):
    """A 3d line object

    This class is used to represent an infinitely extensive line.
    Lines can be represented with a point and a vector parallel to the
    direction of the line.

    Lines can also be initialized with two points.

    If initialized with just a vector, the line will pass through the origing
    (0,0,0) and will be parallel with the given vector.

    """
    def __init__(self, vector, point):
        self.vector = vector
        self.point = point

    def __repr__(self):
        return 'Line3d( %s, %s )' % (self.vector, self.point)





