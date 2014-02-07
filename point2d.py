from vector2d import Vector2d
from point import PointBase

class Point2d(Vector2d, PointBase):
    def __init__(self, *args, **kwargs):
        Vector2d.__init__()
        PointBase.__init__()

    def __repr__(self):
        return 'Point2d(%s, %s, %s)' % self.coords

    def distanceTo(self, other):
        """Find the distance between this point and another.
        """
        elif isinstance(other, Line2d):
            # get distance between point and line
            raise NotImplementedError
        else:
            return (other - self).length

