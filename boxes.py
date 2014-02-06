from vector import Point
from intervals import Interval, Scale

def _parse_arg(arg):
    """The options for
    """

class Box2D(object):
    def __init__(self, width=200, height=100, *args, **kwargs):
        self.x = Interval(0, width)
        self.y = Interval(0, height)

    def center(self):
        """Get or set the center of the box"""
        return Point(
                self.x(0.5),
                self.y(0.5),
                )


class Box3D(object):
    def __init__(self, width=200, length=200, height=200,
            *args, **kwargs):
        self.x = Interval(0, width)
        self.y = Interval(0, length)
        self.z = Interval(0, height)

    def center(self):
        """Get or set the center of the box"""
        return (
                self.x(0.5),
                self.y(0.5),
                self.z(0.5),
                )



