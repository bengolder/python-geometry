from vector3d import Vector3d
from point3d import Point3d

class Line3d(object):
    """A 3d line object

    This class is used to represent an infinitely extensive line.
    Lines can be represented with a point and a vector parallel to the
    direction of the line.

    Lines can also be initialized with two points.

    If initialized with just a vector, the line will pass through the origing
    (0,0,0) and will be parallel with the given vector.

    """
    def __init__(self, *args):
        if isinstance(args[0], Vector3d):
            # assume we have a parallel vector then a point
            self.vector = args[0]
            self.point = args[1]
        else:
            # assume we have two points
            self.vector = args[1] - args[0]
            self.point = args[0]

    def __repr__(self):
        return 'Line3d( %s, %s )' % (self.vector, self.point)




class LineSegment2d(object):
    def __init__(self, start_point, end_point):
        self.coords = (start_point, end_point)
    def __repr__(self):
        return 'LineSegment2d( %s, %s )' % self.coords

