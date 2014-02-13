from .point2d import Point2d
from .point3d import Point3d
from .intervals import Interval, Scale

"""
increase to encompass a point
increase/decrease by a margin
addition between two boxes
boolean operations?
two corner points
initialized with:
    intervals
    interval tuples
    width/height/depth
    points
    arbitrary geometry
"""

class Box2d(object):
    def __init__(self, width=200, height=100, *args, **kwargs):
        self.x = Interval(0, width)
        self.y = Interval(0, height)

    def center(self):
        """Get or set the center of the box"""
        return Point2d(
                self.x(0.5),
                self.y(0.5),
                )

class Box3d(object):
    def __init__(self, width=200, length=200, height=200,
            *args, **kwargs):
        self.x = Interval(0, width)
        self.y = Interval(0, length)
        self.z = Interval(0, height)

    def center(self):
        """Get or set the center of the box"""
        return Point3d(
                self.x(0.5),
                self.y(0.5),
                self.z(0.5),
                )


